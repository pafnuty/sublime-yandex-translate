import sublime

if sublime.version() < '3':
    from translate import *
else:
    from YandexTranslate.core.translate import *