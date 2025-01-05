from pathlib import Path
from requests import get
from traceback import format_exc
from openpyxl import Workbook
import logging

class ManageFiles:
    
    def __init__(self):
        self.downloads_folder = Path(Path(__file__).parent.parent, "downloads")
        self.result_folder = Path(Path(__file__).parent.parent, "results")
        self.verify_folders()
        
    def verify_folders(self) -> None:
        if not self.downloads_folder.exists():
            self.downloads_folder.mkdir()
        
        if not self.result_folder.exists():
            self.result_folder.mkdir()
            
    def download_pdf_file(self, token:str, url:str) -> dict[bool, str, str]:
        try:
            
            header = {
                "token" : token
            }
            
            download = get(url=url, headers=header, stream=True)
            
            download.raise_for_status()
            
            pdf_path = f'{self.downloads_folder}/{url.split("/")[-1]}'
            
            with open(pdf_path, "wb") as pdf_file:
                for chunk in download.iter_content(chunk_size=8192):
                    pdf_file.write(chunk)

                pdf_file.close()
                
            return {"error" : False, "type" : "", "pdf" : pdf_path}
        
        except Exception:
            
            logging.error(f"{format_exc()} token: {token} url: {url}")
            return {"error" : True, "type" : f"Erro inesperado ao efetuar download do arquivo PDF! token: {token} url: {url}", "pdf" : ""}
    
    def generate_excel_file(self, author_data:dict, reus_data:dict, name_file:str):
        try:
            wb = Workbook()
            
            ws = wb.active
            
            headline = ["NOME AUTOR", "DOCUMENTO AUTOR", "NOMES RÉUS", "DOCUMENTOS RÉUS"]
            
            ws.append(headline)
            
            line = [author_data["author_name"], author_data["author_document"], reus_data["reus_names"], reus_data["reus_documents"]]
            
            ws.append(line)
            
            name_file = name_file.split("/")[-1].replace(".pdf", ".xlsx")
            
            path_xlsx = f"{self.result_folder}/{name_file}"
            
            wb.save(path_xlsx)
            
            return {"error" : False, "type" : "", "path_xlsx" : path_xlsx}
            
        except Exception:
            
            logging.error(f"{format_exc()} author_data {author_data}, reus_data: {reus_data}")
            return {"error" : True, "type" : f"Erro inesperado ao gerar arquivo xlsx author_data {author_data}, reus_data: {reus_data}"}