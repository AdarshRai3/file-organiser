class Workflow:
    
    def __init__(self):
        self.tasks = [] 
        
    def add_task(self,task):
        self.tasks.append(task)
    
    def run(self,context):
        for task in self.tasks:
            context = task.execute(context)
        return context