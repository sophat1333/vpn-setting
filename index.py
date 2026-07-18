import telebot
from telebot import types

# ដាក់ API Token របស់អ្នកនៅទីនេះ
TOKEN = '8969441391:AAGh-qN_nPR5AP1SVxBttiNHHx1R3Ii8u6Y'
bot = telebot.TeleBot(TOKEN)

# ---------------- បន្ថែមប៊ូតុង Menu Start នៅជាប់ប្រអប់ Chat ----------------
try:
    bot.set_my_commands([
        types.BotCommand('start', 'ទំព័រដើម / Main Menu')
    ])
    print("បានកំណត់ប៊ូតុង Menu Start ជោគជ័យ!")
except Exception as e:
    print(f"មិនអាចកំណត់ប៊ូតុង Menu បានទេ៖ {e}")

# -------------------------------------------------------------------

# 1. នៅពេល User វាយពាក្យ /start វានឹងបង្ហាញ Main Menu
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    # បង្កើតប៊ូតុងធំៗ
    btn_android = types.KeyboardButton('Sitting Android 🤖')
    btn_ios = types.KeyboardButton('Sitting IOS 📱')
    btn_dpi = types.KeyboardButton('របៀបដាក់ DPI 💀')

    markup.add(btn_android, btn_ios)
    markup.add(btn_dpi)

    bot.send_message(message.chat.id, "🔝 Main Menu", reply_markup=markup)


# 2. នៅពេល User ចុចប៊ូតុង "Sitting IOS 📱"
@bot.message_handler(func=lambda message: message.text == 'Sitting IOS 📱')
def send_ios_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    # បន្ថែមប៊ូតុង IPhone 7 និង IPhone X ទៅក្នុង Menu
    btn_i7 = types.KeyboardButton('IPhone 7')
    btn_ix = types.KeyboardButton('IPhone X')
    btn1 = types.KeyboardButton('IPhone 14')
    btn2 = types.KeyboardButton('IPhone 13 ProMax')
    btn3 = types.KeyboardButton('IPhone 14 Plus')
    btn4 = types.KeyboardButton('IPhone 14 Pro')
    btn5 = types.KeyboardButton('IPhone 15')
    btn6 = types.KeyboardButton('IPhone 14 ProMax')
    btn_back = types.KeyboardButton('🔙 ត្រឡប់ក្រោយ')

    markup.add(btn_i7, btn_ix)
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup.add(btn_back)

    bot.send_message(message.chat.id, "សូមជ្រើសរើសម៉ូដែល iPhone របស់អ្នក៖", reply_markup=markup)


# 3. ប៊ូតុងសម្រាប់ត្រឡប់ទៅ Main Menu វិញ
@bot.message_handler(func=lambda message: message.text == '🔙 ត្រឡប់ក្រោយ')
def back_to_main(message):
    send_welcome(message)


# 4. កន្លែងទទួលបញ្ជា និងផ្ញើ Setting ទៅតាមម៉ូដែល iPhone នីមួយៗ (លុបរូបភាពចេញហើយ)
@bot.message_handler(
    func=lambda message: message.text in ['IPhone 7', 'IPhone X', 'IPhone 13 ProMax', 'IPhone 14',
                                          'IPhone 14 Plus', 'IPhone 14 Pro', 'IPhone 14 ProMax', 'IPhone 15'])
def send_iphone_settings(message):
    selected_phone = message.text

    # បង្កើត markup ឡើងវិញដើម្បីរក្សាប៊ូតុងម៉ូដែលទូរស័ព្ទកុំឱ្យបាត់
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn_i7 = types.KeyboardButton('IPhone 7')
    btn_ix = types.KeyboardButton('IPhone X')
    btn1 = types.KeyboardButton('IPhone 14')
    btn2 = types.KeyboardButton('IPhone 13 ProMax')
    btn3 = types.KeyboardButton('IPhone 14 Plus')
    btn4 = types.KeyboardButton('IPhone 14 Pro')
    btn5 = types.KeyboardButton('IPhone 15')
    btn6 = types.KeyboardButton('IPhone 14 ProMax')
    btn_back = types.KeyboardButton('🔙 ត្រឡប់ក្រោយ')

    markup.add(btn_i7, btn_ix)
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    markup.add(btn_back)

    caption_text = ""

    # ------------------ កំណត់តែអត្ថបទ (Text) ប៉ុណ្ណោះ ------------------
    if selected_phone == 'IPhone 7':
        caption_text = """Sitting Free Fire 🔥 
👉 Iphone 7 ✅

200
140
166
150
125
100

កន្លែងបាញ់ 50% ឫ 40%

DPI 100 ឫ 120 ✅ 👿"""

    elif selected_phone == 'IPhone X':
        caption_text = """Sitting Free Fire 🔥 
👉 Iphone X ✅

200
120
166
130
130
0

កន្លែងបាញ់ 50% ឫ 45%

DPI 120 ✅ 👿"""

    elif selected_phone == 'IPhone 13 ProMax':
        caption_text = """Sitting Free Fire 🔥 
👉 Iphone 13 Pro Max ✅

170
140
166
159
125
100

កន្លែងបាញ់ 50% ឫ 40%

DPI 90 ✅ 👿"""

    elif selected_phone == 'IPhone 14':
        caption_text = """Sitting Free Fire 🔥
👉 Iphone 14 ✅

180
150
160
150
130
100

កន្លែងបាញ់ 45%

DPI 100 ✅ 😈"""

    elif selected_phone == 'IPhone 14 Plus':
        caption_text = """Sitting Free Fire 🔥
👉 Iphone 14 Plus ✅

120
110
200
135
182
196

DPI 90 🔥 😈"""

    elif selected_phone == 'IPhone 14 Pro':
        caption_text = """Sitting Free Fire 🔥
👉 Iphone 14 Pro ✅

190
160
170
160
140
100

កន្លែងបាញ់ 40%

DPI 110 ✅ 😈"""

    elif selected_phone == 'IPhone 14 ProMax':
        caption_text = """Sitting Free Fire 🔥
👉 Iphone 14 Pro Max ✅

120
110
200
135
182
196

DPI 90 🔥 😈"""

    elif selected_phone == 'IPhone 15':
        caption_text = """Sitting Free Fire 🔥
👉 Iphone 15 ✅

200
170
180
170
150
100

កន្លែងបាញ់ 38%

DPI 120 ✅ 😈"""

    # បញ្ជាឲ្យ Bot ផ្ញើតែសារអក្សរ ដោយរក្សាប៊ូតុងឲ្យនៅដដែល
    bot.send_message(message.chat.id, caption_text, reply_markup=markup)


# 5. ប៊ូតុង Android និង DPI
@bot.message_handler(func=lambda message: message.text == 'Sitting Android 🤖')
def send_android_info(message):
    bot.send_message(message.chat.id, "ទិន្នន័យសម្រាប់ Android កំពុងរៀបចំ...")


@bot.message_handler(func=lambda message: message.text == 'របៀបដាក់ DPI 💀')
def send_dpi_info(message):
    bot.send_message(message.chat.id, "របៀបដាក់ DPI...")


# ដំណើរការ Bot កុំឱ្យរលត់
print("Bot កំពុងដំណើរការ...")
bot.infinity_polling()
