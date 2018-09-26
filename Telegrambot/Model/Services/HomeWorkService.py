from ..db.SQLighter import SQLighter
from .BaseService import BaseService

class HomeWorkService(BaseService):
    """обеспечивает доступ к домашним работам"""

    def __init__(self):
        BaseService.__init__(self)
        pass

    def add_hw(self,name, description):
            # НАЗВАНИЕ description
            # КОЛИЧЕСТВО ДОМАШЕК
            # добавить колонку 
        return "метод в сервисе пустой"

    def get_all_hw(self):
         sql = 'SELECT * FROM homeworks;'
         hw = self.db.execute_select(sql)
         if len(hw) > 0:  return hw;

         return None

     


