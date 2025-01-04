from pathlib import Path
from config.serializer import serializer
from time import time
from flask import jsonify
from uuid import uuid4
from rabbit.publish import RabbitPublish

class UploadController:

    def __init__(self):
        self.download_folder = Path(Path(__file__).parent.parent , "static", "downloads")
        
    def uploaded_pdfs_files(self, req):
        """
            Função responsavel por gerenciar o upload de até 5 arquivos PDF,
            salva esses arquivos como nome uuid4, gera token que permite o download
            desses arquivos dentro de 24 horas

        Args:
            req (flask.request): Objeto request da requisição

        Returns:
            flask.Response: retorna um json com uma mensagem informando de houve sucesso ou falha
        """
        
        try:
            token = serializer.dumps({"timestamp" : time()})
            
            files = req.files.getlist('pdfFiles')
            
            if len(files) > 5:
                return jsonify({"message" : "Erro foram enviado uma quantidade maior de pdfs"}), 400
            
            rabbit_publish = RabbitPublish()
            
            for file in files:
                if not file.filename.endswith(".pdf"):
                    return jsonify({"message" : "Erro um dos arquivos não é do tipo pdf!"}), 400
                
                local_filename = f"{uuid4()}.pdf"
                path_file = str(Path(Path(self.download_folder), local_filename))
                
                file.save(path_file)
                
                result = rabbit_publish.publish_one(token, f"http://web:5000/download/{local_filename}")
                if result["error"] == True:
                    return jsonify({"message" : f'{result["type"]}'}), 500
            
            rabbit_publish.channel.close()
            
            return jsonify({"message" : "Arquivos enviados com sucesso!"}), 200
        
        except Exception:
            return jsonify({"message" : "Erro inesperado ao enviar arquivos! Contate o ADM"}), 500