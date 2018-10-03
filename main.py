# Маркитанов Денис КБТУ Машинное Обучение 2018
import re
import numpy as np
import scipy.spatial.distance
import math

def cosDist(x, y): # кастомная функция косинусового расстояния
    dotProduct = 0
    powX = 0
    powY = 0
    for i in range(len(y)): # пробегаюсь по векторам
        dotProduct += x[i] * y[i]
        powX += x[i] * x[i]
        powY += y[i] * y[i]
    return 1 - (dotProduct / (math.sqrt(powX) * math.sqrt(powY))) # возвращаю 1 - косинусовую симилярность (в итоге косинусово расстояние), которое считается выражением косинуса скалярного произведения


with open('sentences.txt', 'r') as f:
  sentences = [] # массив будет хранить все предложения в нижнем регистре (каждое слово есть элемент массива)
  for sentence in f:
    sentenceList = re.split('[^a-z]', sentence.strip('\\n\\r.').lower())
    sentenceList = list(filter(None, sentenceList))        
    sentences.append(sentenceList) # добавление листа слов предложения в массив

text = open('sentences.txt') # открываю файл для токенизации
loweredText = str(text.readlines()).lower() # в нижний регистр

token = re.split('[^a-z]', loweredText) # разделил предложения на слова

token = [x for x in token if x != '\n' and x != ''] # удалил лишнее

uniqueToken = np.unique(token) # вытащил уникальные значения
keys = [x for x in range (len(uniqueToken))] # список уникальных слов
dictionary = dict(zip(keys, uniqueToken)) # словарь

n = sum(1 for line in open('sentences.txt')) # вытаскиваю количество строк
# n = file_len('sentences.txt') # вытаскиваем количество строк
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