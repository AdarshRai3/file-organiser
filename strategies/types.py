class ImageStrategy:
   def matches(self,f): 
       return f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"))
   
   def folder(self):
       return "Images"
   
class DocumentStrategy:
    def matches(self,f):
        return f.lower().endswith((".pdf", ".docx", ".txt", ".xlsx", ".pptx"))
    
    def folder(self):
        return "Documents"
    
class AudioStrategy:
    def matches(self,f):
        return f.lower().endswith((".mp3", ".wav", ".aac", ".flac"))
    
    def folder(self):
        return "Audio"
    
class CodeStrategy:
    def matches(self,f):
        return f.lower().endswith((".py", ".js", ".java", ".cpp", ".c", ".rb",".go","rs",".ts"))
    
    def folder(self):
        return "Code"
    
class VideoStrategy:
    def matches(self,f):
        return f.lower().endswith((".mp4", ".avi", ".mkv", ".mov"))
    
    def folder(self):
        return "Videos"