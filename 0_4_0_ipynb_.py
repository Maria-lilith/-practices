# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.4.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F035qPmto8IZwTYmL0hoax4rba23LNa8

Введите ваше ФИО:
"""

Новоселова Мария Антоновна

"""***Дисклеймер***

В данной практике запрещено использования функций:


*   sum()
*   min()
*   max()
*   average()
*   reversed()
*   sorted()
*   готовые функции или библиотеки

**Задача 1:**



Интернет-магазин предлагает следующие условия скидок:

*   Для заказов больше 1000 единиц, клиент получает скидку 5%. Если клиент использует промокод SUPERDISCOUNT, он получает скидку 10% (вместо 5%).
*  Для заказов более 5000 единиц, клиент получает скидку 15%, а использование промокода SUPERDISCOUNT увеличивает скидку до 20% (вместо 15%).

Этап 1:
Ввод:
```
Введите стоимость единицы товара: 5
Введите количество товара: 1001
Введите промокод: GiVEMEDISCONT
```

Вывод:

```
Ваша скидка: 5%
Итоговая сумма: 4750.0
```
Этап 2:

Оформите ваш код в виде функции
"""

st=int(input('Введите стоимость товара:'))
k=int(input('Ввндите количество товара:'))
prom=input('Введите промокод:')
def f(st,k,prom,summ,sail):
  summ=st*k
  if 1000<k<=5000:
    if prom=='SUPERDISCOUNT':
      sail=10
      summ=summ-summ*sail/100
    else:
      sail=5
      summ=summ-summ*sail/100
  elif k>5000:
    if prom=='SUPERDISCOUNT':
      sail=20
      summ=summ-summ*sail/100
    else:
      sail=15
      summ=summ-summ*sail/100
  return('Ваша скидка:',sail,'Сумма:',summ)
print(f(st,k,prom,0,0))

"""**Задача 2:**

Этап 1:
Напишите программу способную отфильтровать список и вывести только положительные элементы


Ввод:
```
-1 5 1 2 -3
```

Вывод:

```
5 1 2
```

Этап 2:

Оформите ваш код в виде функции
"""

A=list(map(int,input().split()))
def f(A):
  B=[]
  for i in A:
    if i>0:
      B.append(i)
  return B
print(f(A))

"""**Задача 3:**

Этап 1:
Напишите программу реализующую Алгоритм Евклида


> Алгоритм Евклида – это алгоритм нахождения наибольшего общего делителя (НОД) пары целых чисел.



Ввод:
```
30 18
```

Вывод:

```
6
```

Этап 2:
Оформите ваш код в виде функции

"""

a=int(input())
b=int(input())
def f(a,b):
  B=[]
  i=1
  while i!=a+1 and i!=b+1:
    if a%i==0 and b%i==0:
      B.append(i)
    i+=1
  return(B[-1])
print(f(a,b))

"""**Задача 4:**

Этап 1:
Напишите функцию программу, которая принимает строку и возвращает список слов и количество их упомнинаний в предложении

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
apple banana apple
```

Вывод:

```
apple: 2,
banana: 1
```
"""

A=list((input().split()))
def f(A):
  B=[]
  for i in A:
    if B.count(i)==0:
      B.append(i)
  for i in B:
    print( i,':',A.count(i))
print(f(A))

"""**Задача 5:**

Этап 1:
Детектор анаграмм Напишите программу на Python, которая принимает в качестве входных данных две строки и проверяет, являются ли они анаграммами друг друга

Этап 2:
Оформите ваш код в виде функции

Ввод:
```
listen, silent
```

Вывод:

```
True
```
"""

s1=input()
s2=input()
def f(s1,s2):
  if len(s1)!=len(s2):
    return False
  else:
    for i in s1:
      if s1.count(i)==s2.count(i):
        return True
      else:
        return False
print(f(s1,s2))

"""**Задача 6:**

Шифр ​​Цезаря

Напишите программу на Python, которая реализует шифр Цезаря, простой метод шифрования, который заменяет каждую букву буквой на фиксированное количество позиций вниз по алфавиту. Программа должна запрашивать у пользователя сообщение и значение сдвига, а затем шифровать и расшифровывать сообщение.

Этап 1:

Напишите код для реализации данной задачи

Этап 2:

Оформите код в виде нескольких функций:

* Зашифровывает сообщение
* Расшифровывает сообщение
"""

sl=input('Введите слово')
k=int(input('Введите количество позиций'))
alf=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
def fz(sl,k,alf):
  B=[]
  for i in range(len(sl)):
    ind=alf.index(sl[i])
    if ind+k>len(alf):
       B.append(alf[ind+k-len(alf)])
    else:
      B.append(alf[ind+k])
    sh=''.join(B)
  return(sh)
def fr(sl,k,alf):
  B=[]
  for i in range(len(sl)):
    ind=alf.index(sl[i])
    B.append(alf[ind-k])
    sh=''.join(B)
  return(sh)
tar=input('Выбирите: зашифровать или расшифровать')
if tar=='зашифровать':
  print(fz(sl,k,alf))
if tar=='расшифровать':
  print(fr(sl,k,alf))

"""**Задача 7**

Задача: «Банковская система»

Создайте программу Python, которая имитирует базовую банковскую систему. Система должна иметь следующие функции:

Требования
*   Система должна позволять клиентам создавать счета и хранить их балансы.
*   Система должна позволять клиентам вносить и снимать деньги со своих счетов.
*   Система должна позволять клиентам проверять свой текущий баланс.
*   Система должна позволять клиентам переводить деньги между счетами.
*   Система должна отслеживать транзакции (депозиты, снятия и переводы) и иметь возможность печатать детали транзакций.


Задачи
1. Реализуйте банковскую систему, используя только базовые конструкции Python, такие как def, lists, if, elif и else, без классов или словарей.
Определите функции для создания счетов, внесения и снятия денег, получения балансов счетов, перевода денег между счетами, а также создания и печати транзакций.
2. Напишите основную функцию, которая демонстрирует использование банковской системы путем создания счетов, внесения и снятия денег и перевода денег между счетами.
3. Бонусное задание
Реализуйте способ хранения и печати истории транзакций для каждого счета.

Ограничения
Не используйте классы или словари.
Используйте только базовые конструкции Python, такие как def, lists, if, elif и else.

"""

