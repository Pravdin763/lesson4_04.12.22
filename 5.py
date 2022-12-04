# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt') as file1:
    f1 = file1.readline()
with open('file2.txt') as file2:
    f2 = file2.readline()
print('текст первого файла: ', f1)
print('текст второго файла: ', f2)


def repl(file):             # функция удаляет пробел между знаком справа и = 0
    return file.replace(' + ', ' +').replace(' - ', ' -')[:-4]

f11 = repl(f1).split()
f12 = repl(f2).split()


def takedict(x):            # функция создает словарь, где значение степень, а ключ множитель
    if '*' not in x:
        x += '**1'
    slov = {}
    if x[-1].isdigit():
        slov[x[-1]] = ''
    rs = ''                 #переменная куда записывается множитель(х) как текст (если вдруг больше 9, 99 итд..)
    for i in x[:-1]:
        if i.isdigit() or i in '-':
            rs += i
    slov[x[-1]] = int(rs)
    return slov

f1_2 = [takedict(i) for i in f11]
f2_2 = [takedict(i) for i in f12]
f1_2.extend(f2_2)           # объединяем словари файлов


result = {}
for i in f1_2:          # суммируем значения по ключам (где ключ ^степень, значение множитель х)
    for key, value in i.items():                # и записываем все в новый словарь result
        result[key] = result.get(key, 0) + value

text = ''
for key, value in sorted(result.items(), reverse=True):
    text += str(value) + 'x^' + str(key) + ' + '
text = (text[:-2] + '= 0').replace('^1', '').replace('+ -','- ')
print('готовый текст, сумма многочленов: ', text)

with open('itogfile.txt', 'w') as file:
    file.write(text)
