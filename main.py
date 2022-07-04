import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


vk_session = vk_api.VkApi(token="vk1.a.K6eYXuEK8BY8qUaVGLIksmTeSYjgmkcDhllTUT58MrmIusZF1xFqeEn62C496gpojPfE67FKDFQrWmQfqecOZv68a3FYtCAEj3zGB-lz6kc-V4Lozuv8cMQ0Hznn0k8fZJU5Coh1l1Fdy7NO6uXcacg3sGzo38Idk_OUWfJSjTCKt0IiEf818TlmCrYUXBMp")
vk = vk_session.get_api()
longpool = VkLongPoll(vk_session)

keyboard = VkKeyboard(one_time=True)

keyboard.add_button('Отправить свое местоположение в ФБР', color=VkKeyboardColor.SECONDARY)
keyboard.add_line()
keyboard.add_button('Отправить свое местоположение в ФСБ', color=VkKeyboardColor.POSITIVE)
# Настройки для обоих клавиатур
settings = dict(one_time=False, inline=True)

def send_some_msg(id, some_text):
    vk.messages.send(peer_id=id,message=some_text,keyboard=keyboard.get_keyboard(),random_id=0)

def send_some_msg_kboard(id, some_text, kboard):
    vk.messages.send(peer_id=id,message=some_text,keyboard=kboard.get_keyboard(),random_id=0)

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            print(msg);
            if msg == "начать":
                send_some_msg(id, 'TATTS - бренд временных татуировок и накладных ноготочков. \r\n\r\n Мы есть на Ozon и Wildberries, тыкай меню, чтобы увидеть ссылки. \r\n\r\n Тут отчёт наш админ, а ещё подключен бот, для ответа на популярные вопросы. \r\n\r\n Запутаешься, пиши "Меню" ')
            else: send_some_msg_kboard(id,"Ну привет! Я бот! Хочешь, отправлю историю твоего браузера в правоохранительные органы?",keyboard)