from pika import ConnectionParameters, PlainCredentials, BlockingConnection
from config.config import RABBIT_USER, RABBIT_PASSWORD, RABBIT_HOST, RABBIT_PORT, RABBIT_VHOST, RABBIT_QUEUE
from json import dumps
from traceback import format_exc
import logging

class RabbitPublish:
    def __init__(self):
        self.__credentials = PlainCredentials(RABBIT_USER, RABBIT_PASSWORD)
        self.__parameters = ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT, virtual_host=RABBIT_VHOST, credentials=self.__credentials)
        self.__connection = BlockingConnection(self.__parameters)
        self.channel = self.__connection.channel()
        
        self.channel.queue_declare(RABBIT_QUEUE, durable=True)
        
    def publish_one(self, token:str, url:str) -> dict:
        """Função responsavel por publicar token e url em uma fila rabbit

        Args:
            token (str): token que permite baixar os arquivos PDF
            url (str): url do arquivo PDF

        Returns:
            dict: (bool, str)
        """
        
        try:
            message = dumps(
                {
                    "token" : token,
                    "url" : url
                }
            )
            
            self.channel.basic_publish(exchange="", routing_key=RABBIT_QUEUE, body=message)
            
            return {"error" : False, "type" : ""}
        
        except Exception:
            logging.error(f"{format_exc()}")
            return {"error" : True, "type" : "Erro inesperado ao publicar mensagem! Contate o ADM"}