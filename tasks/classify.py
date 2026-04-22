from tasks.base import Task
from strategies.types import ImageStrategy, DocumentStrategy, AudioStrategy, CodeStrategy

class ClassifyFilesTask(Task):
    def __init__(self,strategies):
        super().__init__("Classify")
        self.strategies = strategies
        
    def execute(self,context):
        context.classified.clear()
        for file in context.files:
            for s in self.strategies:
                if s.matches(file):
                    context.classified.setdefault(s.folder(), []).append(file)
                    break
        
        return context
    
#Classify : Use the extractred extension from  scan (.txt) and classify the file into the respective folder (Documents, Images, Audio, Code)using the strategy pattern. Each strategy will define the matching criteria for a specific type of file and the corresponding folder name.