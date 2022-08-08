class EventReader:
    def __init__(self, path):
        self.path_to_event_txt = path
        self.eventlog = []
        self.file = open(self.path_to_event_txt, 'r')

    def __del__(self):
        self.file.close()

    def read_event_file(self):
        while True:
            line = self.file.readline()
            if not line:
                break

    def handle_eventlog(self):
        line = self.file.readline()
        if line:
            return line

