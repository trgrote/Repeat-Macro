#
#   Sivakumar Kailasam and lowliet
#

import sublime, sublime_plugin

class RepeatMacroCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel("Repeat count or [Enter] to run till end of file", "", self.__execute, None, None)

    def __execute(self, text):
        if not text.isdigit() and len(text) > 0:
            print("Repeat Macro | Wrong number")
        else:
            current_line = self.__get_current_line()
            last_line = current_line + int(text) if len(text) > 0 else self.__get_last_line()
            for i in range(current_line, last_line):
                self.view.run_command("run_macro")

    def __get_current_line(self):
        return self.view.rowcol(self.view.sel()[0].begin())[0] + 1

    def __get_last_line(self):
        return self.view.rowcol(self.view.size())[0] + 2
