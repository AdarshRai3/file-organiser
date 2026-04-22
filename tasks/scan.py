import os
from tasks.base import Task

IGNORE_EXT = ( ".crdownload", ".tmp", ".part") 

class ScanFilesTask(Task):
    def __init__(self, name:str="ScanFilesTask"):
        super().__init__(name)

    def execute(self, context):
       context.files =[
           f for f in os.listdir(context.directory) if os.path.isfile(os.path.join(context.directory, f)) and not f.endswith(IGNORE_EXT)
       ]
       return context

#Scan
#To fetch the extension fromm the downloaded file   
#    test.txt -> scan -> .txt