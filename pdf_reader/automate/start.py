from rabbit.consume import RabbitConsume
from utils.manage_files import ManageFiles
from reader.extract_pdf import ExtractPDFData
import logging
from traceback import format_exc

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
                    logging.error(result["type"])
                    break
                
                download = self._manage_files.download_pdf_file(**result["message"])
                if download["error"] == True:
                    print(download["type"])
                    logging.error(download["type"])
                    continue
                                
                extractor = ExtractPDFData()
                
                result_extract = extractor.extract_data_pdf(download["pdf"])
                if result_extract["error"] == True:
                    print(result_extract["type"])
                    logging.error(result_extract["type"])
                    continue
                
                generate_excel = self._manage_files.generate_excel_file(result_extract["author_data"], result_extract["reus_data"], download["pdf"])
                if generate_excel["error"] == True:
                    print(generate_excel["type"])
                    logging.error(generate_excel["type"])
                    continue
                
                message = f'Arquivo Excel gerado na pasta: {generate_excel["path_xlsx"]}'
                
                print(message)
                logging.info(message)
            
            self._consume.channel.close()
            
            return
                
        except Exception:
            logging.critical(f"Erro inesperado: {format_exc()}")
            return