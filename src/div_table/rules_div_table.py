import random

words_operations = ['на', 'разделить на']


def start_text():
    return 'Привет! Я буду задавать вопросы на деление, а ты должен отвечать.\n' \
           'Всё просто!\n' \
           'Готов учить таблицу деления?'


def help_text():
    return 'Все просто! Я буду задавать вопросы, например "2 на 2", а ты должен ответить.\n' \
           'Я проверю!\n' \
           'Готов учить таблицу деления?'


def can_text():
    return 'Я умею задавать вопросы, например "2 на 2", а ты должен ответить.\n' \
           'Я проверю!\n' \
           'Готов учить таблицу деления?'


def div(q) -> str:
    return str(int(int(q[0]) / int(q[1])))


def question_text(q) -> str:
    return q[0] + ' ' + random.choice(words_operations) + ' ' + q[1]


def answer_text(q) -> str:
    return q[0] + ' ' + random.choice(words_operations) + ' ' + q[1] + ' ' + random.choice(words) + ' ' + div(q)
