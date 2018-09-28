from Model.Services.ExcelService import ExcelService
from Model.Services.AdminService import AdminService

def get_all_home_works(bot, id):
    exService = ExcelService()
    adminService = AdminService()

    if not adminService.is_admin(id): 
        bot.send_message(id, "вы не являетесь администратором")
        return
    adminService.close()
    message = exService.get_all_home_works()
    exService.close()
    if message == "ok":
        doc = open('allhomeworks' + '.xls', 'rb')
        bot.send_document(id, doc)
    else: bot.send_message(id, message)

    pass

def get_all_students(bot, self):
        exService = ExcelService()
        adminService = AdminService()

        if not adminService.is_admin(id): 
            bot.send_message(id, "вы не являетесь администратором")
            return
        adminService.close()
        message = exService.get_all_students()
        exService.close()
        if message == "ok":
            doc = open('allStudents' + '.xls', 'rb')
            bot.send_document(id, doc)
        else: bot.send_message(id, message)

        pass        

        return None

def get_absent_students(bot, self):
        exService = ExcelService()
        adminService = AdminService()

        if not adminService.is_admin(id): 
            bot.send_message(id, "вы не являетесь администратором")
            return
        adminService.close()
        message = exService.get_all_students()
        exService.close()
        if message == "ok":
            doc = open('absence' + '.xls', 'rb')
            bot.send_document(id, doc)
        else: bot.send_message(id, message)

        pass        

        return None

#####################################################################################


