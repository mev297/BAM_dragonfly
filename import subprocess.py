import subprocess
import shutil
import os
from tkinter import Tk, Button
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEditHandler(FileSystemEventHandler):
def __init__(self, file_path, callback):
self.file_path = file_path
self.callback = callback

def on_modified(self, event):
if event.src_path == self.file_path:
self.callback()

def run_programs(program1, program2):
subprocess.Popen(program1)
subprocess.Popen(program2)

def transfer_file(source, destination):
shutil.copy(source, destination)
print(f"File transferred from {source} to {destination}")

def setup_file_watcher(file_path, callback):
event_handler = FileEditHandler(file_path, callback)
observer = Observer()
observer.schedule(event_handler, path=os.path.dirname(file_path), recursive=False)
observer.start()
return observer

def main():
program1 = 'path/to/program1.exe' # Replace with your program's path
program2 = 'path/to/program2.exe' # Replace with your second program's path
file_path = 'path/to/edited_file.txt' # Replace with your file's path
destination_path = 'path/to/destination_folder' # Replace with your destination folder's path

run_programs(program1, program2)

def on_file_edit():
transfer_file(file_path, destination_path)

observer = setup_file_watcher(file_path, on_file_edit)

root = Tk()
Button(root, text="Transfer File", command=on_file_edit).pack()
root.mainloop()
observer.stop()
observer.join()

if __name__ == "__main__":
main()
