import random
import re

praises = ['Верно', 'Всё верно', 'Ты прав', 'Да, это так']
errors = ['Это не правильно', 'Тут ты не прав', 'Ошибка']

words_operations = ['на', 'умножить на']
words = ['равно', 'будет']


def start_text():
    return 'Привет! Я буду задавать вопросы на умножение, а ты должен отвечать.\n' \
           'Всё просто!\n' \
           'Готов учить таблицу умножения?'


def help_text():
    return 'Все просто! Я буду задавать вопросы, например "2 на 2", а ты должен ответить.\n' \
           'Я проверю!\n' \
           'Готов учить таблицу умножения?'


def can_text():
    return 'Я умею задавать вопросы, например "2 на 2", а ты должен ответить.\n' \
           'Я проверю!\n' \
           'Готов учить таблицу умножения?'


def mul(q) -> str:
    """
    произведение
    :param q: массив, первые 2 элемента которого - множители
    :return: строковое представление произведения
    """
    return str(int(q[0]) * int(q[1]))


def question_text(q) -> str:
    """
    собираем текст вопроса
    :param q: массив, первые 2 элемента которого - множители
    :return: текст вопроса бля пользователя
    """
    return q[0] + ' ' + random.choice(words_operations) + ' ' + q[1]


def answer_text(q) -> str:
    """
    собираем текст ответа
    :param q: массив, первые 2 элемента которого - множители
    :return: полный текст примера
    """
    return q[0] + ' ' + random.choice(words_operations) + ' ' + q[1] + ' ' + random.choice(words) + ' ' + mul(q)


def count_answers(text):
    """
    подсчет количества целых чисел в строке
    :param text: строка
    :return: количество целых чисел в строке
    """
    return len(set(re.findall('\d+', text)))


def result_text(count_question_with_good_answer, count_question_with_answer):
    p = count_question_with_good_answer / count_question_with_answer
    if p > 0.8:
        return f'Отлично справляещься!\n' \
               f'Ты правильно ответил на {count_question_with_good_answer} из {count_question_with_answer}!'
    else:
        return f'Ты правильно ответил на {count_question_with_good_answer} из {count_question_with_answer}!'
