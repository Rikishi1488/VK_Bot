import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.K6eYXuEK8BY8qUaVGLIksmTeSYjgmkcDhllTUT58MrmIusZF1xFqeEn62C496gpojPfE67FKDFQrWmQfqecOZv68a3FYtCAEj3zGB-lz6kc-V4Lozuv8cMQ0Hznn0k8fZJU5Coh1l1Fdy7NO6uXcacg3sGzo38Idk_OUWfJSjTCKt0IiEf818TlmCrYUXBMp")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id

            if msg == "Начать":
                send_some_msg(id, 'TATTS - бренд временных татуировок и накладных ноготочков. \r\n Мы есть на Ozon и Wildberries, тыкай меню, чтобы увидеть ссылки. \r\n Тут отчёт наш админ, а ещё подключен бот, для ответа на популярные вопросы. \r\n Запутаешься, пиши "Меню" ')

