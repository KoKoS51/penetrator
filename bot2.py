import requests #импортируем библиотеку для работы с http сервисами
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг
#print(config["Telega"]["token"])

def send_msg(text): # определяем функцию с одним входным аргументом
   token = str(config["Telega"]["token"]) # обьявляем переменную содержащую токен для бота
   chat_id = str(config["Telega"]["chat_id"]) #обьявляем переменную содержащую ID канала
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text #обьявляем переменную в которой с конкатенацией указываем полную ссылку
   results = requests.get(url_req) #обьявляем переменную с результатом вызова библиотеки
   print(str(results.json())) #выводим результат предыдущей переменной на экран

send_msg("❌") #вызываю функцию с входным аргументом
send_msg("Шалом мои необрезанные") #вызываю функцию с входным аргументом