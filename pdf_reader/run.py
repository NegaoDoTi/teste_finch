import logging
from datetime import datetime
from schedule import every, repeat, run_pending
from automate.start import StartPdfReader
from time import sleep

logging.basicConfig(filename="pdf_reader.log", filemode="a", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

@repeat(every(1).minutes)
def run_pdf_reader() -> None:
    
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    start_message = f"Executando... {now}"
    
    print(start_message)
    logging.info(start_message)
    
    reader = StartPdfReader()
    
    reader.start()
    
    end = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    end_message = f"Fim da execução... {end}, Verifique a pasta results para ter acesso ao arquivos planilha!"
    
    print(end_message)
    logging.info(end_message)
    
if __name__ == "__main__":
    #run_pdf_reader()
    
    while True:
        run_pending()
        sleep(1)