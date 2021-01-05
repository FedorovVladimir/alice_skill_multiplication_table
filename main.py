import random

from alice_scripts import Skill, say, request, suggest

from questions import questions
from states import State

skill = Skill(__name__)

praises = ['Верно', 'Всё верно', 'Ты прав', 'Да, это так']
errors = ['Это не правильно', 'Тут ты не прав', 'Ошибка']

words_operations = ['на', 'умножить на']
words = ['равно', 'будет']


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


@skill.script
def run_script():
    question = []
    state = State.Start
    yield say(
        'Привет! Я буду задавать вопросы на умножение, а ты должен отвечать.\n'
        'Всё просто!\n'
        'Готов учить таблицу умножения?',
        suggest('Да', 'Готов', 'Конечно'))
    while True:
        if request.has_lemmas('умеешь'):
            state = State.FirstQuestion
            yield say('Я умею задавать вопросы, например "2 на 2", а ты должен ответить.\n'
                      'Я проверю!\n'
                      'Готов учить таблицу умножения?', suggest('Да', 'Готов', 'Конечно'))

        elif request.has_lemmas('помощь'):
            state = State.FirstQuestion
            yield say('Все просто! Я буду задавать вопросы, например "2 на 2", а ты должен ответить.\n'
                      'Я проверю!\n'
                      'Готов учить таблицу умножения?', suggest('Да', 'Готов', 'Конечно'))

        elif state == State.Start:
            if request.has_lemmas('Да', 'Готов', 'Давай', 'Конечно', 'Начнем'):
                state = State.FirstQuestion
            else:
                yield say('Не понял', suggest('Начнём'))

        elif state == State.FirstQuestion:
            state = State.Question
            question = random.choice(questions)
            yield say(question_text(question))

        elif state == State.Question:
            old = question
            question = random.choice(questions)
            if request.has_lemmas(mul(old)):
                reaction = random.choice(praises)
            else:
                reaction = random.choice(errors)
            yield say(reaction + '\n' + answer_text(old) + '\n\n' + question_text(question))

        else:
            yield say('Не понял')


if __name__ == '__main__':
    skill.run(host="0.0.0.0", port="5000")
