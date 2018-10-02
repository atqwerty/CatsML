import re
import numpy as np

def unique(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i-1 # костыль, который подгоняет нужное мне значение (изначально было i+1)

with open('sentences.txt', 'r') as f:
  sentences = [] # массив будет хранить все предложения в нижнем регистре (каждое слово есть элемент массива)
  for line in f:
    line_list = re.split('[^a-z]', line.strip('\\n\\r.').lower())
    line_list = list(filter(None, line_list))        
    sentences.append(line_list) # добавление листа слов предложения в массив

cat = open('sentences.txt') # открываю файл для токенизации
a = str(cat.readlines()).lower() # в нижний регистр

token_cat = re.split('[^a-z]', a) # разделил предложения на слова

token = [x for x in token_cat if x != '\n' and x != ''] # удалил лишнее

#Составьте список всех слов, встречающихся в предложениях. 
#Сопоставьте каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях. 
#Для этого удобно воспользоваться структурой dict

unique_token = unique(token) # вытащил уникальные значения
keys = [x for x in range (len(unique_token))] # список уникальных слов
dictionary_cats = dict(zip(keys, unique_token)) # словарь

#Создайте матрицу размера n * d, где n — число предложений. 
#Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. 
#У вас должна получиться матрица размера 22 * 254.

#Определяем функцию подсчета строк в файле


n = file_len ('sentences.txt') # вытаскиваем количество строк
d = len(unique_token)

word_matrix = np.zeros(shape=(n,d)) # создал матрицу 22 (количество строк) на 255 (все нули)
for i in range(n):
  for j in range(d):
    word_matrix[i][j] = sentences[i].count(dictionary_cats[j]) # ложу в матрицу количество слов из словаря, которые встречаются в предложении

import scipy.spatial.distance
cos_matrix = []
for i in range(n):
  cos_matrix.append(scipy.spatial.distance.cosine(word_matrix[0], word_matrix[i]))
cos_matrix = np.array(cos_matrix) 
print (cos_matrix)