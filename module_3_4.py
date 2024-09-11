'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №3.04
Самостоятельная работа по уроку "Произвольное число параметров"
'''


# Определение функции
def single_root_words(root_word, *other_words):
    same_words = list()
    for word in other_words:
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            same_words.append(word)
    return same_words


# Обращения к функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)