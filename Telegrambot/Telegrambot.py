from Model.Services.StudentsService import StudentsService
from Model.Services.AdminService import AdminService
import telebot
import ExcelMethods
import homeWorkMethods
from Helpers import Config
from Helpers import Commands

bot = telebot.TeleBot(Config.token)
admin_command = ""

@bot.message_handler(content_types=["text"], commands=['start', 'help','adminreg','adminunreg', 'signup', 'signout', 'default', 'loadratings', 'loadabsents',
                               'loadstudents', 'loadhws', 'getstudents', 'gethws', 'getratings', 'getabsents', 'addhw',
                               'delhw', "addstudent", "delstudent", 'hws', 'absents', "allhws", "showstudents",
                               "showhws", "showratings", "showabsents", 'getchats', 'getconfig', 'loadconfig', 'ask',
                               'channel', 'getask', 'answer', 'delask', 'analysis'])
def command_handler(message):
    global admin_command
    chat = message.chat
    user_id = str(chat.id)
    command = (message.text[1:]).split(' ')[0]
    text = message.text[2 + len(command):].strip()
    try:
        if chat.type == 'private':
            if command == 'start':
                bot.send_message(user_id, 'Доступные команды:')
                commands = ""
                for a in Commands.commands_dict['guest'].items():
                    commands += '{} - {}\n'.format(a[0], a[1])
                    pass
                bot.send_message(user_id, commands)
                pass

            elif command == 'help':
                help_command(bot, user_id, text)

            elif command == 'signup':
                signup_student_command(bot, user_id, text)

            elif command == 'adminreg':
                admin_reg_command(bot, user_id, text)
            elif command == 'adminunreg':
                admin_unreg_command(bot, user_id, text)

            elif command == 'getstudents':
                admin_command = "getstudents"
                bot.send_message(user_id, "excel или message ?(yes/not)")
                #get_students_excel(bot, user_id)

            elif command == 'allhws':
                admin_command = 'allhws'
                bot.send_message(user_id, "excel или message ?(yes/not)")

            elif command == 'getstudents':
                ExcelMethods.get_student_list(bot, user_id)

    except Exception as ex:
        bot.send_message(user_id, 'Произошла ошибка: ' + str(ex))
        print(ex)
        pass
    pass

@bot.message_handler(content_types=["text"])
def text_handler(message):
    global admin_command
    chat = message.chat
    user_id = str(chat.id)
    text = message.text
    try:
        if admin_command == '':
            bot.send_message(user_id, "введите команду")
        elif admin_command == 'getstudents':
            if text == 'yes': get_students_excel(bot, user_id)
            else: get_students(bot, user_id)

        elif admin_command == 'allhws':
            if text == 'yes': ExcelMethods.get_all_home_works(bot, user_id)
            else: HomeWorksMethods.get_all_hws(bot, user_id)
        admin_command = ""
        pass
    except Exception as ex:
        bot.send_message(user_id, 'Произошла ошибка: ' + str(ex))
        print(ex)
        admin_command = ""
        pass
    pass
def help_command(bot, userId, text):

   studentsService = StudentsService()
   user = studentsService.get_student_by_userId(userId)
   studentsService.close

   commands = ""
   if user == None:
       for a in Commands.commands_dict['guest'].items():
            commands += '{} - {}\n'.format(a[0], a[1])
            pass
   elif user[0] != "0":
       for a in Commands.commands_dict['student'].items():
            commands += '{} - {}\n'.format(a[0], a[1])
            pass

   elif user[0] == "0":
       for a in Commands.commands_dict['admin'].items():
            commands += '{} - {}\n'.format(a[0], a[1])
            pass
       pass

   bot.send_message(userId, commands)
   pass

def signup_student_command(bot, userId, text):

    studentsService = StudentsService()
    
    user = text.split()
    if len(user) < 4:
        bot.send_message(userId, "Вы ввели недостаточно данных")
        return

    messageText = studentsService.add_student(user[0], user[1], user[2], user[3], userId)
    bot.send_message(userId, messageText)

    studentsService.close()

def admin_reg_command(bot, user_id, text):

    adminService = AdminService()

    if text == "": 
        bot.send_message(user_id, "Вы не ввели пароль")
        return

    if text == "12345":
        messageText = adminService.add_admin(user_id)

    bot.send_message(user_id, messageText)

    adminService.close()
    pass

def get_students(bot, user_id):

    studnetService = StudentsService()
    students = studnetService.get_all_students()
    studnetService.close()

    is_admin = False
    for i in students:
        if i[0] == '0':
            if i[4] == user_id: is_admin = True

    if not is_admin:
        bot.send_message(user_id, "вы не являетесь администратором")
        return

    if len(students) == 0:
        bot.send_message(user_id, "на данном курсе нет студентов" )
        return
    messageText = ""

    for i in students:
        messageText += i[0] +" " + i[1] + " " +i[2] +" " + i[3] + "\n"

    bot.send_message(user_id, messageText)

def get_students_excel(bot, user_id):
    ExcelMethods.get_student_list(bot, user_id)

def admin_unreg_command(bot, user_id, text):
    
    adminService = AdminService()

    if text == "": 
        bot.send_message(user_id, "Вы не ввели пароль")
        return
    messageText = ""
    if text == "12345":
        messageText = adminService.delete_admin()

    bot.send_message(user_id, messageText)

    adminService.close()
    pass










if __name__ == '__main__':
    bot.polling(none_stop=True)