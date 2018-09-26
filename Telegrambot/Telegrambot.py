from Model.Services.StudentsService import StudentsService
import telebot
from Helpers import Config
from Helpers import Commands

bot = telebot.TeleBot(Config.token)

@bot.message_handler(content_types=["text"], commands=['start', 'help','adminreg','adminunreg', 'signup', 'signout', 'default', 'loadratings', 'loadabsents',
                               'loadstudents', 'loadhws', 'getstudents', 'gethws', 'getratings', 'getabsents', 'addhw',
                               'delhw', "addstudent", "delstudent", 'hws', 'absents', "allhws", "showstudents",
                               "showhws", "showratings", "showabsents", 'getchats', 'getconfig', 'loadconfig', 'ask',
                               'channel', 'getask', 'answer', 'delask', 'analysis'])
def command_handler(message):
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

            if command == 'help':
                help_command(bot, user_id, text)

            if command == 'signup':
                signup_student_command(bot, user_id, text)
            pass

    except Exception as ex:
        bot.send_message(user_id, 'Произошла ошибка: ' + str(ex))
        print(ex)
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









if __name__ == '__main__':
    bot.polling(none_stop=True)