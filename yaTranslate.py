# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import json

if sublime.version() < '3':
    from core import *
else:
    from .core import *

settings = sublime.load_settings("yaTranslate.sublime-settings")

class YaTranslateCommand(sublime_plugin.TextCommand):

	def run(self, edit, output_language = settings.get("output_language")):
		key = settings.get("key")
		ui_lang = settings.get("ui_lang")
		if not output_language:
			output_language = settings.get("output_language")
		output_type = settings.get("type")

		for region in self.view.sel():
			if not region.empty():

				if key:
					v = self.view
					selection = v.substr(region).encode('utf-8')
					translate = YandexTranslate(key, ui_lang)

					detected = translate.detect(selection)
					if detected:
						if (detected == output_language):
							self.view.run_command("ya_translate_to")
							return
						else:
							result = translate.translate(selection, detected+'-'+output_language, output_type)
					else:
						sublime.status_message(u'Error! (Look in console)')

					text = (json.dumps(result['text'][0], ensure_ascii = False)).strip('"').replace('\\n', "\n").replace('\\t', "\t").replace('\\"', '"')

					v.replace(edit, region, text)
					if (result['code'] == 200):
						sublime.status_message(u'Text translated: '+detected+' --> '+output_language)
					else:
						sublime.status_message(u'Error of translate text: look in console!')

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
		ui_lang = settings.get("ui_lang")
		output_language = settings.get("output_language")
		output_type = settings.get("type")

		if key:
			v = self.view
			selection = v.substr(v.sel()[0])

			translate = YandexTranslate(key, ui_lang)

			text = (json.dumps(translate.langs, ensure_ascii = False, indent = 2))

			v.replace(edit, v.sel()[0], text)

		else:

			sublime.status_message(u'API Key not defined!')

class YaTranslateToCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings("yaTranslate.sublime-settings")
		key = settings.get("key")
		ui_lang = settings.get("ui_lang")
		output_type = settings.get("type")

		if key:
			v = self.view
			selection = v.substr(v.sel()[0])

			translate = YandexTranslate(key, ui_lang)

			text = (json.dumps(translate.langs['langs'], ensure_ascii = False))
			continents = json.loads(text)
			lkey = []
			ltrasl = []

			for (slug, title) in continents.items():
				lkey.append(slug)
				ltrasl.append(title+' ['+slug+']')

			def on_done(index):
				if index >= 0:
					self.view.run_command("ya_translate", {"output_language": lkey[index]})

			self.view.window().show_quick_panel(ltrasl, on_done)

		else:

			sublime.status_message(u'API Key not defined!')

	def is_visible(self):
		for region in self.view.sel():
			if not region.empty():
				return True
		return False


def plugin_loaded():
    global settings
    settings = sublime.load_settings("yaTranslate.sublime-settings")