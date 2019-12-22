import matplotlib as mpl
import matplotlib.pyplot as plt


def count_letter(word, char):  # Считает количество букв char в файле word
    count = 0  # Счетчик количества элементов
    for c in word:
        if char == c:
            count += 1  # Увеличение счетчика, если элемент встречается в строке
    return count


def table_def_eng(data_names_eng=None, data_values_eng=None):
    if data_values_eng is None:
        data_values_eng = list()
    if data_names_eng is None:
        data_names_eng = list()
    dpi = 90
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
    fig.savefig('bars_ENG.png')
    return 0


def letter_find_eng():
    f = open('textin.txt', "r")  # Переменная файла, открытие файла для его чтения
    a = f.read()  # Переменная-текст в котором сохряняется текст
    f.close()  # Закрывается файл
    letter_list_eng = list()  # Список количества английских букв в тексте
    letter_list_eng_l = list()  # Список названий английских букв
    i = 0  # Счетчик списка
    while i < 26:  # Заполняет список элементами английского и русского алфавита
        letter_list_eng.append(i)  # Создается элемент в листе под номером-буквой
        letter_list_eng_l.append(i)
        letter_list_eng[i] = count_letter(a, chr(i + 97)) + count_letter(a, chr(i + 65))
        letter_list_eng_l[i] = chr(i + 65)
        i += 1  # Увеличение счетчика на 1 - движение на следующую букву алфавита
    table_def_eng(letter_list_eng_l, letter_list_eng)
    return 0


letter_find_eng()
print("Done")  # Индикатор конца программы
exit()

# Заглавная А(ENG) = 65; Заглавная Z(ENG) = 90;
# Малая a(ENG) = 97; Малая z(ENG) = 122;
