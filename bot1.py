import requests #импортируем библиотеку для работы с http сервисами

def send_msg(text): # определяем функцию с одним входным аргументом
   token = "mytoken" # обьявляем переменную содержащую токен для бота
   chat_id = "-1001632111231" #обьявляем переменную содержащую ID канала
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text #обьявляем переменную в которой с конкатенацией указываем полную ссылку
   results = requests.get(url_req) #обьявляем переменную с результатом вызова библиотеки
   print(str(results.json())) #выводим результат предыдущей переменной на экран

send_msg("❌") #вызываю функцию с входным аргументом
send_msg("Шалом мои необрезанные") #вызываю функцию с входным аргументом