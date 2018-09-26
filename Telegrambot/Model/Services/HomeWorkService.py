from ..db.SQLighter import SQLighter
from .BaseService import BaseService

class HomeWorkService(BaseService):
    """обеспечивает доступ к домашним работам"""

    def __init__(self):
        BaseService.__init__(self)
        pass

    def add_hw(self,name, description):
        return "метод в сервисе пустой"



