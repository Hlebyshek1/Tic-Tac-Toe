def print_table():
    a1 = a[:3]
    a2 = a[3:6]
    a3 = a[6:]
    print("---------")
    print(f'| {" ".join(a1)} |')
    print(f'| {" ".join(a2)} |')
    print(f'| {" ".join(a3)} |')
    print("---------")


def win_state():
    global win_combinations,a,counter,x_count,o_count,X_win,O_win,win
    for x in win_combinations:
        if(a[x[0]]==a[x[1]]==a[x[2]]=='X'):
            X_win = 1
        if(a[x[0]]==a[x[1]]==a[x[2]]=='O'):
            O_win = 1
    if (X_win == 1):
        print('X wins')
        counter=0
        win = False
    elif(O_win == 1):
        print('O wins')
        counter=0
        win = False
    elif(X_win == O_win and turn_count == 9):
        print('Draw')
        win = False

a = '_________'
win_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
turns = ('X','O','X','O','X','O','X','O','X')
turn_count = 0
x_count = 0
o_count = 0
X_win = 0
O_win = 0
counter = 0
y = 0
win = True
print_table()
table = [(1, 3), (2, 3), (3, 3),
(1, 2), (2, 2), (3, 2),
(1, 1), (2, 1), (3, 1)]
b = list(a)
while(win):
    print('Enter the coordinates:')
    try:
        coord1,coord2 = map(int,input().split())
    except:
        print("You should enter numbers!")
    else:
        if(1<=int(coord1),int(coord2)<=3):
            for x in table:
                if(int(coord1) == x[0] and int(coord2) == x[1]):
                    if(b[y] == '_'):
                        b[y] = turns[turn_count]
                        a = ''.join(b)
                        print_table()
                        turn_count+=1
                    else:
                        print('This cell is occupied! Choose another one!')
                y+=1
        if(coord1>=4 or coord1<=0 and coord2<=0 or coord2>=4):
            print('Coordinates should be from 1 to 3!')
        y = 0
    if(turn_count>=5):
        win_state()
    else:
        pass
