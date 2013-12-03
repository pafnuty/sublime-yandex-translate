sublime-yandex-translate
========================
![sublime-yandex-translate](https://dl.dropboxusercontent.com/u/8142395/yat.gif)

Yandex Translate plugin for SublimeText 2 and 3

Based on https://github.com/valmet/python-yandex-translate

Configure:
---------------
1. Do not forget to get a free [Yandex API-key](http://api.yandex.ru/key/form.xml?service=trnsl)

	or try this key `trnsl.1.1.20130705T052930Z.27fcc82ff0c243be.c0e2f80d06217633cd117ad29131aff078a05530` 
	Please, use the tests only, as each key has a limit on number of translations

2. For a list of possible translations in the menu, select "Tools > Yandex Translate > Show the available options for the transfer of"

3. Set API-key in user settings:
```
{
    "key": "YOUR_KEY",
    "ui_lang": "ru",
    "output_language": "ru",
    "type": "text"
}
```

Use:
---------------
Select text and:
- press `ctrl+alt+t` or select "Translate selected text" in context menu
- press `ctrl+shift+alt+t` or select "Translate selected on..." in context menu to select the language for translation




---- То же самое на руссом языке ----

sublime-yandex-translate
========================
Плагин для удобного перевода текста в SublimeText 2 и 3

Плагин основан на скрипте: https://github.com/valmet/python-yandex-translate

Настройка:
---------------
1. Не забудьте получить бесплатный [Yandex API-key](http://api.yandex.ru/key/form.xml?service=trnsl)

	или возьмите этот ключ `trnsl.1.1.20130705T052930Z.27fcc82ff0c243be.c0e2f80d06217633cd117ad29131aff078a05530` 
	Пожалуйста, используйте этот ключ только для тестов, я им тоже пользуюсь, а у каждого ключа есть ограничение по количеству переводов.

2. Посмотреть возможные направления перевода можно перейдя в меню "Tools > Yandex Translate > Show the available options for the transfer of"

3. Вставьте полученый API key в файл настроек плагина вместо текста YOUR_KEY:
```
{
    "key": "YOUR_KEY",
    "ui_lang": "ru",
    "output_language": "ru",
    "type": "text"
}
```

Использование:
---------------
Выберите текст:
- нажмите хоткей `ctrl+alt+t` или выберите пункт "Translate selected text" в контекстном меню
- нажмите хоткей `ctrl+shift+alt+t` или выберите пункт "Translate selected on..." в контекстном меню для выбора языка перевода


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/pafnuty/sublime-yandex-translate/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

