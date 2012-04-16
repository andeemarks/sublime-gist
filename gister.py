import sublime, sublime_plugin
import urllib, urllib2
import json
from datetime import datetime
import os

class CreateGistCommand(sublime_plugin.TextCommand):
    GIST_API_URL_ROOT = 'https://api.github.com/gists'
    NAME = "SubGist"

    def run(self, edit):
        gist_content = self.find_content(edit)
        result = self.create_gist(gist_content, "Created by %s" % self.NAME)
        self.show_result(edit, result['html_url'])

    def create_gist(self, gist_content, description):
        try:  
            request_body = self.build_request(description, gist_content)
            result = self.execute_request(request_body)
            
            return result

        except (urllib2.HTTPError) as (e):  
            err = '%s: HTTP error %s contacting API' % (__name__, str(e.code))  
        except (urllib2.URLError) as (e):  
            err = '%s: URL error %s contacting API' % (__name__, str(e.reason))  

        sublime.error_message(err)

    def execute_request(self, request_body):
        request = urllib2.Request(self.GIST_API_URL_ROOT, request_body)
        http_file = urllib2.urlopen(request, timeout=100)  
        result = http_file.read()  
        
        return json.loads(result)

    def build_request(self, description, gist_content):
        file_name = os.path.basename(self.view.file_name())
        data = { 'public':'true', 'description':description, 'files':{file_name:{'content':gist_content}}}
        return json.dumps(data) 

    def find_content(self, edit):
        selections = self.view.sel()  

        selected_text = ''
        for sel in selections:  
            selected_text += self.view.substr(sel)

        if selected_text == '':
            return self.full_text()
        else:
            return selected_text

    def full_text(self):
        full_text = sublime.Region(0, self.view.size())
        return self.view.substr(full_text)

    def show_result(self, edit, gist_url):
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.view.insert(edit, 0, "[%(name)s] %(url)s created %(timestamp)s\n" % { "name": self.NAME, "timestamp": timestamp, "url": gist_url })
        self.view.run_command("goto_line", {"line": 1})
        self.view.run_command("toggle_comment")

