def log(model_expression, result):
    expression = ' '.join(map(str, model_expression))
    with open('expression.txt', 'a') as data:
        data.write(f'{expression} = {result}\n')
