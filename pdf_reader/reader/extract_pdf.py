from PyPDF2 import PdfReader
from traceback import format_exc
import re
import logging

class ExtractPDFData:
    
    def extract_data_pdf(self, pdf_path) -> dict:
        
        try:
            read = self.__reader_pdf(pdf_path)
            
            author_data = self.__find_autor(read["author_part"])
            if author_data["error"] == True:
                logging.error(f'{author_data["type"]} {pdf_path}')
                return author_data
            
            reus_data = self.__find_reus(read["reus_part"])
            if reus_data["error"] == True:
                logging.error(f'{reus_data["type"]} {pdf_path}')
                return reus_data
            
            return {
                "error" : False,
                "type" : "",
                "author_data" : {
                    "author_name" : author_data["author_name"],
                    "author_document" : author_data["author_document"]
                },
                "reus_data" : {
                    "reus_names" : reus_data["reus_names"],
                    "reus_documents" : reus_data["reus_documents"]
                }
            }
            
        except Exception:
            logging.error(f'Erro inesperado ao extrair dados do pdf!: {format_exc()}')
            return {"error" : True, "type" : "Erro inesperado ao extrair dados do pdf!"}
    
    def __reader_pdf(self, pdf_path) -> dict:
        try:
            pdf = PdfReader(str(pdf_path))
            
            string_pdf = ""
            for pages in pdf.pages:
                string_pdf = string_pdf + pages.extract_text().lower()
            
            parts_text = re.split(r"(?=réus:)", string_pdf, maxsplit=1)
            author_part = parts_text[0].strip()
                
            reus_part = parts_text[1].strip()
            
            return {"author_part" : author_part, "reus_part" : reus_part}
        
        except Exception:
            logging.error(f"Erro inesperado ao ler arquivo pdf {pdf_path}")
                
    def __find_autor(self, string_part:str) -> dict[bool, str, str, str]:
            
            name_pattern = r"autor:\s*([A-Za-záéíóúãââà\s]+)(?=\s*\n)"
            document_pattern = r"\s*?(\d{3}\s*?\.?\s*?\d{3}\s*?\.?\s*?\d{3}\s*?-?\s*?\d{2})|\s*?(\d{2}\s*?\.?\s*?\d{3}\s*?\.?\s*?\d{3}/\d{4}\s*?-?\s*?\d{2})"
            
            names_found = re.search(name_pattern, string_part, re.IGNORECASE)
            document_found = re.search(document_pattern, string_part, re.IGNORECASE)
            
            try:
                author_name = names_found.group(1)
            except:
                return {"error" : True, "type" : f"Erro nome do autor não encontrado no pdf", "author_name" : "", "author_document" : ""}
            
            try:
                author_document = document_found.group(0)
            except:
                return {"error" : True, "type" : "Erro documento do autor não encontrado no pdf", "author_name" : "", "author_document" : ""}
            
            return {"error" : False, "type" : "", "author_name" : author_name, "author_document" : author_document}
        
    def __find_reus(self, string_part:str) -> dict[bool, str, str, str]:
        
        reus_names_pattern = r"réus?:\s*([A-Za-záéíóúãââà\s]+(?:\s[e|e\s][A-Za-záéíóúãââà\s]+)?)"
        reus_documents_pattern = r"\s*?(\d{3}\s*?\.?\s*?\d{3}\s*?\.?\s*?\d{3}\s*?-?\s*?\d{2})|\s*?(\d{2}\s*?\.?\s*?\d{3}\s*?\.?\s*?\d{3}/\d{4}\s*?-?\s*?\d{2})"
        
        try:
            reus_names = re.findall(reus_names_pattern, string_part, re.IGNORECASE)[0]
        except:
            return {"error" : True, "type" : "Erro nome dos reus não encontrado no pdf", "reus_names" : "", "reus_documents" : ""}
        
        try:
            reus_documents = re.findall(reus_documents_pattern, string_part, re.IGNORECASE)
            reus_documents = ", ".join( item for data in reus_documents for item in data if item.strip() )
        except:
            return {"error" : True, "type" : "Erro documentos dos reus não encontrado no pdf", "reus_names" : "", "reus_documents": ""}
        
        return {"error" : False, "type" : "", "reus_names" : reus_names, "reus_documents" : reus_documents}

        
