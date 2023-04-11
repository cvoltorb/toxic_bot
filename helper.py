import re, csv

# Counts number of words in a message and returns it
def countWords(message):
    words = message.split()
    return(len(words))
    
# Counts numver of bad words in a message with based on predefined keywords[] list
# Returns number of words in a message
def countBadWords(message):
    badWords = []

    for keyWord in keyWords:
        badWords.extend(re.findall(keyWord, message))
    
    return len(badWords)

# Find user data in csv by username passed as "user"
# Returns a row from csv
# If row not find then returns "False"
def findUserData(username):
    with open(datafile, 'r', encoding='UTF8') as read_f:
        reader = csv.reader(read_f, delimiter=',')
        for row in reader:
            if not row:
                return
            if row[0] == username:
                return row
    return False

# Add new user with an approptiate data
def addUserData(dataset):
    with open(datafile, 'a', encoding='UTF8', newline='') as upd_f:
        updater = csv.writer(upd_f)
        updater.writerow(dataset)
    return

# Updates user data with provided dataset[]
def updateUserData(dataset):
    newrow = []
    # Open main datafile and temporary tempfile
    with (open(datafile, 'r', encoding='UTF8') as read_df,
        open(tempfile, 'a', encoding='UTF8', newline='') as upd_tf):
        reader_df = csv.reader(read_df, delimiter=',')
        updater_tf = csv.writer(upd_tf)
        # Write all data from main- to temp- file
        # If given user exists then write updated row to tempfile
        # Else write the row as is
        for row in reader_df:
            if not row:
                return
            if row[0] != dataset[0]:
                updater_tf.writerow(row)
            elif row[0] == dataset[0]:
                newrow = row
                for i in range(2, 5):
                    newrow[i] = int(newrow[i]) + dataset[i]
                updater_tf.writerow(newrow)
    # Open main- and temp- files to clean mainfile and write there all data from tempfile
    with (open(datafile, 'w', encoding='UTF8', newline='') as write_df,
        open(tempfile, 'r', encoding='UTF8', newline='') as read_tf):
        writer_df = csv.writer(write_df)
        reader_tf = csv.reader(read_tf, delimiter=',')
        for row in reader_tf:
            writer_df.writerow(row)
    # Open tempfile to clear it
    with open(tempfile, 'w', encoding='UTF8', newline='') as tmp:
        return

datafile = 'data/usersAndWords.csv'
tempfile = 'data/temp.csv'

fields = ['username', 'firstName', 'messages', 'words', 'badWords']

keyWords = ['[Пп][Ии][Зз][Дд]', '[Бб][Лл][Яя]', '[Сс][Уу][Кк]',
            '[Хх][Уу][Йй]', '[Дд][Оо][Лл][Бб][Оо][ЕЁеё]']