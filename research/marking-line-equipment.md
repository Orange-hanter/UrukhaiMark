# Оборудование для линии контроля кодов маркировки — от единицы до паллеты + беспроводная телеметрия

> ⚠️ **Черновик `research/`, не канон.** MVP-пилот (Фаза 1 / Slice 1): **настольная этикетка**, термотрансфер 300 dpi — см. [equipment.md](../docs/explanation/technology/equipment.md). Inline TIJ/CIJ в §1 — сценарий **Slice 3+**; для аэрозолей 3307 канон не рекомендует CIJ без inline-верификатора.
>
> Исследование рынка (сентябрь 2026). Область: конвейерная линия UrukhaiMark, наносящая и проверяющая GS1 DataMatrix (в быту — «QR-код Честного знака»; технически это разные символики, но оборудование ниже в основном поддерживает обе). Три контрольные точки: **единица** (банка/бутылка на линии), **короб** (после упаковки), **паллета** (после паллетирования). Отдельные разделы: китайский рынок камер/верификаторов (раздел 6) как альтернатива западным брендам из разделов 1–2, и BLE/LoRa-оборудование китайского рынка для некритичной заводской телеметрии (разделы 4–5, 7).
>
> Источники указаны при каждой позиции. Цены — там, где их удалось найти (в основном производители 2D-считывателей/верификаторов цену не публикуют, только по запросу — это стандартная практика B2B).

---

## 1. Уровень единицы (банка/бутылка/пачка)

### 1.1 Нанесение кода на единицу

| Вендор | Модель | Функция | Ключевые характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Weber Marking Systems | Legi-Air 4050E | Print-and-apply (термотрансфер, сменный печатающий модуль) | скорость печати до 400 мм/с; 203/305/609 dpi; аппликация до 240 этикеток/мин; точность позиционирования ±0.8 мм | по запросу | [weber-marking.com](https://www.weber-marking.com/labelling/label-printers-and-dispensers/legi-air-4050-e.html) |
| Herma | 152C (wrap-around) | Print-and-apply, обёртывание цилиндрических изделий | до 200 изд/мин; диаметр тары 30–150 мм; опциональный термотрансферный модуль под переменный DataMatrix | по запросу | [herma.us](https://www.herma.us/machines/products/labeling-machines/wrap-around-labeler-152c/) |
| CTM Labeling Systems | 3600a-PA | Print-and-apply (движок Sato/Zebra) | tamp-blow аппликация, монтаж сверху/сбоку/снизу; 203–609 dpi | по запросу | [ctmlabelingsystems.com](https://ctmlabelingsystems.com/label-printer-applicators/) |
| Zebra | ZT411 | Печатающий модуль (используется внутри аппликаторов Weber/CTM/Novexx) | 203/300/600 dpi; 14 ips; ширина печати 104 мм; USB/Serial/Ethernet/BT | ~$1.5–2.5k (сам движок, ориентир) | [zebra.com](https://www.zebra.com/us/en/products/printers/industrial/zt400-series/zt411.html) |
| Novexx Solutions | XLP 51x / XLP 60x | Термотрансферные печатающие модули для print-apply | высокая рабочая нагрузка, используются в связке с аппликаторами | по запросу | [novexx.com](https://www.novexx.com/products/printers/) |
| Videojet | 7610 (fiber-лазер) | Прямая лазерная маркировка (без чернил/этикетки) | до 600 м/мин; алюминий, нерж. сталь, HDPE, PVC — подходит для алюминиевых баллонов | по запросу | [videojet.com](https://www.videojet.com/us/homepage/products/laser-marking-systems/videojet-7610.html) |
| Domino | D-Series (CO2-лазер) | Прямая лазерная маркировка | мощность 10/30/60 Вт; DataMatrix/QR; модульная сканирующая головка i-Tech; опция IP65 | по запросу | [codico-distributors.com PDF](https://www.codico-distributors.com/domino-brochures/lasers-co2/DominoD-Series.pdf) |
| Leibinger | JET3up (CIJ) | Струйная маркировка (continuous inkjet), прямо на упаковку | до 10 м/с (600 м/мин); высота печати 1.2–16 мм; DataMatrix + 1D/2D | по запросу | [directindustry.com](https://www.directindustry.com/prod/leibinger/product-15400-1909466.html) |
| Markem-Imaje | 9450 (CIJ) | Струйная маркировка | до 6.6 м/с; до 5 строк печати; G-головка 71 dpi / M-головка 115 dpi | по запросу | [markem-imaje.com](https://www.markem-imaje.com/productview/9450) |
| Videojet | 8520 (TIJ) | Термоструйная маркировка | 600 dpi; до 109 м/мин; **подтверждена продажа/сервис через СНГ-дистрибьютора** (Честный знак) | по запросу | [markjet.ru](https://markjet.ru/oborudovanie/chestnyy-znak/) |
| АРНИ (РФ-бренд) | H-PR-01…08 + VA-50 | Print-and-apply, локальная сборка (Россия) | скорость аппликации 15–40 м/мин | по запросу | [markjet.ru](https://markjet.ru/oborudovanie/chestnyy-znak/) |

Контекст: Videojet DataFlex 6330/6530 (термоперенос на плёнку/этикетку, 250–700 упак/мин) также встречается у того же СНГ-дистрибьютора, но это не прямая печать на жёсткую банку — TTO наносит код на гибкую этикетку/плёнку, которая затем клеится.

### 1.2 Верификация (проверка качества кода) на единице

| Вендор | Модель | Функция | Ключевые характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Cognex | DataMan 475V (Label) | Выделенный инлайн-верификатор | до 20 кодов/сек; соответствие ISO/IEC 15415 и 15416; есть DPM-вариант 475V-DPM для гравировки | по запросу | [cognex.com](https://www.cognex.com/products/barcode-readers/barcode-verifiers/dataman-475v-series/specifications) |
| Cognex | DataMan 8072 | Компактный стационарный верификатор | DataMatrix; поле обзора 27×20 мм; мин. элемент 6.0 mil; 1.2 МП; подсветка 30°/45°/90°; PoE/USB; IP65; ISO 15415 + TR-29158 (DPM) | по запросу | продаётся **Mallenom (РФ)** — [mallenom.ru](https://www.mallenom.ru/oborudovanie/mashinnoe-zrenie/dataman-8072-verifikatory-kodov/) |
| SICK | Lector65x | Инлайн-считыватель/верификатор | 40 Гц; сенсор 2/4 МП; декодирование 1D/2D/DPM в реальном времени; грейдинг по ISO 15415 | от **$1,888** (дистрибьютор, конфигурация) | [qviro.com](https://qviro.com/product/sick/lector64x-lector65x/quote) |
| Keyence | SR-2000 | Инлайн-считыватель со встроенным грейдингом | верификация по ISO 15415, ISO 15416, TR-29158 (AIM DPM), SAE AS9132, SEMI T10-0701 | новая — **~$8,040** (Radwell); б/у/серый рынок $1,150–$3,200 | [keyence.com](https://www.keyence.com/products/barcode/barcode-readers/sr-2000/specs/) |
| Omron Microscan | LVS-9510 | Настольный/QA верификатор (USB) | грейдинг линейных + 2D кодов (DataMatrix, QR, Aztec) + stacked; **не инлайн** — для выборочного контроля/калибровки | по запросу | [omron.eu](https://industrial.omron.eu/en/products/lvs-9510) |
| Omron Microscan | LVS-9580 | DPM-верификатор (компаньон LVS-9510) | для перманентной (лазерной) маркировки; тоже настольный, не инлайн | по запросу | [automation.omron.com](https://automation.omron.com/en/us/products/family/VF9580) |
| Cognex | In-Sight (2800/3800/8000) | Универсальная машинная зрительная платформа | считывание кода + сопутствующие проверки (уровень налива, наличие крышки, перекос этикетки); не выделенный ISO-15415 верификатор из коробки | по запросу | [cognex.com](https://www.cognex.com/en/products/2d-machine-vision-systems) |

**Важное разграничение:** Cognex DataMan 475V/8072, SICK Lector65x и Keyence SR-2000 — стационарные инлайн-устройства с дискретным I/O для ПЛК-управляемого отбраковщика. Omron/Microscan LVS-95xx — настольная QA-станция для выборочной калибровки, а не триггер отбраковки на линии.

> Китайские альтернативы (ридеры без ISO 15415-грейдинга + два исключения с грейдингом) — раздел 6.

### СНГ/Беларусь — доступность

- **Cognex**: **Data-by.by (Минск)** — прямой дистрибьютор машинного зрения/верификаторов Cognex ([data-by.by](https://www.data-by.by/about/cognex-machine-vision.html)); **Mallenom (РФ)** продаёт линейку DataMan.
- **Videojet, Markem-Imaje, Domino**: расходники и часть оборудования активно перепродаются в РФ (markjet.ru, getmark.ru, digitoria.ru, cleverence.ru) — вероятно, параллельный импорт; официальная гарантийная/прошивочная поддержка для региона не подтверждена.
- **SICK**: региональный дистрибьютор в СНГ в ходе поиска не подтверждён — только глобальные реселлеры.
- **Локальная альтернатива**: markjet.ru продаёт пакет «под ключ» для Честного знака с российским брендом печатающих аппликаторов АРНИ и лазерами под брендом Cyklop (вероятно, китайский OEM под локальным брендом) — ниже узнаваемость, но меньше риск санкционных ограничений и локальный сервис.

### Рекомендация (уровень единицы)

> **Расхождение с каноном MVP:** ниже «минимальный вариант TIJ/CIJ» — гипотеза для высокоскоростной inline-линии (Slice 3+). Для пилота cosmetics→РФ (Фаза 1) канон — [equipment.md](../docs/explanation/technology/equipment.md): настольный термотрансфер, не прямая CIJ на металл.

**Минимальный вариант (100–400 банок/мин):** один прямой принтер TIJ/CIJ (Videojet 8520 TIJ или Markem-Imaje 9450/Leibinger JET3up CIJ), печатающий DataMatrix прямо на банку, + один инлайн-верификатор (SICK Lector65x или Cognex DataMan 475V) на ПЛК линии, управляющий простым пневмоотбраковщиком. Прямая печать чернилами дешевле и быстрее при переналадке, чем print-apply или лазер.

**Полный вариант:** лазерная маркировка (Videojet 7610 fiber или Domino D-Series CO2) для перманентного, не смываемого кода + выделенный верификатор (Cognex 475V/8072 или Keyence SR-2000, последний удобен тем, что совмещает считывание и ISO-15415 грейдинг в одном устройстве) со 100%-контролем и логированием грейда для аудита Честного знака/УКЗ. Плюс настольный верификатор (Omron LVS-95xx) в ОТК для периодической калибровки инлайн-считывателя — отдельная, но стандартная закупка в программах ISO 15415.

---

## 2. Уровень короба (кейса)

### 2.1 Маркировка короба

| Вендор | Модель | Функция | Ключевые характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Videojet | 2380 series | Крупносимвольная струйная печать прямо на гофрокороб | 1 контроллер → до 4 печатающих голов, высота символа до 70 мм; переменные данные + штрихкод | по запросу | [videojet.com](https://www.videojet.com/us/homepage/general/news/videojet-launches-new-2380-series-large-character-inkjet-printer.html) |
| Logopak | 300 series | Print-and-apply этикетки короба (SSCC/GS1-128) | 80–100 этикеток/мин; термотрансфер/директ-термо; монтаж сбоку/сверху/спереди; ширина этикетки до 165 мм | по запросу | [logopak.co.uk](https://www.logopak.co.uk/print-and-apply-machines/case-labelling/300-case-labeller/) |
| CTM Labeling Systems | 3600a-PA (Swing Tamp / Dual Action / Corner Wrap) | Print-and-apply на короб | 203/305/406/609 dpi; ширина этикетки 0.5"–7.1"; до ~60 этикеток/мин | по запросу | [ctmlabelingsystems.com](https://ctmlabelingsystems.com/label-printer-applicators/) |
| Zebra | ZT610 / ZT620 (движок в составе Fox IV и др. аппликаторов) | Печатающий модуль для этикеток короба | ZT610: до 14 ips, 203/300/600 dpi, ширина печати 4.09"; ZT620: до 12 ips, до 300 dpi, ширина 6.6"; есть RFID-кодирующие варианты | ZT610 от **$5,333.72**; ZT620 от **$7,345.05** | [atlasrfidstore.com ZT610](https://www.atlasrfidstore.com/zebra-zt610-industrial-barcode-label-printer/), [ZT620](https://www.atlasrfidstore.com/zebra-zt620-industrial-rfid-barcode-label-printer/) |

Примечание: в контексте Честного знака код короба — это чаще «агрегированный код», а не классический GS1-128 SSCC, но категория оборудования та же — меняется только формат содержимого этикетки.

### 2.2 Верификация короба и агрегация

| Вендор | Модель | Функция | Ключевые характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Datalogic | AV900 | Стационарный тоннельный 2D-сканер короба на конвейере | сенсор 9 МП, до 32 fps, «PackTrack» защита от путаницы коробов, Gigabit Ethernet, IP65 | **$16,652** (одна SKU-конфигурация; полный тоннель — несколько модулей) | [barcodefactory.com](https://www.barcodefactory.com/datalogic/stationary-industrial-scanners/av900/938000112) |
| SICK | Lector65x (Dynamic Focus) | Считыватель для малых/средних тоннельных систем | динамический фокус; читает повреждённые/DPM коды; несколько модулей объединяются в сеть на одном кабеле | по запросу | [sick.com PDF](https://www.sick.com/media/docs/2/12/612/product_information_lector%C2%AE_serie_image_based_code_readers_en_im0051612.pdf) |
| Cognex | Modular Vision Tunnel (на базе DataMan 503) | Тоннель сканирования короба (1–6 сторон) | DataMan 503 до 140 Гц; чтение кода под углом до 85°; заявлено 99.9% успешных считываний; ПО Edge Intelligence Tunnel Manager | по запросу | [cognex.com](https://www.cognex.com/en-ca/products/modular-vision-tunnels) |
| Honeywell | HF811 / HF810 / HF800 | Стационарный 2D-сканер линии/конвейера, включая DPM | компактный стационарный форм-фактор | по запросу | [automation.honeywell.com](https://automation.honeywell.com/us/en/products/productivity-solutions/barcode-scanners/fixed-mount/hf811-fixed-mount-scanner) |
| Zebra | MP7000 | Стационарный биоптический сканер (пункты ручной проверки) | 2.3 МП, 45 fps, читает 1D/2D + Digimarc, широкая зона сканирования | по запросу | [zebra.com](https://www.zebra.com/us/en/products/spec-sheets/scanners/general-purpose-scanners/in-counter/mp7000.html) |

**Как реально работает агрегация (подтверждено GS1 и Честным знаком):** это операция в **ПО/базе данных**, а не оптическое пересканирование готового короба. Согласно GS1 EPCIS `AggregationEvent` (шаг «упаковка»): N дочерних кодов единиц привязываются к 1 родительскому коду короба. На линии это выглядит так: оператор/инлайн-сканер читает каждый DataMatrix единицы при укладке в короб → ПО (модуль маркировки, например «автоматическая потоковая агрегация» у интеграторов вроде RBS-GROUP) связывает их в БД → генерируется и печатается агрегированный код короба (раздел 2.1) → тоннельный сканер (раздел 2.2 выше) читает этот ОДИН код короба как проверку, что этикетка напечатана и читаема правильно — **не** для повторного вывода списка вложенных единиц (эта связь уже есть в БД). Источники: [markirovka.ru — ручная агрегация](https://markirovka.ru/knowledge/equipment/aggregation/ruchnaya-agregatsiya-markirovannogo-tovara), [rbs-id.ru — автоматическая агрегация](https://rbs-id.ru/tekhnicheskie-reshenija/katalog/reshenija/agregaciya/avtomaticheskaja-potokovaja-agregacija), [GS1 EPCIS/CBV](https://ref.gs1.org/guidelines/epcis-cbv/).

СНГ-доступность: Datalogic и Zebra сканеры продаются в Минске (planit.by, shtrih.by, yudway.by) и в РФ (datalogic-scanner.ru, rbsgr.ru, geksagon.ru). Для Cognex/SICK тоннельных решений региональное присутствие в этом поиске не подтверждено.

> Китайский аналог тоннеля (Wayzim, 6 сторон) и модульные ридеры HIKROBOT ID6000/ID7000 для сборки своего тоннеля — раздел 6.

---

## 3. Уровень паллеты

### ⚠️ Важный нюанс

**Оптическое пересканирование DataMatrix/QR на всех гранях уже собранной, обмотанной стрейч-плёнкой паллеты — это НЕ стандартная отраслевая практика.** Коды на внутренних коробах становятся физически недоступны после сборки. Ни один найденный производитель не продаёт продукт, заточенный именно под эту задачу. Ниже — что реально применяется вместо этого.

| Вендор | Модель | Функция | Ключевые характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Logopak | 850 pallet labeller | Print-and-apply 1–2 SSCC-этикеток на **уже собранную, обёрнутую** паллету | до 100 паллет/ч (2 этикетки); наносит на фронт+бок или бок+тыл по GS1; **встроенный сканер-валидатор** в аппликаторе перепроверяет только что нанесённую этикетку | по запросу | [logopak.co.uk](https://www.logopak.co.uk/machines/pallet-labelling/850-pallet-labeller/) |
| NOVEXX Solutions | XPU pallet labeler | Полностью автоматический print-and-apply на 1–2 смежные грани | до 180 паллет/ч (2 этикетки) | по запросу | [novexx.com](https://www.novexx.com/products/printapply/xpu/) |
| NOVEXX Solutions | XPA 9xx + Rotor-Long | Интегрированная система паллетной маркировки для остановленной паллеты | скорость аппликации до 400 мм/с; до 2 GS1-этикеток A5; ширина этикетки 10–233 мм | по запросу | [novexx.com](https://www.novexx.com/products/printapply/xpa-palletlabeling/) |
| SATO | CL6NX (Plus) | Печатающий модуль для станций паллетной маркировки | головка 6.5", 203/305 dpi, до 10 ips, термотрансфер/директ-термо, USB/Ethernet/Wi-Fi | по запросу | [satoamerica.com](https://www.satoamerica.com/resources/videos/print-and-apply-multi--panel-label) |
| Zebra | FX9600 | Стационарный UHF RFID-считыватель — **RFID-подход** к идентификации паллеты/короба без прямой видимости, работает сквозь плёнку и стопки коробов | до 8 RF-портов, PoE, IP53, высокая чувствительность для плотно уложенного товара | по запросу | [zebra.com](https://www.zebra.com/us/en/products/spec-sheets/rfid/rfid-readers/fx9600.html) |
| Impinj | R700 / R720, xSpan gateway | Портальное/дверное RFID-считывание паллет | R720: 4-портовый ридер для порталов/ворот; xSpan — «гейтвей»-форм-фактор для настенного монтажа портала, определяет направление движения | по запросу | [impinj.com R700](https://www.impinj.com/products/readers/impinj-r700), [xSpan](https://www.atlasrfidstore.com/impinj-xspan-gateway-rfid-reader/) |
| Avery Dennison (Smartrac) | AD-160u7 и аналоги | Пассивная UHF RFID-метка на короб/паллету — то, что реально «читают» ридеры выше | 860–960 МГц, дальность чтения до ~14.5 м, 64×6 мм | **~$0.05–0.25/метка** (оценка по объёму, не прайс вендора) | [dipolerfid.com](https://www.dipolerfid.com/en/product/rfid-tag-averydennison-ad-160u7) |
| Zebra | ZT610-RFID / ZT620-RFID | Печать + кодирование RFID-инлея за один проход (этикетка короба/паллеты) | те же механические характеристики, что в разделе 2.1, + опция RFID-кодирования | от **$5,333.72** / **$7,345.05** | [atlasrfidstore.com](https://www.atlasrfidstore.com/zebra-zt620-industrial-rfid-barcode-label-printer/) |
| AbeTech | GateKeeper Pallet Scanning | Стационарный портал сканирования/зрения у паллетообмотчика — финальная проверка перед отгрузкой | сверхширокое поле зрения, читает UPC/Code128/QR/DataMatrix; заявлено до 99.9% чтения повреждённых этикеток; интеграция с WMS/ERP/MES/RFID | по запросу | [abetech.com](https://www.abetech.com/solutions/gatekeeper/pallet-scanning) |
| Accella AI | Dock Check (платформа Accella MFG Bot) | Камерная проверка **полноты паллеты**: подсчёт видимых коробов, чтение видимых этикеток, флаг недостачи/лишнего/не того SKU | 2× камеры LUCID Triton 24.5 МП (перед/зад паллеты), ~6–8 сек/паллета, интеграция с ПЛК/WMS/ERP, локальный inference | по запросу | [thinklucid.com](https://thinklucid.com/case-studies/ai-vision-system-verifies-palletized-shipments/) |

**Паттерн, а не отдельный продукт:** интеграторы паллетирующих ячеек (напр. связка Photoneo/Jacobi Robotics) сканируют/3D-верифицируют **каждый короб в момент укладки роботом** — до обмотки, теми же тоннельными/портальными сканерами из раздела 2.2, результат сразу пишется в WMS. Именно так на практике честно получают утверждение «паллета проверена». Источник: [photoneo.com](https://www.photoneo.com/jacobi-robotics-partnership-mixed-case-palletizing/).

### Рекомендации (уровень паллеты)

1. **Агрегация — в софте, не пересканированием.** Связь единица→короб формируется в момент упаковки (раздел 2.2), хранится в БД, передаётся в Честный знак как событие агрегации — не восстанавливается повторным чтением.
2. **Проверять состав паллеты на этапе сборки, до обмотки** — сканированием каждого короба роботом-паллетоукладчиком или тоннельным/портальным сканером на конвейере перед паллетайзером, пока все коды ещё физически доступны.
3. **Один паллетный SSCC/агрегированный ярлык печатать после сборки и обмотки** (Logopak 850, NOVEXX XPU/XPA) — это фактическая, почти повсеместная практика; многие такие аппликаторы сами перепроверяют собственную нанесённую этикетку встроенным сканером.
4. **RFID — только при реальной бизнес-потребности** (напр. требование российского логистического партнёра, или инвентаризация склада без распаковки паллет). Это единственная технология, читающая содержимое сквозь плёнку без прямой видимости, но добавляет стоимость метки на единицу и не является требованием Честного знака — держать как опциональное расширение, не часть MVP.
5. **Камерная проверка полноты паллеты** (по образцу Accella Dock Check / AbeTech GateKeeper) — разумное дополнение для финальной проверки перед отгрузкой (счёт коробов, читаемость видимых этикеток), но нужно честно позиционировать как *проверку количества/качества*, а не как повторную верификацию всей цепочки прослеживаемости — камера видит только внешние этикетки.

---

## 4. Беспроводная передача данных: BLE (китайский рынок)

Некритичная заводская телеметрия (статус оборудования, датчики среды, метки операторов/тары) как лёгкая надстройка над проводной ПЛК/fieldbus-сетью — не замена ей.

### 4.1 BLE-шлюзы (gateways)

| Производитель | Модель | Категория | Характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Minew (Shenzhen Minew Technologies) | G1 | Индор-шлюз BLE→WiFi/Ethernet | BLE 5.0, дальность до 300 м на открытом пространстве, ~400 BLE-пакетов/с, MQTT/HTTPS+TLS, PoE 802.3af/at или DC 5В/1А | ~$65/шт (пробная партия, Alibaba) | [alibaba.com](https://www.alibaba.com/product-detail/Minew-G1-Indoor-Location-Ble-Wifi_60767516588.html) |
| Minew | MG5 | Уличный мобильный шлюз | LTE-M/NB-IoT + BLE 5.0 + GPS, цифровой вход детекции зажигания (8–48В), буфер ~50k записей, защищённый уличный корпус | по запросу | [minew.com](https://www.minew.com/product/mg5-outdoor-mobile-lte-gateway/) |
| MOKOSmart (Shenzhen) | MKGW1-BW Pro | Индор-шлюз BLE→WiFi/Ethernet | BLE 5.0 (Coded PHY + 2M PHY), >150 м, до 319 пакетов/с, 8 одновременных BLE-соединений, MQTT/HTTP/TCP/UDP | по запросу | [mokosmart.com PDF](https://docs.mokosmart.com/wp-content/uploads/2025/06/MKGW1-BW-Pro-Bluetooth-Gateway-Specification-V1.1.pdf) |
| MOKOSmart | MK107 | Шлюз-розетка (форм-фактор вилки) | мост BLE→WiFi, plug-and-play, сквозная розетка, варианты вилки US/UK/EU/FR | по запросу | [mokosmart.com](https://www.mokosmart.com/moko-ble-to-wifi-gateway-data-relay-between-beacons-and-your-cloud-server-mk107/) |
| KKM / Kbeacon (Shenzhen KKM, с 2008 г.) | KG02 | Индор-шлюз BLE→WiFi/Ethernet | BLE 5.0, чипсет серии nRF52, заявлено >300 м, PoE или DC 5В, HTTP/HTTPS/MQTT | уточнять в листинге | [alibaba.com](https://www.alibaba.com/product-detail/KKM-KG02-bluetooth-gateway-ble-devices_1600534984938.html) |
| KKM / Kbeacon | KG01 | Уличный шлюз | IP54, BLE 5.0 + 4G/GPS backhaul | уточнять | [bestsuppliers.com](https://www.bestsuppliers.com/products/zfzlywpzt1ri/kkm-kg01-outdoor-waterproof-ip54-iot-receiver-device-bluetooth-beacon-gateway-ble-50-gateway) |
| Dragino (Shenzhen) | BH01-LB/LS | Хаб BLE→**LoRaWAN** (не прямой WiFi/Ethernet) | сканирует окружающие BLE-датчики темп./влажности и ретранслирует по LoRaWAN; батарея 8500 мАч Li/SOCl2 или solar+Li-ion; уличное исполнение | не подтверждена (~$45–65 ориентировочно) | [dragino.com](https://www.dragino.com/products/lora-lorawan-end-node/item/359-bh01-lb-ls-ble-to-lorawan-hub.html) |

### 4.2 BLE-датчики / маячки

| Производитель | Модель | Категория | Характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Minew | S1 | Датчик темп./влажности | BLE 5.0, nRF52832, сенсор SHT31 (±0.5°C, ±0.25%RH), IP66, батарея AAA 3–5 лет, буфер 200 записей | $12–25/шт (опт от $12 при 5000+) | [alibaba.com](https://www.alibaba.com/product-detail/Minew-S1-smart-Wireless-bluetooth-Temperature_60581548588.html) |
| Minew | C10 | Маячок-бейдж (персонал) | BLE 5.0, карточный форм-фактор, вещание 100 м, iBeacon/Eddystone, батарея-таблетка — используется с G1 для позиционирования/учёта присутствия | по запросу | [minew.com](https://www.minew.com/product/c10-card-beacon/) |
| MOKOSmart | M2 | Маячок для отслеживания активов | BLE 5.1, IP67, 160 м, сменная батарея CR2477, до 4 лет автономности, опционально датчик Холла + акселерометр | **$3.00/шт при MOQ 100** | [mokosmart.com](https://www.mokosmart.com/asset-tracking-beacon-m2/) |
| MOKOSmart | H4 Pro | Датчик темп./влажности (для холодовой цепи) | BLE 5.0, nRF52-серия, точность ±0.3°C, IP66 | по запросу | [mokosmart.com](https://www.mokosmart.com/mokosmart-h4-p5202dh2-beacon-ip66-waterproof-with-external-sensor/) |
| MOKOSmart | L02S | Мультидатчик (темп./влажность + геркон + акселерометр) | BLE 5.0, IP67, несколько типов телеметрии в одном устройстве | по запросу | [store.mokosmart.com](https://store.mokosmart.com/product/l02s-multiple-sensor/) |
| KKM / Kbeacon | K6 | Датчик-логгер темп./влажности | BLE, чипсет серии nRF52 | уточнять | [alibaba.com](https://www.alibaba.com/product-detail/KKM-K6-BLE-Beacon-temperature-and_1600201952342.html) |
| WitMotion (Shenzhen) | WTVB01-BT50 | Датчик вибрации (3 оси: смещение/скорость/частота/угол) | BLE 5.0, на базе MPU6050, дальность 50 м, до 4 одновременных соединений, зарядка Type-C, автономность ~8 ч | ~$35–45/шт (розница) | [witmotion-sensor.com](https://witmotion-sensor.com/products/wtvb01-bt50-bluetooth-50m-wireless-multi-connected-vibration-sensor) |

⚠️ WTVB01-BT50: автономность ~8 ч — больше подходит для периодических вибро-обходов, чем для постоянного мониторинга.

### 4.3 BLE радиомодули (для встраивания)

| Производитель | Модель | Категория | Характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Chengdu Ebyte Electronic Technology | E104-BT5032A | Модуль на чипе nRF52832 | BLE 4.0/4.2/5.0, UART, 2.4 ГГц, керамическая антенна, ~60 м, +4 дБм | $3.78–4.69/шт (по объёму) | [alibaba.com](https://www.alibaba.com/product-detail/Ebyte-E104-BT5032A-nRF52832-module-blue_1600999732090.html) |
| Shenzhen RF-star Technology | RF-BM-ND04 | Модуль на чипе nRF52832 | BLE 5.0, Cortex-M4, UART/SPI, антенна PCB (есть IPEX-вариант ND04I), поддержка Bluetooth Mesh, 20–100 м, +4 дБм | от $3.77/шт | [rfstariot.com](https://www.rfstariot.com/bluetooth-5-0-low-energy-bluetooth-mesh-low-energy-nrf52832-module-rf-bm-nd04_p19.html) |
| Espressif Systems (Шанхай) | ESP32-C3-WROOM-02(U)-N4 | Модуль-SoC (RISC-V) | WiFi 4 + BLE 5, 4 МБ флэш, вариант с PCB- или U.FL-антенной — удобен для узлов, где нужен и WiFi, и BLE | ~$2.2–3.5/шт (розница LCSC/DigiKey) | [lcsc.com](https://www.lcsc.com/product-detail/C2934560.html) |
| Fanstel Corporation (Тайбэй — **не материковый Китай**) | BT832F | Модуль на чипе nRF52832 | BLE 5.x, 512 КБ флэш/64 КБ RAM, PCB-антенна, заявлено до 760 м, есть CMIIT-сертифицированный вариант для рынка КНР | от $7.40/шт | [fanstel.com](https://www.fanstel.com/bt832-1-1) |
| Shenzhen Bluetrum Technology (深圳市中科蓝讯) | AB5301A / плата AB32VG1 | Чип/модуль | RISC-V MCU со встроенным Bluetooth 6.0/BLE, 8 МБ флэш, ориентирован на аудио (TWS-наушники/колонки), LQFP48 | чип ~$1–2/шт; плата ~$10–15 | [cnx-software.com](https://www.cnx-software.com/2021/03/09/bluetrum-ab32vg1-board-features-ab5301a-bluetooth-risc-v-mcu-runs-rt-thread-rtos/) |

⚠️ Bluetrum AB5301A — аудио-SoC, а не выделенный сенсорный модуль; годится для базовой BLE+GPIO-телеметрии, но без экосистемы AT-команд/сенсорных SDK, как у Ebyte/RF-star/Espressif.

---

## 5. Беспроводная передача данных: LoRa/LoRaWAN (китайский рынок)

Подходит там, где BLE не хватает дальности — большая площадь цеха/склада, редкие показания раз в несколько минут.

### 5.1 LoRaWAN-шлюзы

| Производитель | Модель | Категория | Характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Dragino (Shenzhen) | LPS8N | Индор-шлюз | EU868/US915, SX1301+2×SX1257 (8 каналов), WiFi/Ethernet + опция 3G/4G, встроенный LoRaWAN/IoT-сервер | ~$245/шт (розница AliExpress) | [aliexpress.com](https://www.aliexpress.com/item/1005004133174496.html) |
| Dragino | DLOS8N | Уличный шлюз | EU868/US915, SX1301+SX1257, IP65, Ethernet/WiFi + опция встроенного 4G LTE, PoE или 12В DC, заявлено до 20 км LOS | $310–330/шт при 100–300+ шт (вариант с 4G — $330–420) | [alibaba.com](https://www.alibaba.com/product-detail/Dragino-EU868-US915Mhz-DLOS8N-4G-Outdoor_1601341214310.html) |
| Milesight (Xiamen) | UG65 | Полу-промышленный индор/лёгкий уличный шлюз | 8 каналов, Semtech SX1302, SKU EU868 (UG65-868M-EA), 2000+ узлов, Ethernet/WiFi/PoE, опция сотовой связи, ~15 км LOS / ~2 км в городе | ~$454/шт (розница) | [milesight.com](https://www.milesight.com/iot/product/lorawan-gateway/ug65) |
| Milesight | UG67 | Промышленный уличный шлюз | IP67, 8 каналов SX1302, 2000+ узлов, Ethernet/WiFi/4G, доступен SKU EU868 | не подтверждена | [milesight.com](https://www.milesight.com/iot/product/lorawan-gateway/ug67) |
| RAKwireless (Shenzhen) | RAK7268 (WisGate Edge Lite 2) | Индор-шлюз | 8 каналов SX1302, Ethernet + WiFi-AP для настройки, поддержка PoE, региональные SKU вкл. EU868, компактный корпус | ~$139/шт (AliExpress) | [aliexpress.com](https://www.aliexpress.com/item/1005002622143019.html) |
| RAKwireless | RAK7249 (WisGate Edge Pro / Macro Outdoor) | Промышленный уличный шлюз | корпус IP67/NEMA-6 с кабельными вводами, двойной концентратор, до 16 каналов, Ethernet/WiFi/LTE, Class A/C | $499–940/шт (зависит от продавца/комплекта) | [lora-alliance.org](https://lora-alliance.org/marketplace/rakwireless-technology-co/rak7249-macro-outdoor-gateway/) |
| Seeed Studio (Shenzhen) | SenseCAP M2 | Индор-шлюз | концентратор SX1302, SKU EU868/US915/AU915/AS923, подключение к нескольким network-серверам, HW+FW открыты (2025) | не подтверждена | [seeedstudio.com](https://www.seeedstudio.com/SenseCAP-Multi-Platform-LoRaWAN-Indoor-Gateway-SX1302-EU868-p-5471.html) |

### 5.2 LoRa конечные узлы (датчики)

| Производитель | Модель | Категория | Характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Dragino | LHT65N (напр. -E31F) | Узел темп./влажности | встроенный SHT20 + порт для внешнего зонда (напр. DS18B20), LoRaWAN 1.0.4, SKU EU868/US915/AU915, батарея 2400 мАч (заявлено >10 лет), буфер 3200 записей | $35–42/шт (тиры 5–500+, Alibaba) | [alibaba.com](https://www.alibaba.com/product-detail/Dragino-LHT65N-E31F-LoRawan-Temperature-Humidity_1600834992690.html) |
| Dragino | LDS02 | Датчик двери/контакта | статус открыт/закрыт, лог времени/числа открытий, тревога при долгом открытии, 2×AAA (~16,000–70,000 посылок), LoRaWAN | не подтверждена | [dragino.com](https://www.dragino.com/products/lorawan-nb-iot-door-sensor-water-leak/item/181-lds02.html) |
| Dragino | LWL01 | Датчик протечки воды | контактный зонд, батарея CR2032, ~12,000 посылок / до 2 лет | не подтверждена | [dragino.com](https://www.dragino.com/products/lorawan-nb-iot-door-sensor-water-leak/item/158-lwl01.html) |
| Dragino | LT-22222-L | Универсальный узел ввода/вывода→LoRaWAN | 2× дискретный вход, 2× дискретный выход (NPN), 2× релейный выход, 4× аналог. вход (2×0–20мА + 2×0–30В), Class A/C, питание от сети 7–24В (не батарея) — мост для существующих ПЛК/сухих контактов на LoRaWAN | не подтверждена | [dragino.com](https://www.dragino.com/products/lora-lorawan-end-node/item/156-lt-22222-l.html) |
| Dragino | SN50v3-LB / -LS | Универсальный влагозащищённый узел | IP68, кабельный ввод M16, на базе SX1262, поддержка внешних зондов разных типов, батарея 4000/8500 мАч Li-SOCl2 (LB) или 3000 мАч Li-ion+солнечная (LS) | не подтверждена | [dragino.com](https://www.dragino.com/products/lora-lorawan-end-node/item/260-sn50v3-lb-ls.html) |
| Milesight (Xiamen) | EM300-TH | Узел темп./влажности | сенсор Sensirion, ±0.3°C/±3%RH, −30…70°C, IP67, SKU EU868 (EM300-TH-868M), настройка по NFC, сменная батарея 4000 мАч (~5 лет, опция 8000 мАч до 10 лет) | от ~$89/шт (розница) | [tme.com](https://www.tme.com/us/en-us/details/em300-th/rf-modules/xiamen-milesight-iot-co-ltd/) |
| Anhui Doton Link Technology | WS11M-L | Узел вибрации + температуры (мониторинг состояния оборудования) | трёхосевой акселерометр ±16g, отклик 5Гц–3.6кГц, −40…120°C, IP68, корпус нерж. сталь 304, крепление M6, настройка по BLE 5.0 + передача по LoRaWAN; диапазон по умолчанию 470–510МГц (Китай), заявлена «настраиваемость» — **перед заказом уточнять реальный 868МГц-вариант**; автономность ~3 года | $200–400/шт, MOQ 1 | [made-in-china.com](https://dotonlink.en.made-in-china.com/product/tUcrRoYKIJkp/China-WS11M-L-Smart-Lorawan-Wireless-Vibration-Temperature-Sensor-for-Machinery-Health-Monitoring-Lorawan-Wireless-Vibration-Accelerometer-Sensor.html) |

### 5.3 LoRa радиомодули/чипы (для встраивания)

| Производитель | Модель | Категория | Характеристики | Цена | Источник |
|---|---|---|---|---|---|
| Ebyte (Chengdu, пров. Сычуань) | E22-900T30S(-V2) | Модуль UART | SX1262, 850–930МГц (868/915 настраиваемо), 30дБм (1Вт), UART, заявлено до 10 км LOS, SMD 25×40.5мм, CE/FCC | $9.56–10.43/шт (тиры 2–999) | [alibaba.com](https://www.alibaba.com/product-detail/Ebyte-E22-900T30S-wireless-serial-port_62504566322.html) |
| Ebyte | E22-900M30S | Модуль SPI | SX1262, 868МГц, 30дБм, заявлено ~12 км, SPI, разъём антенны IPEX, низкий ток сна | не подтверждена | [ebyteiot.com](https://ebyteiot.com/products/sx1262-lora-module-e22-900m30s-868mhz-wireless-module-30dbm-12km-range-ipex-antenna-spi-interface-low-power-consumption-ebyte) |
| Heltec Automation (Shenzhen) | HT-RA62 | Голый LoRa-модуль | SX1262, выбор 433/868/915МГц, компактный SMD-корпус для встраивания в свою плату | $3.90/шт, MOQ 1 | [alibaba.com](https://www.alibaba.com/product-detail/Heltec-SX1262-LoRa-Series-Module-HT_1600671300543.html) |
| Heltec Automation | HT-CT62 | Комбо-модуль LoRa+MCU | ESP32-C3 + SX1262, 433/868/915МГц, MCU на модуле для автономной прошивки узла | $6.90/шт, MOQ 1 | [alibaba.com](https://m.alibaba.com/product/1600673882659/Heltec-ESP32C3-SX1262-LoRa-Module-HT.html) |
| Heltec Automation | WiFi LoRa 32 (V3) | Отладочная плата (ESP32-S3+SX1262) | 863–928МГц (покрывает EU868), встроенный OLED, WiFi+BLE+LoRa, Arduino-совместимая — частая база для прототипов узлов/шлюзов | ~$15–20/шт (ориентир) | [alibaba.com](https://www.alibaba.com/product-detail/Heltec-WiFi-LoRa-32-V3-0_62360259165.html) |
| NiceRF / Shenzhen NiceRF Wireless Technology | LoRa1262 (G-NiceRF) | Модуль SPI | SX1262, 868/915МГц, 22дБм (160мВт), TCXO 1.5ppm, SPI, сертификация CE-RED и FCC ID; есть более мощная версия LoRa1262F30 (1.5Вт, ~7км) | $5.69–6.94/шт (тиры 2–100+) | [alibaba.com](https://www.alibaba.com/product-detail/G-NiceRF-LoRa1262-CE-RED-FCC-60824103708.html) |

---

## 6. Машинное зрение и верификаторы — китайский рынок

Дополнение к разделам 1.2 и 2.2: китайские альтернативы западным брендам (Cognex/SICK/Keyence/Datalogic) для чтения и проверки кода.

**Главный вывод по ISO/IEC 15415:** массовые китайские бренды (HIKROBOT, Dahua/Huaray, Newland, Rakinda, OPT) — это **ридеры** (read/no-read, декодирование), а не **верификаторы** — они не выдают формальный грейд A–F, как Cognex DataMan/SICK Lector65x/Keyence SR-2000. Найдено два реальных исключения (HEROJE BV9600, iDPRT iV5820/iV8600) — оба явно заявляют ISO/IEC 15415 и 15416.

### 6.1 Инлайн-ридеры/верификаторы для единицы

| Вендор | Модель | Функция | Ключевые характеристики | Цена | Источник |
|---|---|---|---|---|---|
| HIKROBOT (машинное зрение Hikvision) | ID3000 (напр. MV-ID3050PM) | Инлайн-ридер, без ISO 15415 | 4.2 МП, до 60 кодов/сек, deep-learning декодирование, DPM-режим, M12 I/O | ~$500/шт при 100+ шт | [alibaba.com](https://www.alibaba.com/product-detail/HIKROBOT-MV-ID3050PM-08M-12M-16M_1600740927075.html) |
| Dahua / Zhejiang Huaray Technology | R72 series | Ридер (декодирование, DPM) | 20 МП, 15 fps, GigE, IP67, декодирует QR/DM/DPM + 1D | по запросу | [huaraytech.com](http://en.huaraytech.com/) |
| Newland AIDC | FM600 | Ридер, AI fixed-mount | 2.3 МП, 60 fps, IP65, Ethernet/RS232/USB, OCR | по запросу | [newlandaidc.com](https://www.newlandaidc.com/roa/products/OEM-Fixed-Mount/FM600.html) |
| Rakinda (Shenzhen) | RK4000 | Бюджетный ридер-модуль | ~1 МП, IP65, RS232/USB/Ethernet, Good/NG выход на ПЛК-отбраковщик | **$280–290/шт** | [alibaba.com](https://www.alibaba.com/product-detail/Rakinda-RK4000-2D-Barcode-IP65-Industrial_1600676539724.html) |
| HEROJE (Shenzhen) | BV9600 | **Настольный верификатор** (аналог Omron LVS-9510) | 8.5 МП, явный **ISO/IEC 15415, 15416, 15426-1/2 + китайские GB/T23704, GB/T14258** | по запросу | [heroje.com](https://www.heroje.com/product/122-en.html) |
| iDPRT (Xiamen) | iV5820 / iV8600 | **Инлайн-верификация**, встроена в принтер | явный **ISO/IEC 15415 + 15416 в реальном времени на скорости печати**, CIS-камера до 1200 dpi, до 14 ips | по запросу | [idprt.com](https://www.idprt.com/Featured-Articles/idprt-iv-barcode-inspection-printer.html) |

⚠️ Ни HIKROBOT/Dahua/Newland/Rakinda/OPT не заменяют напрямую DataMan/Lector65x/SR-2000 — они управляют отбраковкой по факту чтения, не по качеству печати. HEROJE BV9600 закрывает роль настольного QA (как LVS-9510). iDPRT — единственный найденный китайский продукт с реальным инлайн ISO-грейдингом, но только внутри собственного принтера, не как отдельный верификатор для чужой линии.

### 6.2 Тоннельные/портальные сканеры короба

| Вендор | Модель | Функция | Ключевые характеристики | Цена | Источник |
|---|---|---|---|---|---|
| HIKROBOT | ID6000 (напр. MV-ID6200M) | Логистический ридер — блок для сборки тоннеля | 20 МП, до 60 кодов/сек, GigE, IP67, декодирование под повреждённые/грязные этикетки | по запросу | [innosmart.bg](https://www.innosmart.bg/product/mv-id6200m-00c-nng/) |
| HIKROBOT | ID7000 (напр. MV-ID7080EM) | Высокоскоростной line-scan ридер — сортировка/тоннель | 8K line-scan, до 15 кГц, скорость конвейера **до 2.5 м/с** | по запросу | [innosmart.bg](https://www.innosmart.bg/product/mv-id7080em-35f-wha/) |
| Wayzim Technology (Wuxi) | 6-Sided Scanning Tunnel | **Готовый тоннель** — прямой аналог Datalogic AV900 / Cognex Vision Tunnel | 20 МП area-scan + 8K line-scan камеры на все 6 сторон короба, «no blind zone» | по запросу | [wayzim.com](https://www.wayzim.com/en/product/detail/1004) |

HIKROBOT не продаёт единую SKU «тоннель» (как Datalogic/Cognex) — 6-стороннее чтение собирается из нескольких модулей ID6000/ID7000 + ПО CodePlatform, тот же паттерн, что у тоннеля на SICK Lector65x из раздела 2.2. Wayzim — единственный найденный вендор с готовым тоннелем как отдельным продуктом.

### 6.3 Паллетное зрение

**Честный результат: прямого китайского аналога Accella AI Dock Check / AbeTech GateKeeper не найдено.** Ни один из проверенных брендов (HIKROBOT, Dahua/Huaray, OPT, Newland, SUNLUX, Rakinda, Wayzim, HEROJE, iDPRT) не продаёт готовую камерную систему проверки полноты собранной паллеты — это подтверждает вывод раздела 3: категория нишевая и слабо стандартизирована даже у западных вендоров.

Единственный релевантный паттерн: **Mech-Mind Robotics** (Пекин) — 3D-камеры Mech-Eye + ПО Mech-Vision для робота-паллетоукладчика, верифицирующие каждый короб **в момент укладки** (тот же принцип «проверка до обмотки», что у Photoneo/Jacobi Robotics из раздела 3). [mech-mind.com](https://www.mech-mind.com/solution/depalletizing-and-palletizing.html)

### СНГ-доступность (китайские камеры)

- **HIKROBOT** — лучший вариант по логистике: несколько подтверждённых официальных дистрибьюторов в РФ (Sensotek, CameraIQ, CameraLab, Azimut Photonics), и что важно — **Mallenom Systems** ([hikrobot.mallenom.ru](https://hikrobot.mallenom.ru/)) — тот же дистрибьютор, что уже продаёт Cognex DataMan (раздел 1.2). Один канал закупки потенциально закрывает и западный верификатор, и китайский ридер. Отдельного дистрибьютора в Беларуси не подтверждено, но у sister-бренда Hikvision (видеонаблюдение) есть развитая дистрибуция в Минске.
- **Newland, SUNLUX, Rakinda** — есть российские AIDC-дистрибьюторы, но их фокус — ручные/розничные сканеры; промышленные fixed-mount линии (RK4000, FM600) в наличии не подтверждены (у Rakinda позиция значится «под заказ»).
- **Dahua/Huaray, OPT, HEROJE, iDPRT, Wayzim** — дистрибьютор в СНГ не найден; закупка напрямую через Alibaba/фабрику, документация и поддержка на китайском.

### Компромисс: китайские камеры vs западные бренды

**Цена** — разрыв в разы там, где нашлись цифры: Rakinda RK4000 ~$280–290 против SICK Lector65x от $1,888 или Keyence SR-2000 ~$8,040 (не совсем прямое сравнение — западные модели включают ISO-грейдинг, которого нет у бюджетных китайских ридеров).

**Разрыв — не в оптике, а в ISO 15415.** По железу (разрешение, fps, устойчивость декодирования) HIKROBOT ID6000/ID7000 — реальный конкурент Datalogic AV900-класса для тоннеля/короба. Но именно инлайн-конвейерного ПЛК-интегрированного ISO-15415-грейдера уровня DataMan 475V/Lector65x/SR-2000 у китайских вендоров пока нет — HEROJE BV9600 закрывает только настольную QA-роль, iDPRT грейдит инлайн, но только внутри своего принтера.

**Практическая архитектура:** гибрид, а не полная замена. Китайское железо (HIKROBOT, Rakinda, Wayzim) — обоснованный дешёвый выбор для **чтения на уровне короба/тоннеля** (раздел 2, категория "успешно считано или нет"), тем более что у HIKROBOT уже есть РФ-дистрибуция через тот же канал, что и Cognex. Для **верификации единицы с защитимым ISO-15415 грейдом для аудита Честного знака/УКЗ** безопаснее остаться на западном инлайн-верификаторе (Cognex/SICK/Keyence) или добавить HEROJE BV9600 в ОТК на роль, аналогичную LVS-9510. Риск поддержки для остальных китайских вендоров (кроме HIKROBOT) реален: нет подтверждённого дистрибьютора в СНГ, документация и прошивки — на китайском.

---

## 7. BLE vs LoRa — когда что выбирать

**BLE** выигрывает там, где нужна высокая скорость данных, низкая задержка или плотное сосуществование на коротких дистанциях — метки активов рядом со считывателем, сопряжение HMI-с-устройством, посекундная передача статуса в пределах одного помещения (обычно 30–100 м на линк).

**LoRa/LoRaWAN** выигрывает там, где ограничение — это **расстояние и проникновение через стены при очень малом объёме данных**: периодическое скалярное показание, смена состояния двери, пороговая тревога — по всей площадке, слишком большой или заставленной для BLE-mesh с множеством повторителей. Один шлюз LoRa может заменить то, что иначе потребовало бы BLE-mesh с множеством хопов, ценой намного меньшей пропускной способности (байты за сообщение, задержка секунды-минуты) и регуляторных ограничений duty-cycle (1% на суб-полосах EU868), что делает LoRa непригодным для чего-либо похожего на управление в реальном времени.

**Минимальный BLE-слой** для небольшой линии: 1–2 индор-шлюза (Minew G1 / MOKOSmart MKGW1-BW Pro / KKM KG02) поднимают MQTT-мост в общий брокер; точечные датчики (Minew S1 / MOKOSmart H4 на температуру/влажность в шкафах управления и на складе); WitMotion WTVB01-BT50 как переносной инструмент для периодических вибро-обходов; MOKOSmart M2/L02S как generic-метка на тележки/тару; Minew C10 — бейдж оператора. Для DIY-узлов на сухом контакте/GPIO от ПЛК — радиомодуль Ebyte E104-BT5032A или RF-star RF-BM-ND04 (оба на Nordic nRF52832, $3.7–4.7/шт).

**Минимальный LoRa-слой**: 1 шлюз (Dragino DLOS8N или Milesight UG65/UG67) на крышу/антресоль обычно покрывает весь цех/склад или несколько корпусов; десятки-сотни батарейных узлов (Dragino LHT65N, LDS02, Milesight EM300-TH), отчитывающихся раз в несколько минут и живущих на одной батарее годами. Dragino LT-22222-L особенно полезен как мост для оборудования, уже имеющего сухие контакты/4-20мА/релейные сигналы из шкафов ПЛК — позволяет вывести эти сигналы на LoRaWAN, не трогая сам fieldbus.

---

## 8. Итоговые рекомендации

| Слой | Минимальный вариант (CAPEX ориентир) | Полный вариант |
|---|---|---|
| Единица (банка) | 1× TIJ/CIJ принтер + 1× инлайн-верификатор + пневмоотбраковщик | + лазерная маркировка, настольный верификатор ОТК |
| Короб | 1× print-and-apply на короб + 1× тоннельный сканер | + полное 6-стороннее тоннельное сканирование, ПО агрегации |
| Паллета | 1× паллетный print-and-apply (после обмотки) | + RFID-считыватели/метки, камерная проверка полноты паллеты |
| BLE | 1–2 шлюза + 3–5 точечных датчиков | сеть датчиков по цеху + бейджи операторов |
| LoRa | 1 шлюз + 5–10 узлов | покрытие всей площадки, мост с ПЛК-сигналами через LT-22222-L-подобные узлы |

**Ключевой message для стейкхолдеров:** оптическое пересканирование кодов на паллете — не реальная практика; агрегация — это база данных, а не повторное сканирование; BLE и LoRa — некритичная телеметрия поверх/рядом с проводной сетью ПЛК, а не замена ей; китайские камеры (раздел 6) — обоснованная замена западным на уровне короба/чтения, но не на уровне сертифицируемого ISO 15415-грейда единицы.

---

## 9. Источники

Все ссылки инлайн в таблицах выше — сайты производителей, спецификации, каталоги дистрибьюторов (включая Alibaba/Made-in-China листинги для разделов 4–6) и отраслевые ресурсы (GS1 EPCIS, markirovka.ru, rbs-id.ru). Ценовые ориентиры получены на момент исследования (сентябрь 2026) и могут отличаться от актуальных прайсов вендоров — почти все производители 2D-верификаторов/считывателей и print-apply систем работают по модели «цена по запросу», это стандартная практика для B2B промышленного оборудования.
