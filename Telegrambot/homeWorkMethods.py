from Model.Services.HomeWorkService import HomeWorkService
from Model.Services.StudentsService import StudentsService
from Model.Services.AdminService import AdminService

def get_all_hws(bot, id):
    studentService= StudentsService()
    homeWorkService = HomeWorkService()
    if not studentService.is_student_recordered_userId(id):
        bot.send_message(id, "Студент не записан")
    studentService.close()
    homelist = homeWorkService.get_all_hw()
    textmessage= ''
    for i in homelist:
        textmessage+= str(i[0])+' '+ str(i[1])+ ' '+ str(i[2])+ '\n'
    bot.send_message(id, textmessage)
   
    
#text - name description через пробел
def add_home_work(bot, user_id, text):
    adminService= AdminService()
    if not adminService.is_admin(user_id):
         bot.send_message(id, "не админ")
    adminService.close()
    hlist = text.split()

    homeworkService = HomeWorkService()
    message = homeworkService.add_hw(hlist[0], hlist[1])
    homeworkService.close()
    bot.send_message(id, message)
def is_admins(bot, id):
    adminService= AdminService()
    if not adminService.is_admin_recordered(id):
        bot.send_message(id, "Админ не записан")
    if not adminService.is_admin(id):
        bot.send_message(id, "Не прошел проверку на админа")
    bot.send_message(id, "Админ")
    adminService.close()
    
add_home_work(None,0,"ffdsfdsf ВПВПВПЫВПСМС")
#проверка на админа
