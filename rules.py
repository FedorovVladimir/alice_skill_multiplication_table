import re

praises = ['Верно', 'Всё верно', 'Ты прав', 'Да, это так']
errors = ['Это не правильно', 'Тут ты не прав', 'Ошибка']
words = ['равно', 'будет']


def result_text(count_question_with_good_answer, count_question_with_answer):
    p = count_question_with_good_answer / count_question_with_answer
    if p > 0.8:
        return f'Отлично справляещься!\n' \
               f'Ты правильно ответил на {count_question_with_good_answer} из {count_question_with_answer}!'
    else:
        return f'Ты правильно ответил на {count_question_with_good_answer} из {count_question_with_answer}!'


def count_answers(text):
    return len(set(re.findall('\d+', text)))
