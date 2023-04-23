# подключение модулей
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QRadioButton, QPushButton, QButtonGroup
)
# класс вопрос
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
# обрабатывающую нажатие на «Ответить»
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    to_answer.setText('Следующий вопрос')
# обрабатывающую нажатие на «Следующий вопрос»
def show_question():
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroupBox.show()
    to_answer.setText('Ответить')
# next_question() для последовательного перехода между вопросами
def next_question():
    main_win.total += 1  #увеличиваем счетчик вопросов на 1
    # При задавании нового вопроса напечатай текущую статистику
    print('Статистика\n-Всего вопросов: ' +  str(main_win.total) + '\n-Правильных ответов: ' + str(main_win.score))
    cur_question = randint(0, len(questions_list) - 1)
    ask(questions_list[cur_question])
# Функция перемешивает список answer, заменяет тексты кнопок
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    answer_right.setText(q.right_answer)
    show_question()
# проверяет надпись кнопки
def check_ok():
    if to_answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()
# Функция check_answer() должна проверять правильность данного ответа при нажатии на «Ответить»
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1  #увеличиваем счетчик правильныхответов на 1
        # После проверки ответа пользователя отобрази изменённую статистику и рейтинг
        print('Статистика\n-Всего вопросов: ' +  str(main_win.total) + '\n-Правильных ответов: ' + str(main_win.score))
        print('Рейтинг: ' + str(main_win.score / main_win.total * 100) + ' %')
    else:
        show_correct('Неверно')
        # После проверки ответа пользователя отобрази изменённую статистику и рейтинг
        print('Статистика\n-Всего вопросов: ' +  str(main_win.total) + '\n-Правильных ответов: ' + str(main_win.score))
        print('Рейтинг: ' + str(main_win.score / main_win.total * 100) + ' %')
# Функция show_correct() должна: устанавливать текст-результат в форме ответа, отображать форму ответа
def show_correct(text_result):
    result.setText(text_result)
    show_result()

# создание объект-приложение, окно приложения, задали загаловок и размеры
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(500, 300)
# Введем 2 накопителя для вопросов(total) и верный ответов(score)
main_win.total = 0
main_win.score = 0

# Создай виджет-вопрос и виджет-кнопку
lb_question = QLabel('Какой национальности не существует?')
to_answer = QPushButton('Ответить')

# Создай набор переключателей с вариантами ответов. Расположи их по лэйаутам и объедини в группу
btn_answer1 = QRadioButton('Энцы')
btn_answer2 = QRadioButton('Смурфы')
btn_answer3 = QRadioButton('Чулымцы')
btn_answer4 = QRadioButton('Алеуты')
RadioGroupBox = QGroupBox('Варианты ответов')
layoutV1RadioGroup = QVBoxLayout()
layoutV2RadioGroup = QVBoxLayout()
layoutH1RadioGroup = QHBoxLayout()
layoutV1RadioGroup.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layoutV1RadioGroup.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layoutV1RadioGroup.setSpacing(3)
layoutV2RadioGroup.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layoutV2RadioGroup.addWidget(btn_answer4, alignment=Qt.AlignCenter)
layoutV2RadioGroup.setSpacing(3)
layoutH1RadioGroup.addLayout(layoutV1RadioGroup)
layoutH1RadioGroup.addLayout(layoutV2RadioGroup)
RadioGroupBox.setLayout(layoutH1RadioGroup)
# создаем группу для кнопок, может быть выбран только один из них
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

# Создай виджет-результат «Правильно» (или «Неправильно») и виджет для правильного ответа
result = QLabel('Правильно/Неправильно')
answer_right = QLabel('Правильный ответ')
# Расположи новые виджеты по лэйаутам и объедини их в группу.
AnsGroupBox = QGroupBox()
layoutV1AnsGroup = QVBoxLayout()
layoutV1AnsGroup.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layoutV1AnsGroup.addWidget(answer_right, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layoutV1AnsGroup)

# Расположи вопрос, группу переключателей и кнопку по лэйаутам
layout_mainV1 = QVBoxLayout()
layout_mainH1 = QHBoxLayout()
layout_mainH2 = QHBoxLayout()
layout_mainH3 = QHBoxLayout()
layout_mainH1.addWidget(lb_question, alignment=(Qt.AlignVCenter | Qt.AlignHCenter))
layout_mainH2.addWidget(RadioGroupBox)
layout_mainH2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_mainH3.addWidget(to_answer, alignment=Qt.AlignCenter)
layout_mainV1.addLayout(layout_mainH1)
layout_mainV1.addLayout(layout_mainH2)
layout_mainV1.addLayout(layout_mainH3)
main_win.setLayout(layout_mainV1)

# Создаем список кнопок
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
# создаем список вопросов
questions_list = list()
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Итальянский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Столица Российской Федерации', 'Москва', 'Симферополь', 'Санкт-Петербург', 'Пекин'))
questions_list.append(Question('Столица Турции', 'Анкара', 'Стамбул', 'Анталия', 'Мармарис'))
questions_list.append(Question('У древних греков была такая муза — Урания. Музой чего она являлась?', 'Астрономия', 'Математика', 'Торговля', 'Скульптура'))

next_question()
# Обработай клики по кнопке «Ответить»/«Следующий вопрос»
to_answer.clicked.connect(check_ok)



main_win.show()
app.exec_()

'''
# проверять надпись на кнопке - start_test()
def start_test():
    if to_answer.text() == 'Ответить':
        show_result()
    elif to_answer.text() == 'Следующий вопрос':
        show_question()









questions_list.append(Question('Вопрос7', 'Правильный ответ7', 'Неправильный ответ7', 'Неправильный ответ7', 'Неправильный ответ7'))
questions_list.append(Question('Вопрос8', 'Правильный ответ8', 'Неправильный ответ8', 'Неправильный ответ8', 'Неправильный ответ8'))
questions_list.append(Question('Вопрос9', 'Правильный ответ9', 'Неправильный ответ9', 'Неправильный ответ9', 'Неправильный ответ9'))
questions_list.append(Question('Вопрос10', 'Правильный ответ10', 'Неправильный ответ10', 'Неправильный ответ10', 'Неправильный ответ10'))
        '''