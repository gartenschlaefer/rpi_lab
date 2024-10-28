''' 
  - Die Log-Datei wird bei jedem Programmstart gelöscht
''' 
import os
from lib.wlandata import*

# Logpage
# --------------------------------------------------
def HTML(input):

    if input == "log":
        daten = log
    elif input == "safe":
        daten = safe
    else:
        daten = nothing
    
    refresh = daten.refresh
    filename = daten.filename
    titel = daten.titel
    content = daten.get_content()
    ip = get_device_ip()
    
    return """\
    <!DOCTYPE html>
    <html lang=de>
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="refresh" content="{}">
            <title>{}</title>
        </head>
        <body>
            <p><a href="http://{}:{}">Back</a> to Homepage<br>
            </p>
            <h1>{}</h1>
            <h3>
            {}
            </h3>
        </body>
    </html>
    """.format(refresh, filename, ip, port, titel, content)

class FileSafe:
    '''
      titel: wird als Überschrift und <title> eingesetzt
      content: der eigentliche Inhalt
      refresh: Refresh - Zeit in Sekunden
      filename: Filename, falls Speicherung gewünscht
    '''
    def __init__(self, titel, refresh, filename=""):
        self.titel = titel
        self.refresh = refresh
        self.filename = filename
        self.lines = []
        self.clear()
    
    def get_version(self):
        return 20 # enstspricht Version 2.0
    '''
      Der Filname kann nachträglich gesetzt oder gelöscht werden.
      set_filename() ohne Angabe löscht den Filenamen.
      Die bereits geschriebenen Werte werden jeweils übernommen.
    '''
    def set_filename(self, filename = ""):
        if self.filename != "":
            self.lines.clear()
            for line in self.read_lines_from_file():
                self.lines.append(line.rstrip())    
            os.remove(self.filename)
        else:
            with open(filename,"w") as file:
                for line in self.lines:
                  file.write(line + "\n")
            self.lines.clear()
        self.filename = filename
    
    def add_line_to_file(self, line=""):
        with open(self.filename,"a") as file:
            file.write(line + "\n")
    
    def read_lines_from_file(self):
        with open(self.filename,"r+") as file:
            return file.readlines()
    
    def read_last_line(self, back = -1):
        if (self.filename != ""):
            last_line = ""
            if self.read_lines_from_file():
                last_line = self.read_lines_from_file()[back]
            return last_line
        else:
            last_line = ""
            if self.lines:
                last_line = self.lines[back]
            return last_line
    
    def clear_file(self):
        with open(self.filename,"w") as file:
            pass
    
    def set_refresh(self, refresh):
        self.refresh = refresh
    
    def add(self, line = ""):
        if (self.filename != ""):
            self.add_line_to_file(line)
        else:
            self.lines.append(line)
    
    def clear(self):
        self.lines.clear()
        if (self.filename != ""):
            self.clear_file()
    
    def print(self):        
        if (self.filename != ""):
            for line in self.read_lines_from_file():
                print(line.rstrip())
        else:
            for line in self.lines:
                print(line)
    
    def get_content(self):
        if (self.filename != ""):
            content = ""
            for line in self.read_lines_from_file():
                content += line.rstrip() + "<br>"
            return content
        else:
            content = ""
            for line in self.lines:
                content += line + "<br>"
            return content
    
    def getHTML(self, input):
        return HTML(input)


log = FileSafe("LogFile",100,"log.txt")
safe = FileSafe("SafeFile",100,"safe.txt")
nothing = FileSafe("NoFile",100)
