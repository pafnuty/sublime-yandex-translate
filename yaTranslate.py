
import sublime
import sublime_plugin
import json

if sublime.version() < '3':
    from core import *
else:
    from .core import *


class YaTranslateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings("yaTranslate.sublime-settings")
		key = settings.get("key")
		output_language = settings.get("output_language")

		for region in self.view.sel():
			if region.empty():
				continue
	
			if key:
				v = self.view
				selection = v.substr(v.sel()[0])

				translate = YandexTranslate(key)

				detected = translate.detect(selection)
				if detected:
					result = translate.translate(selection, detected+'-'+output_language)
				else:
					sublime.status_message(u'Error! (Look in console)')

				text = (json.dumps(result['text'], ensure_ascii = False))
				text = text.replace('["', '')
				text = text.replace('"]', '')

				v.replace(edit, v.sel()[0], text)
				if (result['code'] == 200):
					sublime.status_message(u'Done! (translate '+detected+' --> '+output_language+')')
				else: 
					sublime.status_message(u'Error! (Look in console)')

			else:				
				sublime.status_message(u'API Key not defined!')


	def is_visible(self):
		for region in self.view.sel():
			if not region.empty():
				return True
		return False

class YaTranslateInfoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings("yaTranslate.sublime-settings")
		key = settings.get("key")
		output_language = settings.get("output_language")

		if key:
			v = self.view
			selection = v.substr(v.sel()[0])

			translate = YandexTranslate(key)

			print(json.dumps(translate.langs))

			text = (json.dumps(translate.langs))

			v.replace(edit, v.sel()[0], text)

		else:

			sublime.status_message(u'API Key not defined!')
		