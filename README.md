sublime-yandex-translate
========================
Yandex Translate plugin for SublimeText

Based on https://github.com/valmet/python-yandex-translate

ATTENTION
---------------
New functionality now need only to specify the language to be translated.
Instead 'en-ru' now need to write 'en'.


Install:
---------------

1. Get the [Yandex API-key](http://api.yandex.ru/key/form.xml?service=trnsl) or try this key `trnsl.1.1.20130705T052930Z.27fcc82ff0c243be.c0e2f80d06217633cd117ad29131aff078a05530` 
Please, use the tests only, as each key has a limit on number of translations
2. Install Plugin:

a) With [Package Control](https://sublime.wbond.net/installation):
Run “Package Control: Install Package” command, find and install `Yandex Translate` plugin.

b) Manually:
Clone or [download](https://github.com/pafnuty/sublime-yandex-translate/archive/master.zip) git repo into your packages folder (in ST, find Browse Packages... menu item to open this folder)


3. Set API-key in user settings: ```{
    "key": "YOUR_KEY",
    "output_language": "ru"
}```

Use:
---------------
Select text, press `ctrl+alt+t`
