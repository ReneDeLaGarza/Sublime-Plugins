import sublime, sublime_plugin
import simplejson as json

class PrettyjsonCommand(sublime_plugin.TextCommand):
    def run(self,  args): 
        edit = self.view.begin_edit()
        for region in self.view.sel():        
            if not region.empty():                                    
                s = self.view.substr(region)
                input = json.loads(s)
                x = json.dumps(input, sort_keys = False, indent = 4)
                self.view.replace(edit, region, x )
        self.view.end_edit(edit)