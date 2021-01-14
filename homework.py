import sys
import random
x = 0

print ("Давай сыграем в одну игру")
print ("У меня есть 10 вопросов")
print ("Тебе всего-то нужно вписывать правильный ответ на заданный вопрос")
print ("Первый вопрос!")
#Задаем первый вопрос
a1 = "да"
a1_no = "нет"
while True:
    q1 = input ("Думаешь сможешь ответить правильно на все вопросы? " ).lower()
    if q1 == a1:
        print ("По крайней мере у тебя есть вера, следующий вопрос!")
        x = x + 1
        break
    if q1 == a1_no:
        print("Пошел вон")
        sys.exit(0)
    else:
        print ("А ты не очень то умный, попробуем еще раз.")

#Задаем второй вопрос вопрос

#a2 = "да"
#a2_no = "нет"

r1 = random.randint(1,10)
r2 = random.randint(1,10)
r1_r2_summ = random.randint(1,20)



while True:
    r1 = random.randint(1,10)
    r2 = random.randint(1,10)
    r1_r2_summ = random.randint(1,20)

    q2 = input (f"{r1} + {r2} = {r1_r2_summ} ?:" )
    if r1 + r2 == r1_r2_summ:
        if q2 == "да":
            print ("Это было не трудно, следующий вопрос!")
            x = x + 1
            break
        else:
            print ("ты уверен?")

    if r1 + r2 != r1_r2_summ:
        if q2 == "нет":
            print ("Это было не трудно, следующий вопрос!")
            x = x + 1
            break
        else:
            print ("ты уверен?")
    

while True:
    q3 = input ("Тук-тук, кто там? " ).lower()
    if q3 == "четвертый":
        print ("Это было не трудно, следующий вопрос!")
        x = x + 1
        break
    elif q3 == "4":
        print ("Это было не трудно, следующий вопрос!")
        x = x + 1
        break   
    else:
        print ("А если подумать?")

print ( "На этом всё, число верно дынных ответов:", x )
sys.exit(0)

