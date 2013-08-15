import sublime
import sublime_plugin

from yandex_translate import *

class YaTranslateCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view

        translate = YandexTranslate('trnsl.1.1.20130705T052930Z.27fcc82ff0c243be.c0e2f80d06217633cd117ad29131aff078a05530')

        result = translate.translate('Hello World', 'en-ru')

        # code not work :(
        # v.replace(edit, v.sel()[0], result['text'])

        v.replace(edit, v.sel()[0], 'result')
