from ..db.SQLighter import SQLighter
from .BaseService import BaseService

class StudentsService(BaseService):
    """класс инкапсулирует доступ к базе данных"""

    def __init__(self):
        BaseService.__init__(self)
        pass

    # записался ли студент на курс (return boolean)
    def is_student_recordered(self, id):
         user = self.db.execute_select('SELECT * FROM students WHERE number={};'.format(id))

         if len(user) > 0: return True
         else: return False
         pass
    # return student
    def get_student(self, id):
         sql = 'SELECT * FROM students WHERE number=\'{}\';'.format(id)
         user = self.db.execute_select(sql)
         if len(user) > 0:  return user[0];

         return None


        


