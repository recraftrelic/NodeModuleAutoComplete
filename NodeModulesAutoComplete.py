import os.path
import sublime
import sublime_plugin
import json
from os import path

class NodeModulesAutoCompleteCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		project_variables = sublime.active_window().extract_variables()
		project_folder = project_variables['folder']
		if project_folder is not None:
			package_json_path = project_folder + "/package.json"
			if path.exists(package_json_path):
				dependenciesArr = []
				with open(package_json_path) as package_json:
					data = json.load(package_json)
					for dependency in data["dependencies"]:
						dependenciesArr.append([dependency, dependency])
				return (dependenciesArr, 0)