# resources-tool

### Сборка

Версия без gui\
```pyinstaller --onefile --icon=favicon.ico resources-tool.py``` 

Версия с gui\
```pyinstaller --onefile --windowed --name ResourcesTool --icon favicon.ico gui_app.py```

### Первый запуск

УЖЕ СОБРАННЫЕ EXE лежат в `dist`

Без GUI:
- запустить `resources-tool.exe` первый раз, чтоб создался конфиг
- внести в конфиг свои урони заводов
  - при необходимости сделать поправку на ускорение фабрики через ГБ или бусты (коэфф. `speed_mult`)
- перезапустить программу

С GUI:
- Запустить `ResourcesTool.exe`
- Заполнить свои уровни заводов во вкладке `Заводы`
  - при необходимости поменять цены ресурсов во вкладке `Ресурсы`