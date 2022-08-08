import tkinter as tk
import eventReader

PATH_EVENT = 'F:/Program Files (x86)/Steam/steamapps/common/Wurm Online/gamedata/players/Szewo/logs/_Event.2022-08.txt'
VERSION = '0.1'


class Gui:
    def __init__(self, root):
        self.root = root
        self.eventReader = eventReader.EventReader(PATH_EVENT)
        self.eventReader.read_event_file()
        self.eventlog = tk.Text(self.root, height=4, background="gray71", font=('Sans Serif', 13, 'italic bold'))
        self.eventlog.pack(fill='x')

    def setup(self):
        self.root.title("Wurmbot Alpha v{}".format(VERSION))
        self.root.geometry("800x600")

    def event_window(self):
        eventEntry = self.eventReader.handle_eventlog()
        if eventEntry:
            self.eventlog.insert(tk.INSERT, eventEntry)
            self.eventlog.see(tk.INSERT)
        self.root.after(200, self.event_window)




