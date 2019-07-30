import sublime
import sublime_plugin

class NodeModulesAutoCompleteCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		return ["sublime", "sublime text", "sublime text 3"]