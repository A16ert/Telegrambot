from .BaseService import BaseService
import xlwt, xlrd, xlutils, sqlite3


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

    def absents(db):
        #conn = sqlite3.connect(db)
        #cursor = conn.cursor()
        sql = 'SELECT * FROM absents;'
        try:
             ab = self.db.execute_select(sql)
        # Counting attending classes
        #cursor.execute("SELECT * FROM absents")
        ab = self.db.execute_select(sql)
        #results = cursor.fetchall()
        # print(results)
        # print(type(results))
        plus = 0
        minus = 0
        groupVisitationDict = {}
        for tuple in st:
            for el in tuple:
                if el == '+':
                    plus += 1
                elif el == '-':
                    minus += 1
            groupVisitationDict.update({tuple[0]: {'+': plus, '-': minus}})
            minus = 0
            plus = 0

        
        # Count of Students
        cursor.execute("SELECT * FROM students")

        results = cursor.fetchall()
        st = self.db.execute_select(sql)
        studFIO = ''
        studentsDict = {}
        for tup in results:
            for i in range(1, len(tup)):
                studFIO += tup[i] + ' '
            studentsDict.update({tup[0]: studFIO})
            studFIO = ''

        # print(studentsDict)
        # End count of students

        # EXCEL writing
        f_name = 'absence.xlsx'
        wb = xlwt.Workbook()
        ws = wb.add_sheet('ABSENTS')
        sheet = wb._sheets[0]
        sheet['A1'] = 'Количество студентов на курсе:'
        k = 2
        for i in studentsDict:
            sheet['A' + str(k)] = i
            sheet['B' + str(k)] = studentsDict[i]
            k += 1

        k = 2
        # print(groupVisitationDict)
        sheet['C1'] = 'Прогулы курса:'
        for i in groupVisitationDict:
            sheet['C' + str(k)] = i
            for j in groupVisitationDict[i]:
                if j == '+':
                    sheet['D' + str(k)] = j
                    sheet['E' + str(k)] = groupVisitationDict[i][j]
                elif j == '-':
                    sheet['F' + str(k)] = j
                    sheet['G' + str(k)] = groupVisitationDict[i][j]
            k += 1

        try:
            wb.save(f_name)

        # End EXCEL writing

        return 'ok'
    pass
