# Hometask 5.1
import random

def get_wordsnumber(number_word: int, alph: str='abc'):
    list_word = []
    for i in range(number_word):
        random_word = random.sample(alph, k=3)
        list_word.append(''.join(random_word))
    return ' '.join(list_word)

def remove_abc(word_list):
    word = 'abc'
    list_final = list(filter(lambda i: word not in i, word_list.split()))
    return ' '.join(list_final)

all_list = get_wordsnumber(int(input('Кол-во слов: ')))
print(all_list)
print(remove_abc(all_list))