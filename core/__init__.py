import sublime

if sublime.version() < '3':
    from translate_old import *
else:
    from YandexTranslate.core.translate_old import *