from .BaseService import BaseService
import xlwt, xlrd, xlutils


class ExcelService(BaseService):
    """description of class"""

    def __init__(self):
       BaseService.__init__(self)
       pass

    def get_all_home_works(self):

        sql = 'SELECT * FROM homeworks;'
        try:
            hw = self.db.execute_select(sql)
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass
            
        if len(hw) < 1: return 'нет домашних работ'

        font0 = xlwt.Font()
        font0.name = 'Times New Roman'
        font0.colour_index = 2
        font0.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font0

        style1 = xlwt.XFStyle()
        style1.num_format_str = 'DD-MM-YY'

        wb = xlwt.Workbook()
        ws = wb.add_sheet('HOMEWORKS')

        
        ws.write(0, 0, 'Id', style0)
        ws.write(0, 1, 'Name', style0)
        ws.write(0, 2, 'Description', style0)
        i = 1
        for home in hw:
            ws.write(i, 0, home[0], style0)
            ws.write(i, 1, home[1], style0)
            ws.write(i, 2, home[2], style0)
            i += 1
            pass
        try:
            wb.save('allhomeworks.xls')
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass
        return 'ok'
    pass

    def get_all_students(self):

        sql = 'SELECT * FROM students;'
        try:
            st = self.db.execute_select(sql)
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass
            
        if len(st) < 1: return 'нет студентов'

        font0 = xlwt.Font()
        font0.name = 'Times New Roman'
        font0.colour_index = 2
        font0.bold = True

        style0 = xlwt.XFStyle()
        style0.font = font0

        style1 = xlwt.XFStyle()
        style1.num_format_str = 'DD-MM-YY'

        wb = xlwt.Workbook()
        ws = wb.add_sheet('STUDENTS')

 
        ws.write(0, 0, 'Number', style0)
        ws.write(0, 1, 'Surname', style0)
        ws.write(0, 1, 'Firsf Name', style0)
        ws.write(0, 2, 'Middle Name', style0)
  
        i = 1
        for stud in st:
            ws.write(i, 0, st[0], style0)
            ws.write(i, 1, st[1], style0)
            ws.write(i, 2, st[2], style0)
            ws.write(i, 3, st[3], style0)
            i += 1
            pass
        try:
            wb.save('allStudents.xls')
        except Exception as ex:
            return 'Произошла ошибка: ' + str(ex)
            print(ex)
            pass
        return 'ok'
    pass


        
     

