import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


vk_session = vk_api.VkApi(token="vk1.a.K6eYXuEK8BY8qUaVGLIksmTeSYjgmkcDhllTUT58MrmIusZF1xFqeEn62C496gpojPfE67FKDFQrWmQfqecOZv68a3FYtCAEj3zGB-lz6kc-V4Lozuv8cMQ0Hznn0k8fZJU5Coh1l1Fdy7NO6uXcacg3sGzo38Idk_OUWfJSjTCKt0IiEf818TlmCrYUXBMp")
vk = vk_session.get_api()
longpool = VkLongPoll(vk_session)

start = VkKeyboard(one_time=True)
start.add_button('Начать', color=VkKeyboardColor.POSITIVE)
# start

title = VkKeyboard(one_time=True)
title.add_button('Ozon', color=VkKeyboardColor.SECONDARY)
title.add_button('WB', color=VkKeyboardColor.SECONDARY)
title.add_line()
title.add_button('Меню', color=VkKeyboardColor.POSITIVE)
# title

menu = VkKeyboard(one_time=True)
menu.add_button('WB и Ozon', color=VkKeyboardColor.POSITIVE)
menu.add_line()
menu.add_button('Админ', color=VkKeyboardColor.PRIMARY)
menu.add_line()
menu.add_button('Хочу тату по своему эскизу', color=VkKeyboardColor.SECONDARY)
# Menu


Ozon = VkKeyboard(one_time=True)
Ozon.add_button('Ozon', color=VkKeyboardColor.SECONDARY)
Ozon.add_button('WB', color=VkKeyboardColor.SECONDARY)
Ozon.add_line()
Ozon.add_button('Меню', color=VkKeyboardColor.PRIMARY)
# WBandOzon

admin = VkKeyboard(one_time=True)
admin.add_button('Оплата и доставка', color=VkKeyboardColor.SECONDARY)
admin.add_line()
admin.add_button('Вы не обманите?', color=VkKeyboardColor.SECONDARY)
admin.add_line()
admin.add_button('Меню', color=VkKeyboardColor.NEGATIVE)
# Admin

self = VkKeyboard(one_time=True)
self.add_button('Оформить заказ', color=VkKeyboardColor.POSITIVE)
self.add_line()
self.add_button('Прайс', color=VkKeyboardColor.SECONDARY)
self.add_button('Меню', color=VkKeyboardColor.SECONDARY)
# SelfTatoo

Zakaz = VkKeyboard(one_time=True)
Zakaz.add_button('Вызвать администратора', color=VkKeyboardColor.POSITIVE)
Zakaz.add_line()
Zakaz.add_button('Меню', color=VkKeyboardColor.SECONDARY)
# Zakaz

AdminVizvan = VkKeyboard(one_time=True)
AdminVizvan.add_button('Классные эскизы', color=VkKeyboardColor.SECONDARY)
AdminVizvan.add_line()
AdminVizvan.add_button('Меню', color=VkKeyboardColor.SECONDARY)
# AdminVizvan


settings = dict(one_time=False, inline=True)

def send_some_msg_kboard(id, some_text, kboard):
    vk.messages.send(peer_id=id,message=some_text,keyboard=kboard.get_keyboard(),random_id=0)

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            print(msg);
            if msg == "начать":
                send_some_msg_kboard(id, 'TATTS - бренд временных татуировок и накладных ноготочков. \r\n\r\n Мы есть на Ozon и Wildberries, тыкай меню, чтобы увидеть ссылки. \r\n\r\n Тут отвечает наш админ, а ещё подключен бот, для ответа на популярные вопросы. \r\n\r\n Запутаешься, пиши "Меню" ', title)

            if msg == "меню":
                send_some_msg_kboard(id,'Вызывай админстратора, если есть вопрос', menu)

            if msg == "wb и ozon":
                send_some_msg_kboard(id,'Бесплатная доставка за 1-3 дня по всей России О чём ещё можно мечтать? \r\n\r\n Ozon - \r\n\r\n Wildberries - ', Ozon)

            if msg == "админ":
                send_some_msg_kboard(id,'Что вас интересует? \r\n\r\n Опишите максимально подробно и ждите ответа. Наш администратор ждёт вашего вопроса.', admin)

            if msg == "хочу тату по своему эскизу":
                send_some_msg_kboard(id,'Как сделать заказ тату по своему эскизу? \r\n Создать свой эскиз - canva.com \r\n найти эскиз - pinterest.ru \r\n\r\n 1.Выбери эскиз \r\n 2.Подбери необходимый размер \r\n 3.Скинь эскизы в этот диалог \r\n 4.Оформи и оплати заказ\r\n 5.Жди свои татушечки\r\n\r\n Узнать цены - \r\nМинимальный заказ от 750руб.', self)

            if msg == "Оформить заказ":
                send_some_msg_kboard(id,'Скидывай эскизы с размерами. Затем тыкай на кнопку "вызвать администратора" \r\n\r\n Он поможет тебе оформить заказ', Zakaz)

            if msg == "Прайс":
                send_some_msg_kboard(id,'У нас шаблонные размеры. Если у вас будет нестандартный размер, то вы всё равно платите за ---- тату \r\n\r\n К примеру, 9x8см всё равно будет стоить 249руб. \r\n\r\n Мальенький(5x5) - 159руб. \r\n Средний(10x10) - 249руб.\r\n Большой(10x15) - 349руб.\r\n Широкий(5x15) - 199руб. \r\n Высокий(15x5) - 199руб. \r\n Очень большой(15x20) - 549уб.', Zakaz)

            if msg == "Вызвать администратора":
                send_some_msg_kboard(id,'Администратору пришло уведомление', Zakaz)

