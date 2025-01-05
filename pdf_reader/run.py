import logging
from datetime import datetime
from schedule import every, repeat, run_pending
from automate.start import StartPdfReader
from time import sleep

logging.basicConfig(filename="pdf_reader.log", filemode="a", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

@repeat(every(1).minutes)
def run_pdf_reader() -> None:
    
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    print(f"Executando... {now}")
    
    reader = StartPdfReader()
    
    reader.start()
    
    end = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Fim da execução... {end}")
    
if __name__ == "__main__":
    run_pdf_reader()
    
    #while True:
        #run_pending()
        #sleep(1)