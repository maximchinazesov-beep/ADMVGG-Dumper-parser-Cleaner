# Author: maximchinazesov (https://github.com/maximchinazesov-beep)
import os
import httpx
import json

# --- CONFIG ---
CATEGORIES = ["pets", "eggs", "petwear", "strollers", "food", "vehicles", "toys", "gifts", "stickers"]
TOKEN = "" # Paste ur token here. [read readme to get it]
KEYS_TO_DELETE = {"id", "lastUpdatedAt", "origin"}

# --- EXTRACTOR ---
def extract_array(data, category):
    if isinstance(data, dict):
        if category in data and isinstance(data[category], list) and len(data[category]) > 0 and "name" in data[category][0]:
            return data[category]
        if "items" in data and isinstance(data["items"], list) and len(data["items"]) > 0 and "name" in data["items"][0]:
            return data["items"]
        for val in data.values():
            res = extract_array(val, category)
            if res: return res
    elif isinstance(data, list):
        for item in data:
            res = extract_array(item, category)
            if res: return res
    return None

# --- PIPELINE ---
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(script_dir, "amvgg_database.json")
    
    final_data = {}

    with httpx.Client(timeout=15.0) as client:
        for cat in CATEGORIES:
            try:
                url = f"https://amvgg.com/values/{cat}?_rsc={TOKEN}"
                resp = client.get(url, headers={"User-Agent": "Mozilla/5.0"})
                
                json_str = None
                for line in resp.text.splitlines():
                    if '{"id":"' in line:
                        json_str = line.split(':', 1)[1] if ':' in line else line
                        break
                        
                if not json_str:
                    print(f"[-] {cat.upper()}: data length pattern not found")
                    continue

                parsed_rsc = json.loads(json_str)
                items = extract_array(parsed_rsc, cat)
                
                if not items:
                    print(f"[-] {cat.upper()}: massive not found")
                    continue

                cleaned_category = []
                for item in items:
                    cleaned_item = {}
                    for k, v in item.items():
                        if k in KEYS_TO_DELETE:
                            continue
                        if isinstance(v, str):
                            try:
                                cleaned_item[k] = float(v) if '.' in v else int(v)
                            except ValueError:
                                cleaned_item[k] = v
                        else:
                            cleaned_item[k] = v
                    cleaned_category.append(cleaned_item)
                
                sort_key = "regularValue" if cat == "pets" else "value"
                
                def get_val(x):
                    val = x.get(sort_key, 0)
                    return float(val) if val is not None else 0.0
                    
                cleaned_category.sort(key=get_val, reverse=True)
                final_data[cat] = cleaned_category
                
                print(f"[+] {cat.upper()}: parsed and cleaned {len(cleaned_category)} шт.")

            except Exception as e:
                print(f"[-] {cat.upper()}: error -> {e}")

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
        
    print(f"\Ready. path: {save_path}")

if __name__ == "__main__":
    main()