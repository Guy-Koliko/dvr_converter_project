import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from converter import convert_tool



#g

src_dir ="../test_folder"
dst_dir ="./media"

def on_created(event):
    convert_tool(src_dir,dst_dir)
def on_deleted(event):
    print(event)
def on_modified(event):
    pass
def on_moved(event):
    pass

if __name__=="__main__":
    event_handler = FileSystemEventHandler()
    #calling Function
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved
    path ="../test_folder"
    observer = Observer()
    observer.schedule(event_handler,path,recursive=True)
    observer.start()
    try:
        print("Monitoring")
        while True: 
            time.sleep(1)
  
    except KeyboardInterrupt:
        observer.stop()
        print("Done")
    observer.join()
