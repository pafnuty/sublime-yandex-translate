
import sublime
import sublime_plugin
import json

from yandex_translate import *

class YaTranslateCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		settings = sublime.load_settings("yaTranslate.sublime-settings")
		key = settings.get("key")
		output_language = settings.get("output_language")
		
		if key:
			v = self.view
			selection = v.substr(v.sel()[0])

			translate = YandexTranslate(key)

			result = translate.translate(selection, output_language)

			text = (json.dumps(result['text']))
			text = text.replace('["', '')
			text = text.replace('"]', '')
			text = text.decode('unicode_escape')
			v.replace(edit, v.sel()[0], text)
			sublime.status_message(u'Done!')

		else:

			sublime.status_message(u'API Key not defined!')