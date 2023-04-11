
from itertools import count
import telebot
import helper, csv

bot = telebot.TeleBot('PUT_YOUR_KEY_HERE');
datafile = 'data/usersAndWords.csv'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я тута!')

@bot.message_handler(commands=["members"])
def members(m, res=False):
    bot.send_message(m.chat.id, 'В чате ' + str(bot.get_chat_member_count(m.chat.id) - 1) + ' участника(ов)')

@bot.message_handler(commands=["me"])
def me(m, res=False):
    isSent = False
    with open(datafile, 'r', encoding='UTF8') as read_df:
        reader = csv.reader(read_df, delimiter=',')
        for row in reader:
            if row[0] == m.from_user.username:
                bot.send_message(m.chat.id,
                f'Вот твоя статистика, {row[1]}!\n\nСообщений: {row[2]}\nСлов: {row[3]}\nМатных слов: {row[4]}\n')
                isSent = True
        if not isSent:
            bot.send_message(m.chat.id, f'{m.from_user.first_name}, для тебя пока нет статистики :(')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    new_dataset = []
    tg_username = message.from_user.username
    tg_firstName = message.from_user.first_name
    print(message.from_user.first_name + ' написал: ' + message.text +
    '\nМатных слов в его сообщении: ' + str(helper.countBadWords(message.text)))
    new_dataset.extend([tg_username, tg_firstName, 1, helper.countWords(message.text), helper.countBadWords(message.text)])
    if not(helper.findUserData(tg_username)):
        helper.addUserData(new_dataset)
    else:
        helper.updateUserData(new_dataset)


bot.polling(none_stop=True, interval=0)