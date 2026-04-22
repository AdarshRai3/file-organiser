import time
from watchdog.events import FileSystemEventHandler

class DownloadHandler(FileSystemEventHandler):
    def __init__(self,agent,directory):
        self.agent = agent
        self.directory = directory

    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            time.sleep(1)  # Wait for the file to be fully written
            self.agent.organize(self.directory)