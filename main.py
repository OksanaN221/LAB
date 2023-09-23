#Country

RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[40m'

for i in range(6):
    if i == 0 or i == 5:
        print(f'{RED}{"   " * 5}{END}')
    if i == 1 or i == 4:
        print(f'{RED}{"   " * 2}{WHITE}{"   "}{RED}{"   " * 2}{END}')
    if i == 3:
        print(f'{RED}{"   "}{WHITE}{"   " * 3}{RED}{"   "}{END}')


#Pattern

print(f'{BLACK}{"   " * 32}{END}')
print(f'{BLACK}{"   " * 7}{WHITE}{"   " * 3}{BLACK}{"   " * 6}{BLACK}{"   " * 6}{WHITE}{"   " * 3}{BLACK}{"   " * 7}{END}')
print(f'{BLACK}{"   " * 5}{WHITE}{"   " * 7}{BLACK}{"   " * 4}{BLACK}{"   " * 4}{WHITE}{"   " * 7}{BLACK}{"   " * 5}{END}')
print(f'{BLACK}{"   " * 3}{WHITE}{"   " * 3}{BLACK}{"   " * 5}{WHITE}{"   " * 3}{BLACK}{"   " * 2}{BLACK}{"   " * 2}{WHITE}{"   " * 3}{BLACK}{"   " * 5}{WHITE}{"   " * 3}{BLACK}{"   " * 3}{END}')
print(f'{BLACK}{"   " * 2}{WHITE}{"   " * 3}{BLACK}{"   " * 7}{WHITE}{"   " * 3}{BLACK}{"   " * 1}{BLACK}{"   " * 1}{WHITE}{"   " * 3}{BLACK}{"   " * 7}{WHITE}{"   " * 3}{BLACK}{"   " * 2}{END}')
print(f'{BLACK}{"   " * 1}{WHITE}{"   " * 3}{BLACK}{"   " * 9}{WHITE}{"   " * 3}{WHITE}{"   " * 3}{BLACK}{"   " * 9}{WHITE}{"   " * 4}{END}')
print(f'{BLACK}{"   " * 1}{WHITE}{"   " * 3}{BLACK}{"   " * 9}{WHITE}{"   " * 3}{WHITE}{"   " * 3}{BLACK}{"   " * 9}{WHITE}{"   " * 4}{END}')
print(f'{BLACK}{"   " * 2}{WHITE}{"   " * 3}{BLACK}{"   " * 7}{WHITE}{"   " * 3}{BLACK}{"   " * 1}{BLACK}{"   " * 1}{WHITE}{"   " * 3}{BLACK}{"   " * 7}{WHITE}{"   " * 3}{BLACK}{"   " * 2}{END}')
print(f'{BLACK}{"   " * 3}{WHITE}{"   " * 3}{BLACK}{"   " * 5}{WHITE}{"   " * 3}{BLACK}{"   " * 2}{BLACK}{"   " * 2}{WHITE}{"   " * 3}{BLACK}{"   " * 5}{WHITE}{"   " * 3}{BLACK}{"   " * 3}{END}')
print(f'{BLACK}{"   " * 5}{WHITE}{"   " * 7}{BLACK}{"   " * 4}{BLACK}{"   " * 4}{WHITE}{"   " * 7}{BLACK}{"   " * 5}{END}')
print(f'{BLACK}{"   " * 7}{WHITE}{"   " * 3}{BLACK}{"   " * 6}{BLACK}{"   " * 6}{WHITE}{"   " * 3}{BLACK}{"   " * 7}{END}')
print(f'{BLACK}{"   " * 32}{END}')


#Function

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i/3

step = round(abs(result[0] - result[9]) / 7, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step


for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k + 1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '||'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

for i in range(10):
    pass


#Diagramm

cnt1 = 0
file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
dl = len(list)
for i in range(dl - 1):
    if -3 <= list[i] <= 3:
        cnt1 += 1
cnt2 = dl - cnt1
print(f'{WHITE}{" " * (int(cnt1/dl * 100))}{END}', cnt1/dl * 100, '%')
print(f'{WHITE}{" " * (int(cnt2/dl * 100))}{END}', cnt2/dl * 100, '%')