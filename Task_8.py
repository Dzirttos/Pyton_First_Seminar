# Задача 8
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите длину шоколадки:  '))
m = int(input('Введите ширину шоколадки:  '))

if m > n:
    print('\033[31mВообще-то мы просили сначала ввести длину, а не ширину. Ну да ладно - в данном случае это не принципиально.')

k = int(input('\033[37mСколько долек Вы хотите отломить? \n'))

if k < n or k < m:
    print('\033[31mЗа один раз столько долек отломить не получится!')

elif k > (m*n):
    print('\033[33mЭто же больше всей шоколадки! Ешьте уже целиком!')

else:
    print(f'\033[32m{k} дольки за один раз отломить можно.')
