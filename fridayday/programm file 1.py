import matplotlib as mpl
import matplotlib.pyplot as plt


def count_letter(word, char):  # Считает количество букв char в файле
    count = 0  # Счетчик количества элементов
    for c in word:
        if char == c:
            count += 1  # Увеличение счетчика, если элемент встречается в строке
    return count


i = 0  # Счетчик списка
letter_list_eng = list()  # Список количества английских букв в тексте
letter_list_eng_l = list()  # Список названий английских букв
letter_list_rus = list()  # Список количества русских букв в тексте
letter_list_rus_l = list()  # Список названий русских букв
f = open('textin.txt', "r")  # Переменная файла, открытие файла для его чтения
a = f.read()  # Переменная-текст в котором сохряняется текст
f.close()  # Закрывается файл
while i < 26:  # Заполняет список элементами английского и русского алфавита
    letter_list_eng.append(i)  # Создается элемент в листе под номером-буквой
    letter_list_eng_l.append(i)
    letter_list_rus.append(i)  # Создается элемент в листе под номером-буквой
    letter_list_rus_l.append(i)
    letter_list_eng[i] = count_letter(a, chr(i + 97)) + count_letter(a, chr(i + 65))
    letter_list_eng_l[i] = chr(i + 65)
    letter_list_rus[i] = count_letter(a, chr(i + 1072)) + count_letter(a, chr(i + 1040))
    # Элемент = количеству раз, когда появляется буква
    i += 1  # Увеличение счетчика на 1 - движение на следующую букву алфавита
while i < 33:  # Продолжает заполнять лист, но уже с русским алфавитом
    letter_list_rus.append(i)
    letter_list_rus[i] = count_letter(a, chr(i + 1072)) + count_letter(a, chr(i + 1040))
    i += 1
letter_list_rus.append(i)
letter_list_rus[i] = count_letter(a, chr(1105)) + count_letter(a, chr(1025))
# Тут начинается магия
data_names_eng = letter_list_eng_l
data_values_eng = letter_list_eng
#
dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})
plt.title('Very Important Table Eng')
ax = plt.axes()
ax.yaxis.grid(True, zorder=1)
xs = range(len(data_names_eng))
plt.bar([x + 0.05 for x in xs], [d * 0.9 for d in data_values_eng],
        width=0.2, color='red', alpha=0.7,
        zorder=2)
plt.xticks(xs, data_names_eng)
fig.autofmt_xdate(rotation=25)
plt.legend(loc='upper right')
fig.savefig('barsEng.png')
# Тут магия кончается

print("Done")  # Индикатор конца программы
exit()

# Заглавная А(ENG) = 65; Заглавная Z(ENG) = 90;
# Малая a(ENG) = 97; Малая z(ENG) = 122;

# Заглавная А(RUS) = 1040; Заглавная Я() = 1071; Заглавная Ё() = 1025;
# Малая а(RUS) = 1072; Малая я() = 1103; Малая ё() = 1105;
