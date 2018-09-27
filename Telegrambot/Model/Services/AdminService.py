from ..db.SQLighter import SQLighter
from .BaseService import BaseService

class AdminService(BaseService):
    """description of class"""

    def __init__(self):
        BaseService.__init__(self)
        pass

    def is_admin_recordered(self):
        user = self.db.execute_select('SELECT * FROM students WHERE number=\'0\';')

        if len(user) > 0: return True
        else: return False
        pass
    # проверка на админа
    def is_admin(self, id):
        user = self.db.execute_select('SELECT * FROM students WHERE userId={};'.format(id))

        if len(user) > 0: return True
        else: return False
        pass

    def add_admin(self, user_id):
        select_sql = 'SELECT * FROM students WHERE userId={};'.format(user_id)
        insert_sql = ('INSERT INTO students(number, last_name, first_name, middle_name, userId) VALUES (\'0\', \'\', \'\', \'\', {});'
                        .format(user_id))
        if self.is_admin_recordered():
            return "администратор уже существует"

        if len(self.db.execute_select(select_sql)) > 0:
            return "вы уже зарегестрированы как студент"

        try:
            self.db.execute_insert(insert_sql)
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass

        return "вы успешно зарегестрированы"

