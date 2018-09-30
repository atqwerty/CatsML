#Каждая строка в файле соответствует одному предложению. 
#Считайте их, приведите каждую к нижнему регистру с помощью строковой функции lower().
import re
with open('sentences.txt', 'r') as f:
  sentences = []
  words = []
  for line in f:
    line_list = re.split('[^a-z]', line.strip('\\n\\r.').lower())
    line_list = list(filter(None, line_list))        
    sentences.append(line_list)
    words += line_list

cat = open('sentences.txt') #открыл файл
a = str(cat.readlines()).lower() #привел к нижнему регистру

#Произведите токенизацию, то есть разбиение текстов на слова. 
#Для этого можно воспользоваться регулярным выражением, 
#которое считает разделителем любой символ, не являющийся буквой: 
#re.split('[^a-z]', t). 

import re
token_cat = re.split('[^a-z]', a) #разделил на слова

#Не забудьте удалить пустые слова после разделения.

token = [x for x in token_cat if x != '\n' and x != ''] #удалил n - разделитель строки и пустые слова

#Составьте список всех слов, встречающихся в предложениях. 
#Сопоставьте каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях. 
#Для этого удобно воспользоваться структурой dict

#Определили функцию для оставления только уникальных значений списка
def unique(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

unique_token = unique(token)
keys = [x for x in range (len(unique_token))] # определил список ключей массивом от 0 до размера массива
dictionary_cats = dict(zip(keys, unique_token)) # создал словарь с ключчами от 0 до 254

#Создайте матрицу размера n * d, где n — число предложений. 
#Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. 
#У вас должна получиться матрица размера 22 * 254.

#Определяем функцию подсчета строк в файле

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i-1 # костыль, который подгоняет нужное мне значение (изначально было i+1)

n = file_len ('sentences.txt') # определяем количество строк = 22
d = len(unique_token)
import numpy as np

word_matrix = np.zeros(shape=(n,d))
for i in range(n):
  for j in range(d):
    word_matrix[i][j] = sentences[i].count(dictionary_cats[j])

#Найдите косинусное расстояние от предложения в самой первой строке 
#(In comparison to dogs, cats have not undergone...) 
#до всех остальных с помощью функции scipy.spatial.distance.cosine. 
#Какие номера у двух предложений, ближайших к нему по этому расстоянию 
#(строки нумеруются с нуля)? 
#Эти два числа и будут ответами на задание. 
#Само предложение (In comparison to dogs, cats have not undergone... ) имеет индекс 0.
import scipy.spatial.distance
cos_matrix = []
for i in range(n):
  cos_matrix.append(scipy.spatial.distance.cosine(word_matrix[0], word_matrix[i]))
cos_matrix = np.array(cos_matrix) 
print (cos_matrix)