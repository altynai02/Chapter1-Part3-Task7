# 7. Напишите функцию где исходный список содержит
# положительные и отрицательные числа. Требуется
# положительные поместить в один список, а отрицательные
# - в другой.

def plus_minus(list_):
    positive = []
    negative =[]
    for i in list_:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
        else:
            continue
    return list_, negative, positive

print(plus_minus([2,3,4, 0 , -2,-33, 5, -100]))