import os, shutil
from tasks.base import Task

class MoveFilesTask(Task):
    def execute(self,context):
        base = context.directory
        
        for folder, files in context.classified.items():
            path = os.path.join(base,folder)
            
            os.makedirs(path, exist_ok=True)
            
            for f in files:
                src = os.path.join(base,f)
                dst = os.path.join(path,f)
                
                if os.path.exists(dst):
                    print(f"File {dst} already exists, skipping {src}")
                    continue
                
                print(f"Moving {src} to {dst}")
                shutil.move(src, dst)
            
            return context