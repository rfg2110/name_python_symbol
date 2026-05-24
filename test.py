planet = ...
flag = 'по умолчанию'

if planet == 'Венера' or planet == 'Земля' or planet == 'Марс':
    flag = 'планета земной группы'
elif planet == 'Юпитер' or planet == 'Сатурн' or planet == 'Уран':
    flag = 'планета-гигант'
elif planet == 'Плутон' or planet == 'Макемаке' or planet == 'Эрида':
    flag = 'транснептуновый объект'