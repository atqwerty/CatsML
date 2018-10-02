# Маркитанов Денис КБТУ Машинное Обучение 2018
import re
import numpy as np
import scipy.spatial.distance
import math

def unique(token):
    n = []
    for i in token:
        if i not in n:
            n.append(i)
    return n

def file_len(fileName):
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
    return i+1 # костыль ¯\_(ツ)_/¯

def cosDist(x, y): # кастомная функция косинусового расстояния
    dotProduct = 0
    powX = 0
    powY = 0
    for i in range(len(y)): # пробегаюсь по векторам
        dotProduct += x[i] * y[i]
        powX += x[i] * x[i]
        powY += y[i] * y[i]
    return 1 - (dotProduct / (math.sqrt(powX) * math.sqrt(powY))) # возвращаю 1 - косинусовую симилярность (в итоге косинусово расстояние), которое считается выражением косинуса скалярного произведения


with open('C:\\Users\\Денис\\Desktop\\Programing\\ML\\Cats\\CatsML\\sentences.txt', 'r') as f:
  sentences = [] # массив будет хранить все предложения в нижнем регистре (каждое слово есть элемент массива)
  for sentence in f:
    sentenceList = re.split('[^a-z]', sentence.strip('\\n\\r.').lower())
    sentenceList = list(filter(None, sentenceList))        
    sentences.append(sentenceList) # добавление листа слов предложения в массив

text = open('C:\\Users\\Денис\\Desktop\\Programing\\ML\\Cats\\CatsML\\sentences.txt') # открываю файл для токенизации
loweredText = str(text.readlines()).lower() # в нижний регистр

token_cat = re.split('[^a-z]', loweredText) # разделил предложения на слова

token = [x for x in token_cat if x != '\n' and x != ''] # удалил лишнее

uniqueToken = unique(token) # вытащил уникальные значения
keys = [x for x in range (len(uniqueToken))] # список уникальных слов
dictionary = dict(zip(keys, uniqueToken)) # словарь

n = file_len('C:\\Users\\Денис\\Desktop\\Programing\\ML\\Cats\\CatsML\\sentences.txt') # вытаскиваем количество строк
d = len(uniqueToken)

matrix = np.zeros(shape=(n,d)) # создал матрицу 22 (количество строк) на 255 (все нули)
for i in range(n):
  for j in range(d):
    matrix[i][j] = sentences[i].count(dictionary[j]) # ложу в матрицу количество слов из словаря, которые встречаются в предложении


output = []
for i in range(n):
#   output.append(scipy.spatial.distance.cosine(matrix[0], matrix[i]))
    output.append(cosDist(matrix[0], matrix[i]))
output = np.array(output) 
print (output)