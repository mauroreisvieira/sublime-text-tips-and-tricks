import sublime
import sublime_plugin


SETTINGS_FILE = "Preferences.sublime-settings"
TRIM_TRAILING_EXTRA_LINES  = "trim_trailing_extra_lines"


class DeleteExtraTrailingLines(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        view.run_command('trim_trailing_extra_lines')

class TrimTrailingExtraLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        match = self.view.find(r'(?<=\n)\s+\z', 0)
        settings = sublime.load_settings(SETTINGS_FILE)
        if match != (-1, -1) and settings.get(TRIM_TRAILING_EXTRA_LINES, True):
            self.view.erase(edit, match)
