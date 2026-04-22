from core.context import Context

class FileOrganizerAgent:
    def __init__(self,workflow):
        self.workflow = workflow
        
    def organize(self,directory):
        context = Context(directory)
        self.workflow.run(context)
        print("Organised")