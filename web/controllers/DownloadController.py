from pathlib import Path
from flask import send_file, jsonify
from config.serializer import serializer
from itsdangerous.exc import SignatureExpired, BadSignature
from traceback import format_exc
import logging

class DownloadController:

    def __init__(self):
        self.download_folder = Path(Path(__file__).parent.parent, "static", "downloads")
        self.verify_downloads_folder()
        
    def verify_downloads_folder(self):
        if not self.download_folder.exists():
            self.download_folder.mkdir()
        
    def send_pdf_file(self, req, archive_name):
        """
            Função responsavel por devolver um arquivo PDF dentro da condições,
            desde que o token tenha não expirado apos de 24 horas e se o arquivo 
            existir no servidor

        Args:
            req (flask.request): Objeto request da requisição
            archive_name (str): nome do arquivo pdf

        Returns:
            flask.Response: Caso todas condições sejam atendidas e retornado um arquivo PDF
            flask.Response: Caso alguma condição esteja incorreta retornado um json com uma mensagem de erro
        """
        
        try:
                authorization = req.headers.get("token")
                
                if not authorization:
                    return jsonify({"message" : "Erro acesso negado, token não fornecido!"}), 401
                
                try:
                    token = serializer.loads(authorization, max_age=86400) # Verifica se o token ja execeu as 24 horas, ou é invalido
                except SignatureExpired:
                    return jsonify({"message" : "Erro acesso negado, token expirado!"}), 401
                
                except BadSignature:
                    return jsonify({"message" : "Erro acesso negado, token incorreto!"}), 401
                
                path_file = Path(Path(self.download_folder), archive_name)
                
                if not path_file.exists():
                    return jsonify({"message" : "Erro arquivo não existe mais!"}), 404
                    
                return send_file(str(path_file)), 200
            
        except Exception:
            logging.error(f"{format_exc()}")
            return jsonify({"message" : "Erro interno no servidor, contate o ADM!"}), 500