import telebot
from telebot import types

bot = telebot.TeleBot("5921534942:AAFfSPhsUxA2azueW2oQPoiSZiT0PrIqfpc", parse_mode=None)

r = open("cards", "r")
line = r.readlines()
card1 = (line[0]) 
card2 = (line[1])
card3 = (line[2])
card4 = (line[3])
card5 = (line[4])
card6 = (line[5])

r.close

card1=float(card1)
card2=float(card2)
card3=float(card3)
card4=float(card4)
card5=float(card5)
card6=float(card6)

@bot.message_handler(commands=['help', 'start'])
def welcome(message):

    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("Перевести кошти", callback_data='per')
    item2 = types.InlineKeyboardButton("Подивитися баланс картки", callback_data='pod')


    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Що будемо робити?', reply_markup=markup)

@bot.message_handler(commands=['restart'])
def welcome(message):

    card1 = 1000
    card2 = 1000
    card3 = 1000
    card4 = 1000
    card5 = 1000
    card6 = 10000


    m = str(card1), "\n", str(card2),"\n", str(card3),"\n", str(card4),"\n", str(card5),"\n", str(card6)

    w = open("cards", "w")
    for t in m:
        w.write(t)

    w.close

    bot.send_message(message.chat.id, 'Все готово, баланс ваших карток - 1000')

    bot.send_message(message.chat.id, 'Напишіть пароль 1 картки, але щоб ніхто не побачив використвуюте ||  на початку та на кінці паролю,   наприклад: ||1234||')

    bot.send_message(message.chat.id, 'Якщо ж картка зайва, і нікому не належить, то напишіть - немає')

    r = open("perevody", "w")
    s = "1"                                          
    t = None
    for t in s:
        r.write(t)
    r.close

    r = open("enter_password", "w")
    s = "new_password"                                          
    t = None
    for t in s:
        r.write(t)
    r.close

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'per':
            
            markup1 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("1 картка", callback_data='1', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6', one_time_keyboard=True)

            markup1.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'З якої картки будемо переводити?', reply_markup=markup1)    

        if call.data == 'pod':

            markup2 = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("1 картка", callback_data='1p', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2p', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3p', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4p', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5p', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6p', one_time_keyboard=True)

            markup2.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'Якої картки хочете побачити рахунок?', reply_markup=markup2)   

        r = open("cards", "r")
        line = r.readlines()
        card1 = (line[0]) 
        card2 = (line[1])
        card3 = (line[2])
        card4 = (line[3])
        card5 = (line[4])
        card6 = (line[5])

        r.close

        card1=float(card1)
        card2=float(card2)
        card3=float(card3)
        card4=float(card4)
        card5=float(card5)
        card6=float(card6) 

        if call.data == '1p':
            bot.send_message(call.message.chat.id, card1)  
        if call.data == '2p':
            bot.send_message(call.message.chat.id, card2)  
        if call.data == '3p':
            bot.send_message(call.message.chat.id, card3)  
        if call.data == '4p':
            bot.send_message(call.message.chat.id, card4)  
        if call.data == '5p':
            bot.send_message(call.message.chat.id, card5)  
        if call.data == '6p':
            bot.send_message(call.message.chat.id, card6)  

        if call.data == '1':

            r = open("perevody", "w")
            s = call.data                                           
            t = None
            for t in s:
                r.write(t)
            r.close

            r = open("enter_password", "w")                                         
            r.write("1")
            r.close


            markup1 = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("1 картка", callback_data='1p1', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2p2', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3p3', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4p4', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5p5', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6p6', one_time_keyboard=True)


            markup1.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'На яку картку будемо переводити?', reply_markup=markup1)   

        if call.data == '2':
            r = open("perevody", "w")
            s = call.data
            t = None
            for t in s:
                r.write(t)
            r.close

            r = open("enter_password", "w")                                         
            r.write("2")
            r.close


            markup1 = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("1 картка", callback_data='1p1', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2p2', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3p3', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4p4', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5p5', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6p6', one_time_keyboard=True)


            markup1.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'На яку картку будемо переводити?', reply_markup=markup1)   

        if call.data == '3':
            r = open("perevody", "w")
            s = call.data
            t = None
            for t in s:
                r.write(t)
            r.close

            r = open("enter_password", "w")                                         
            r.write("3")
            r.close


            markup1 = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("1 картка", callback_data='1p1', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2p2', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3p3', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4p4', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5p5', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6p6', one_time_keyboard=True)


            markup1.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'На яку картку будемо переводити?', reply_markup=markup1)   

        if call.data == '4':
            r = open("perevody", "w")
            s = call.data
            t = None
            for t in s:
                r.write(t)
            r.close

            r = open("enter_password", "w")                                         
            r.write("4")
            r.close


            markup1 = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("1 картка", callback_data='1p1', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2p2', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3p3', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4p4', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5p5', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6p6', one_time_keyboard=True)


            markup1.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'На яку картку будемо переводити?', reply_markup=markup1)   

        if call.data == '5':
            r = open("perevody", "w")
            s = call.data
            t = None
            for t in s:
                r.write(t)
            r.close

            r = open("enter_password", "w")                                         
            r.write("5")
            r.close


            markup1 = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("1 картка", callback_data='1p1', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2p2', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3p3', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4p4', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5p5', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6p6', one_time_keyboard=True)


            markup1.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'На яку картку будемо переводити?', reply_markup=markup1)   

        if call.data == '6':
            r = open("perevody", "w")
            s = call.data
            t = None
            for t in s:
                r.write(t)
            r.close


            markup1 = types.InlineKeyboardMarkup(row_width=2)

            item1 = types.InlineKeyboardButton("1 картка", callback_data='1p1', one_time_keyboard=True)
            item2 = types.InlineKeyboardButton("2 картка", callback_data='2p2', one_time_keyboard=True)
            item3 = types.InlineKeyboardButton("3 картка", callback_data='3p3', one_time_keyboard=True)
            item4 = types.InlineKeyboardButton("4 картка", callback_data='4p4', one_time_keyboard=True)
            item5 = types.InlineKeyboardButton("5 картка", callback_data='5p5', one_time_keyboard=True)
            item6 = types.InlineKeyboardButton("Банківський рахунок", callback_data='6p6', one_time_keyboard=True)


            markup1.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(call.message.chat.id, 'На яку картку будемо переводити?', reply_markup=markup1)   

        if call.data == '1p1':
            r = open("perevody", "a")
            s = " ", '1'
            t = None
            for t in s:
                r.write(t)
            r.close
            bot.send_message(call.message.chat.id, "Для переводу напишіть пароль картки з якої переводите кошти:")  
        if call.data == '2p2':
            r = open("perevody", "a")
            s = " ", '2'
            t = None
            for t in s:
                r.write(t)
            r.close
            bot.send_message(call.message.chat.id, "Для переводу напишіть пароль картки з якої переводите кошти:")  
        if call.data == '3p3':
            r = open("perevody", "a")
            s = " ", '3'
            t = None
            for t in s:
                r.write(t)
            r.close
            bot.send_message(call.message.chat.id, "Для переводу напишіть пароль картки з якої переводите кошти:")  
        if call.data == '4p4':
            r = open("perevody", "a")
            s = " ", '4'
            t = None
            for t in s:
                r.write(t)
            r.close
            bot.send_message(call.message.chat.id, "Для переводу напишіть пароль картки з якої переводите кошти:")  
        if call.data == '5p5':
            r = open("perevody", "a")
            s = " ", '5'
            t = None
            for t in s:
                r.write(t)
            r.close
            bot.send_message(call.message.chat.id, "Для переводу напишіть пароль картки з якої переводите кошти:")  
        if call.data == '6p6':
            r = open("perevody", "a")
            s = " ", '6'
            t = None
            for t in s:
                r.write(t)
            r.close
            bot.send_message(call.message.chat.id, "Для переводу напишіть пароль картки з якої переводите кошти:")  
 
@bot.message_handler(content_types=['text'])
def buttons(message):


    r = open("perevody", "r")
    t = r.read(10)
    t = t.split(" ")
    r.close

    r = open("enter_password", "r")
    p = r.read(20)
    p = p.split(" ")
    r.close

    if p[0] == "Ok":
        r = open("perevody", "a")
        s = " ", message.text
        t = None
        for t in s:
            r.write(t)
        r.close

    if p[0] == "1":

        r = open("passwords", "r")
        line = r.readlines()
        password_1ok = (line[0]) 
        password_2ok = (line[1])
        password_3ok = (line[2])
        password_4ok = (line[3])
        password_5ok = (line[4])
        r.close

        if message.text[0] == password_1ok[0]:
        
            r = open("enter_password", "w")                                         
            r.write("Ok")
            r.close

            bot.send_message(message.chat.id, "Скільки коштів ви бажаєте перевести?")  
        else:
            bot.send_message(message.chat.id, "Пароль не вірний!")  
        
    elif p[0] == "2":

            r = open("passwords", "r")
            line = r.readlines()
            password_1ok = (line[0]) 
            password_2ok = (line[1])
            password_3ok = (line[2])
            password_4ok = (line[3])
            password_5ok = (line[4])
            r.close

            if message.text[0] == password_2ok[0]:
            
                r = open("enter_password", "w")                                         
                r.write("Ok")
                r.close

                bot.send_message(message.chat.id, "Скільки коштів ви бажаєте перевести?")  
            else:
                bot.send_message(message.chat.id, "Пароль не вірний!")  


    elif p[0] == "3":

            r = open("passwords", "r")
            line = r.readlines()
            password_1ok = (line[0]) 
            password_2ok = (line[1])
            password_3ok = (line[2])
            password_4ok = (line[3])
            password_5ok = (line[4])
            r.close
            print(password_1ok)
            print(message.text)

            if message.text[0] == password_3ok[0]:
            
                r = open("enter_password", "w")                                         
                r.write("Ok")
                r.close

                bot.send_message(message.chat.id, "Скільки коштів ви бажаєте перевести?")  
            else:
                bot.send_message(message.chat.id, "Пароль не вірний!")  
            
    elif p[0] == "4":

            r = open("passwords", "r")
            line = r.readlines()
            password_1ok = (line[0]) 
            password_2ok = (line[1])
            password_3ok = (line[2])
            password_4ok = (line[3])
            password_5ok = (line[4])
            r.close
            print(password_1ok)
            print(message.text)

            if message.text[0] == password_4ok[0]:
            
                r = open("enter_password", "w")                                         
                r.write("Ok")
                r.close

                bot.send_message(message.chat.id, "Скільки коштів ви бажаєте перевести?")  
            else:
                bot.send_message(message.chat.id, "Пароль не вірний!")  
        
    elif p[0] == "5":

            r = open("passwords", "r")
            line = r.readlines()
            password_1ok = (line[0]) 
            password_2ok = (line[1])
            password_3ok = (line[2])
            password_4ok = (line[3])
            password_5ok = (line[4])
            r.close
            print(password_1ok)
            print(message.text)

            if message.text[0] == password_5ok[0]:
            
                r = open("enter_password", "w")                                         
                r.write("Ok")
                r.close

                bot.send_message(message.chat.id, "Скільки коштів ви бажаєте перевести?")  
            else:
                bot.send_message(message.chat.id, "Пароль не вірний!")     

    if len(t)>1 and p[0] == "Ok":

        r = open("perevody", "a")
        s = " ", message.text
        t = None
        for t in s:
            r.write(t)
        r.close

        r = open("cards", "r")
        line = r.readlines()
        card1 = (line[0]) 
        card2 = (line[1])
        card3 = (line[2])
        card4 = (line[3])
        card5 = (line[4])
        card6 = (line[5])

        r.close

        card1=float(card1)
        card2=float(card2)
        card3=float(card3)
        card4=float(card4)
        card5=float(card5)
        card6=float(card6)
            
        r = open("perevody", "r")
        t = r.read(10)
        t = t.split(" ")

        a = t[0]
        b = t[1]
        c = t[2]
        r.close


        if(a == '1'):
            if card1 - int(c)>=0:
                card1 = card1 - int(c)
            else:
                bot.reply_to(message, "недостатньо грошей!")

                exit()
        elif(a == '2'):
            if card2 - int(c)>=0:
                card2 = card2 - int(c)
            else:
                bot.reply_to(message, "недостатньо грошей!")
        
                exit()
        elif(a == '3'):
            if card3 - int(c)>=0:
                card3 = card3 - int(c)
            else:
                bot.reply_to(message, "недостатньо грошей!")
            
                exit()
        elif(a == '4'):
            if card4 - int(c)>=0:
                card4 = card4 - int(c)
            else:
                bot.reply_to(message, "недостатньо грошей!")
        
                exit()
        elif(a == '5'):
            if card5 - int(c)>=0:
                card5 = card5 - int(c)
            else:
                bot.reply_to(message, "недостатньо грошей!")
    
                exit()
        elif(a == '6'):
            if card6 - int(c)>=0:
                card6 = card6 - int(c)
            else:
                bot.reply_to(message, "недостатньо грошей!")

                exit()
        
        if(b == '1'):
            card1 = card1 + int(c)

            bot.reply_to(message, "Переведено успішно!")
        elif(b == '2'):
            card2 = card2 + int(c)

            bot.reply_to(message, "Переведено успішно!")
        elif(b == '3'):
            card3 = card3 + int(c)

            bot.reply_to(message, "Переведено успішно!")
        elif(b == '4'):
            card4 = card4 + int(c)

            bot.reply_to(message, "Переведено успішно!")
        elif(b == '5'):
            card5 = card5 + int(c)

            bot.reply_to(message, "Переведено успішно!")
        elif(b == '6'):
            card6 = card6 + int(c)

            bot.reply_to(message, "Переведено успішно!")
        else:
            print("друга картка не правильна")
            quit()

        m = str(card1), "\n", str(card2),"\n", str(card3),"\n", str(card4),"\n", str(card5),"\n", str(card6)

        w = open("cards", "w")
        for t in m:
            w.write(t)

        w.close    

    

    elif p[0] == "new_password":

        if t[0] == "1":

            if message.text == "немає":

                bot.send_message(message.chat.id, 'Гаразд!')

            else:

                password_1 = message.text

                bot.send_message(message.chat.id, 'Напишіть пароль 2 картки:')

                g = open("passwords", "w")
                j = None
                for j in password_1:
                    g.write(j)
                g.close

                r = open("perevody", "w")
                s = "2"                                          
                t = None
                for t in s:
                    r.write(t)
                r.close

        elif t[0] == "2":

            if message.text == "немає":

                bot.send_message(message.chat.id, 'Гаразд!')

            else:

                password_2 = message.text

                bot.send_message(message.chat.id, 'Напишіть пароль 3 картки:')

                r = open("passwords", "r")
                t = r.read(10)
                r.close

                password_2 = t, '\n', str(password_2)

                g = open("passwords", "w")
                j = None
                for j in password_2:
                    g.write(j)
                g.close

                r = open("perevody", "w")
                s = "3"                                          
                t = None
                for t in s:
                    r.write(t)
                r.close


        elif t[0] == "3":

            if message.text == "немає":

                bot.send_message(message.chat.id, 'Гаразд!')

            else:

                password_3 = message.text

                bot.send_message(message.chat.id, 'Напишіть пароль 4 картки:')

                r = open("passwords", "r")
                t = r.read(20)
                r.close

                password_3 = t, '\n', str(password_3)

                g = open("passwords", "w")
                j = None
                for j in password_3:
                    g.write(j)
                g.close

                r = open("perevody", "w")
                s = "4"                                          
                t = None
                for t in s:
                    r.write(t)
                r.close

        elif t[0] == "4":

            if message.text == "немає":

                bot.send_message(message.chat.id, 'Гаразд!')

            else:

                pass4 = message.text

                bot.send_message(message.chat.id, 'Напишіть пароль 5 картки:')

                r = open("passwords", "r")
                t = r.read(30)
                r.close

                pass4 = t, '\n', pass4

                r = open("passwords", "w")
                t = None
                for t in pass4:
                    r.write(t)
                r.close

                r = open("perevody", "w")
                s = "5"                                          
                t = None
                for t in s:
                    r.write(t)
                r.close

        elif t[0] == "5":

            if message.text == "немає":

                bot.send_message(message.chat.id, 'Гаразд!')

            else:

                password_5 = message.text

                bot.send_message(message.chat.id, 'Дякую, можете починати!')

                r = open("passwords", "r")
                t = r.read(40)
                
                r.close

                password_5 = t, '\n', password_5

                r = open("passwords", "w")
                t = None
                for t in password_5:
                    r.write(t)
                r.close

                r = open("perevody", "w")
                r.write("nothihg")
                r.close




bot.polling()