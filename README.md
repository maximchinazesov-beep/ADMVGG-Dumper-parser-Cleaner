AMVGG (Adopt Me Values) Fast Parser

A lightning-fast quote parser for amvgg.com (Adopt Me Values) that extracts clean data via the hidden Next.js API. The script works without heavy browser emulation and aggregates up-to-date prices for all item categories into a single JSON file.

**Features**
* Full coverage: Collects absolutely all categories from the site—from pets and eggs to vehicles, toys, and stickers.
* Surgical cleaning: Automatically strips out React Server Components system junk and removes utility keys (id, origin, lastUpdatedAt).
* Smart sorting: Orders arrays strictly in descending order of value (regularValue for pets, value for everything else).
* Structure preservation: Carefully transfers all in-game characteristics (Regular, Neon, Mega, Demand, Fly/Ride), converting string numbers to native floats.

**Why it's cool**
The code works head-on via direct HTTP requests—no Selenium crutches or bulky browser engines. The output is a perfectly structured database ready for integration. You can immediately upload the file to a host and pull it via HttpService:JSONDecode() directly into your Lua scripts. This is the ideal foundation for custom UI menus, pet visualizer overlays, and trade automation systems in Adopt Me!, allowing you to close out the task and finish your interface tab today.

**Guide to getting the token (_rsc)**
The site's architecture is tied to the Next.js build hash. If the site receives a global update, the token will change, and the script will throw an error. To fix it, you need to update the TOKEN variable in the code:
* Open amvgg.com in your browser and press F12 (Developer Tools).
* Go to the Network tab and enable the Fetch/XHR filter.
* Refresh the page (F5) or click on any category.
* Find a system request matching the category name (e.g., pets?_rsc=... or petwear?_rsc=...).
* Copy the string of characters after _rsc= (e.g., Q2bj4kjiKLs856Aw) and paste it into the parser's config.

---

Парсер-дампер для сайта ADMVGG от рио на базе

Работает в касание, на выходе имеем базу json. Без эмуляций и прочего.

**Возможности**
* Полный охват: собирает абсолютно все категории с сайта — от питомцев и яиц до транспорта, игрушек и стикеров. (вы можете сами выбирать что вам сохранять)
* Хирургическая очистка: автоматически вырезает системный мусор React Server Components и удаляет служебные ключи (id, origin, lastUpdatedAt). (также можете выбирать сами)
* Умная сортировка: выстраивает массивы строго по убыванию стоимости (regularValue для петов, value для остального).
* Сохранение структуры: бережно переносит все игровые характеристики (Regular, Neon, Mega, Demand, Fly/Ride), конвертируя строковые числа в полноценный float.

**В чем кайф**
Код работает «в лоб» через прямые HTTP-запросы — никаких костылей с Selenium или громоздких браузерных движков. На выходе генерируется идеально ровная база данных, готовая к интеграции. Файл можно сразу закидывать на хостинг и дергать через HttpService:JSONDecode() прямо в твоих Lua-скриптах. Это идеальный фундамент для кастомных UI-меню, оверлеев визуализатора петов и систем автоматизации трейдов в Adopt Me!, позволяющий закрыть задачу и доделать нужную вкладку интерфейса уже сегодня.

**Гайд на получение токена (_rsc)**
Архитектура сайта завязана на хэш сборки Next.js. Если сайт получит глобальное обновление, токен изменится, и скрипт выдаст ошибку. Для починки нужно обновить переменную TOKEN в коде:
* Открой amvgg.com в браузере и нажми F12.
* Перейди во вкладку Network (Сеть) и включи фильтр Fetch/XHR.
* Обнови страницу.
* Найди системный запрос, совпадающий с названием раздела (например, pets?_rsc=... или petwear?_rsc=...).
* Скопируй набор символов после _rsc= (например, Q2bj4kji....) и вставь его в конфиг парсера.