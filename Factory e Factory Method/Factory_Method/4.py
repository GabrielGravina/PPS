from abc import ABC
from datetime import datetime

class Event(ABC):
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message

    def log(self):
        pass

class ErrorEvent(Event):
    def log(self):
        print(f"[{self.timestamp}] [Error] {self.message}")

class WarningEvent(Event):
    def log(self):
        print(f"[{self.timestamp}] [Warning] {self.message}")

class InfoEvent(Event):
    def log(self):
        print(f"[{self.timestamp}] [Info] {self.message}")

class EventFactory(ABC):
    def create_event(self, message):
        pass

class ErrorEventFactory(EventFactory):
    def create_event(self, message):
        return ErrorEvent(datetime.now(), message)

class WarningEventFactory(EventFactory):
    def create_event(self, message):
        return WarningEvent(datetime.now(), message)

class InfoEventFactory(EventFactory):
    def create_event(self, message):
        return InfoEvent(datetime.now(), message)

class EventLogger:
    def __init__(self, event_factory):
        self.event_factory = event_factory

    def log_event(self, message):
        event = self.event_factory.create_event(message)
        event.log()

if __name__ == "__main__":
    error_event_factory = ErrorEventFactory()
    warning_event_factory = WarningEventFactory()
    info_event_factory = InfoEventFactory()

    logger = EventLogger(error_event_factory)
    logger.log_event("Erro crítico detectado")

    logger = EventLogger(warning_event_factory)
    logger.log_event("Aviso: Recurso limitado")

    logger = EventLogger(info_event_factory)
    logger.log_event("Informação: Operação concluída com sucesso")
