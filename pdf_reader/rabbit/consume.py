from pika import ConnectionParameters, PlainCredentials, BlockingConnection
from config.config import RABBIT_HOST, RABBIT_USER, RABBIT_PASSWORD, RABBIT_PORT, RABBIT_QUEUE, RABBIT_VHOST
from json import loads
from traceback import format_exc
import logging

class RabbitConsume:
    
    def __init__(self):
        self.__credentials = PlainCredentials(RABBIT_USER, RABBIT_PASSWORD)
        self.__parameters = ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT, virtual_host=RABBIT_VHOST, credentials=self.__credentials)
        self.__connection = BlockingConnection(self.__parameters)
        self.channel = self.__connection.channel()
        
    def consume_one(self) -> dict[bool, str, str, dict]:
        try:
            method_frame, header_frame, body = self.channel.basic_get(queue=RABBIT_QUEUE)
            
            if method_frame:
                
                message = body.decode("utf-8")
                
                self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
                
                message = loads(message)
                
                return {'error' : False, "type" : "", "message" : message}
            else:
                print("Sem mensagens para consumir, fila vazia!")
                return {"error" : True, "type" : "Sem mensagens para consumir, fila vazia!"}
            
        except Exception:
            logging.error(f"{format_exc()}")
            return {"error" : True, "type" : "Erro inesperado ao consumir fila", "message" : {} }