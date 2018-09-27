from ..db.SQLighter import SQLighter
from .BaseService import BaseService

class HomeWorkService(BaseService):
    """обеспечивает доступ к домашним работам"""

    def __init__(self):
        BaseService.__init__(self)
        pass

    def add_hw(self,name, description):
            # НАЗВАНИЕ, ОПИСАНИЕ 
        insert_sql = ('INSERT INTO homeworks(name, description) VALUES (\'{}\', \'{}\');'.format(name, description))
        if name == "":
            return "Название домашней работы задано неверно"
        if description == "":
            return "Описание домашней работы задано неверно"
        
        try:
            self.db.execute_insert(insert_sql)
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass
        # КОЛИЧЕСТВО ДОМАШЕК
        sql = 'UPDATE sqlite_sequence SET seq= seq +1  WHERE name=\'homeworks\';'
        count = self.db.execute_select('SELECT seq FROM sqlite_sequence WHERE name=\'homeworks\';')
        # добавить колонку 
        insert_sql = ('ALTER TABLE ratings ADD \'hw_{}\' TEXT DEFAULT \'-\' NOT NULL;'.format(count[0][0]))
         
        try:
            self.db.execute_insert(insert_sql)
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass
        return "Добавление домашней работы произошло успешно"
     
    def get_all_hw(self):
         sql = 'SELECT * FROM homeworks;'
         hw = self.db.execute_select(sql)
         if len(hw) > 0:  return hw;

         return None

     


