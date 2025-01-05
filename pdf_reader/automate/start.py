from rabbit.consume import RabbitConsume
from utils.manage_files import ManageFiles
from reader.extract_pdf import ExtractPDFData

class StartPdfReader:
    
    def __init__(self):
        self._manage_files = ManageFiles()
        
    def start(self) -> None:
        try:
            while True:
                
                self._consume = RabbitConsume()
                
                result = self._consume.consume_one()
                if result["error"] == True:
                    print(result["type"])
                    break
                
                download = self._manage_files.download_pdf_file(**result["message"])
                if download["error"] == True:
                    print(download["type"])
                    continue
                                
                extractor = ExtractPDFData()
                
                result_extract = extractor.extract_data_pdf(download["pdf"])
                if result_extract["error"] == True:
                    print(result_extract["type"])
                    continue
                
        except Exception:
            ...