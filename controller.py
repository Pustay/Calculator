from model import parse, calculate
from view import view_result as view
from logger import log

def button_click():
    flag = input('Введите +, чтобы продолжить, или другой символ, чтобы прервать работу программы: ')
    while flag == '+':
        model_expression = parse()
        result = calculate(model_expression)
        log(model_expression, result)
        view(result)
        flag = input('Введите +, чтобы продолжить, или другой символ, чтобы прервать работу программы: ')
    print('Программа завершена.')