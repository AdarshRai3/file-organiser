from tasks.base import Task

class DoNothingTask(Task):
    def __init__(self):
        super().__init__("DoNothing")
        
    def execute(self, context):
        return context