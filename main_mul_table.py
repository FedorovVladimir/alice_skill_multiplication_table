import random

from alice_scripts import Skill, say, request, suggest

from src.mul_table.questions_mul_table import questions
from src.rules import count_answers, praises, errors, result_text
from src.mul_table.rules_mul_table import question_text, mul, answer_text, start_text, help_text, can_text
from src.states import State

skill = Skill(__name__)


@skill.script
def run_script():
    question = []
    state = State.Start
    count_answer = 0
    count_good_answer = 0

    # приветственная фраза
    yield say(start_text(), suggest('Да', 'Готов', 'Конечно'))

    while True:
        # что ты умеешь?
        if request.has_lemmas('умеешь'):
            state = State.NewQuestion
            yield say(can_text(), suggest('Да', 'Готов', 'Конечно'))

        # помощь
        elif request.has_lemmas('помощь'):
            state = State.NewQuestion
            yield say(help_text(), suggest('Да', 'Готов', 'Конечно'))

        # обработка ответа на приветственную фразу
        elif state == State.Start:
            if request.has_lemmas('Да', 'Готов', 'Давай', 'Конечно', 'Начнем'):
                state = State.NewQuestion
            else:
                yield say('Не понял', suggest('Начнём'))

        # задаем новый вопрос
        elif state == State.NewQuestion:
            state = State.AnswerAndNewQuestion
            question = random.choice(questions)
            yield say(question_text(question))

        # обрабатывает ответ и задаем новый вопрос
        elif state == State.AnswerAndNewQuestion:
            # проверка количества чисел
            count = count_answers(request.command)
            if count == 0:
                yield say('Ответом должно быть число.\nДавай ещё раз.\n\n' + question_text(question))
            elif count > 1:
                yield say('Ответом должно быть одно число.\nДавай ещё раз.\n\n' + question_text(question))
            else:
                old = question
                while old == question:
                    question = random.choice(questions)
                count_answer += 1
                # правильно
                if request.has_lemmas(mul(old)):
                    reaction = random.choice(praises)
                    count_good_answer += 1
                # не правильно
                else:
                    reaction = random.choice(errors)

                text = reaction + '\n' + answer_text(old) + '\n\n'
                if count_answer % 7 == 0:
                    text += result_text(count_good_answer, count_answer) + '\n\n'
                text += question_text(question)
                yield say(text)

        else:
            yield say('Не понял')


if __name__ == '__main__':
    skill.run(host="0.0.0.0", port="5000")
