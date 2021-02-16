import vk_api
import telebot
import time
import traceback
import datetime
import random
bot = telebot.TeleBot("tgtoken") # ТГ нужен только для отладки!!!(Ошибки будет присылать туда, а не падать или засирать консоль сервера)
vk = vk_api.VkApi(token="vktoken")
def delete(ids):
	vk.method("messages.delete",{"message_ids":ids,"delete_for_all":1,})
def getone(count,peer_id):
	return vk.method("messages.getHistory", {"count":count,"user_id":551758635,"peer_id":peer_id})
def chlen(ids,from_id):
	usr = vk.method('users.get',{'fields':"first_name,screen_name","user_ids":from_id})[0]
	send_name = usr.get("first_name")
	send_scname = usr.get("screen_name")
	dlina = int(random.randint(0,40))
	rand = int(random.randint(1,1000))
	vk.method("messages.send",{"random_id":rand,"peer_id":2000000009,"message":"@"+send_scname+" ("+send_name+"), длина твоей бибы "+str(dlina)+" см.","reply_to":ids})
def butilka(ids,peer_id,from_id):
	usr = vk.method('users.get',{'fields':"first_name,screen_name","user_ids":from_id})[0]
	send_name = usr.get("first_name")
	send_scname = usr.get("screen_name")
	gCM = vk.method("messages.getConversationMembers",{"peer_id":2000000009})
	count = (int(gCM.get("count"))-2)
	rind = int(random.randint(0,count))
	user = gCM.get('profiles')[rind]
	nick = user.get('screen_name')
	ids = user.get('id')
	usr = vk.method('users.get',{'fields':"first_name,last_name","user_ids":ids,"name_case":"acc"})[0]
	fname = usr.get("first_name")
	lname = usr.get("last_name")
	randid = int(random.randint(0,1234))
	lovid = usr.get('id')
	sex = str(usr.get('sex'))
	if sex == "1":
		gender = "a"
	else:
		gender = ""
	if lovid == from_id:
		vk.method("messages.send",{"random_id":randid,"peer_id":2000000009,"message":"💋 @"+send_scname+" ("+send_name+")"+" поцелует сам"+str(gender)+" себя 💋"})
	else:
		vk.method("messages.send",{"random_id":randid,"peer_id":2000000009,"message":"💋 @"+send_scname+" ("+send_name+")"+" поцелует @"+nick+" ("+fname+" "+lname+") 💋"})
def sharick(ids):
	try:
		words = ["Бесспорно","Возможно.. но нет.","Конечно же да!","Я отвечу да, но тебе стоит самому обдумать решение","Это не самая лучшая твоя мысль..","Когда нибудь, но не сегодня","Да, определённо да.","Как в этом вообще можно сомневаться? Конечно же да!","Маловероятно, что это лучшая мысль, но да","В библии написано, что да", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется — «да»", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят — «да»", "Да", "Пока не ясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ — «нет»", "По моим данным — «нет»", "Перспективы не очень хорошие", "Весьма сомнительно"]
		unique_words = list(set(words))
		random.shuffle(unique_words)
		random.SystemRandom().shuffle(unique_words)
		rand = int(random.randint(1,1000))
		vk.method("messages.send",{"random_id":rand,"peer_id":2000000009,"message":"Бот сказал:"+str(unique_words[1]),"reply_to":ids})
	except Exception:
		bot.send_message(895942747,traceback.format_exc())
while True:
	try:
		php = getone(count = 1, peer_id	= 2000000009)
		peer_id = php.get("items")[0].get("peer_id")
		text = php.get("items")[0].get("text")
		att = php.get('items')[0].get('attachments')
		from_id = php.get('items')[0].get("from_id")
		ids = php.get("items")[0].get("id")
		ids = str(ids)
		text = text.lower()
		if text.lower() == "!шарик":
			sharick(ids)
		if text.lower() == "!бутылочка":
			butilka(ids,peer_id,from_id)
		if text.lower() == "!член":
			chlen(ids,from_id)
		#print(nowtime+"\nID Диалога: "+str(peer_id)+"\nТекст последнего сообщения: "+str(text)+"\nВложения: "+str(att)+"\nID Отправителя: "+str(from_id)+"\nID Сообщения: "+str(ids))
		time.sleep(0.5)
	except Exception:
		bot.send_message(895942747,traceback.format_exc())
