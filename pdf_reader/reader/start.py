from rabbit.consume import RabbitConsume
from utils.manage_files import ManageFiles

class StartPdfReader:
    
    def __init__(self):
        self._manage_files = ManageFiles()
        
    def start(self) -> None:
        try:
            while True:
                
                self._consume = RabbitConsume()
                
                result = self._consume.consume_one()
                if result["error"] == True:
                    break
                
                download = self._manage_files.download_pdf_file(**result["message"])
                if download["error"] == True:
                    continue
                
                pdf = download["pdf"]
                
        except Exception:
            ...