from ..db.SQLighter import SQLighter
from .BaseService import BaseService

class StudentsService(BaseService):
    """класс инкапсулирует доступ к базе данных"""

    def __init__(self):
        BaseService.__init__(self)
        pass

    # записался ли студент на курс (return boolean)
    def is_student_recordered(self, id):
         user = self.db.execute_select('SELECT * FROM students WHERE userId={};'.format(id))

         if len(user) > 0: return True
         else: return False
         pass
    # return student
    def get_student(self, id):
         sql = 'SELECT * FROM students WHERE number=\'{}\';'.format(id)
         user = self.db.execute_select(sql)
         if len(user) > 0:  return user[0];

         return None

    def get_all_students(self):
        sql = 'SELECT number, last_name, first_name, middle_name FROM students;'.format(id)
        user = self.db.execute_select(sql)
        if len(user) > 0:  return user;

        return None

    def delete_student(self, user_id):
        sql = 'DELETE FROM students WHERE userId={}'.format(user_id)
        try:
            self.db.execute_insert(sql)
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass

        return "вы удалены с курса"

    def get_student_by_userId(self, id):
         sql = 'SELECT * FROM students WHERE userId=\'{}\';'.format(id)
         user = self.db.execute_select(sql)
         if len(user) > 0:  return user[0];

         return None

    def is_student_recordered_userId(self, id):
        user = self.db.execute_select('SELECT * FROM students WHERE userId={};'.format(id))

        if len(user) > 0: return True
        else: return False
        pass

    def add_student(self, number, last_name, first_name, middle_name, user_id):
        insert_sql = ('INSERT INTO students(number, last_name, first_name, middle_name, userId) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', {});'
                        .format(number, last_name, first_name, middle_name, user_id))

        if number == "":
            return "номер зачётной книжки задан не верно"

        if self.is_student_recordered_userId(user_id):
            return "вы уже записаны на курс"
        if self.is_student_recordered(number):
            return "студент с таким номером зачётки записан на курс"

        try:
            self.db.execute_insert(insert_sql)
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass

        return "вы успешно записаны на курсе"









        


