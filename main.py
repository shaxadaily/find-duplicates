lst = []
lst1 = []
duplicates = []
while True:
    n = input('Введите имя: ')
    if n == 'stop':
        print(f'\nВсе участники : {sorted(lst)} \n Количество: {len(lst)}\n Дубликаты: {len(duplicates)}\n')
        print('-'*100)
        print(f'\nУникальные: {sorted(lst1)} \n Количество: {len(lst1)}')
        break
    else:
        lst.append(n)

    if n not in lst1:
        lst1.append(n)
    else:
        duplicates.append(n)
        print('\nЭто дубликат\n')
