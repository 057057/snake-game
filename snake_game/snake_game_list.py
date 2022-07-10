from distutils.command.build_py import build_py
from random import randrange


num=10 #board size=num*nmum

def row():
  # make row with num of '.'
  row=[]
  for i in range (num):
      row.append ('.')
  return row

def board():
  board=[]
  # make board with num of row
  for i in range (num):
      board.append (row())
  return board

def wall():
    ground=board()
    for i in range(num):
        ground[i][0]='|'
    for i in range(num):
        ground[i][-1]='|'
    for j in range(num):
        ground[0][j]='-'
    for j in range(num):
        ground[-1][j]='-'
    return ground

def food():
    food_y=randrange(1,num-1)
    food_x=randrange(1,num-1)
    if ground[food_y][food_x]=='S':
        ground[food_y][food_x]='S'
        food_y=randrange(1,num-1)
        food_x=randrange(1,num-1)
    else:
        ground[food_y][food_x]='O'
    return ground



def find(target):
    for y,lst in enumerate(ground):
        for x,element in enumerate(lst):
            if element == 'S':
                return y,x
    return (None, None)

def find_food(target):
    for food_y,lst in enumerate(ground):
        for food_x,element in enumerate(lst):
            if element == 'O':
                return food_y, food_x
    return (None, None)

def snake_mv():
  global y,x
  ground[y][x]='.'
  #user_mv=input('type "e":move right; "w":move left; "n":move up; "s":move down')
  if user_mv=='w':
    x=x-1
    if ground[y][x]=='O':
        ground[y][x+1+ate_food_num():x]=snake_body()
    if ground[y][x]=='.':
        ground[y][x]='S' 
  if user_mv=='e':
    x=x+1
    if ground[y][x]=='O':
        ground[y][x-1-ate_food_num():x]=snake_body()
    if ground[y][x]=='.':
        ground[y][x]='S' 
  if user_mv=='s':
    y=y+1
    ground[y][x]='S' 
  if user_mv=='n':
    y=y-1
    ground[y][x]='S' 
    
  return ground,y,x

def snake_bd_mv():
    global food_y, food_x
    bd_y=food_y
    bd_x=food_x
    if user_mv=='w':
        bd_x=bd_x-1
        ground[bd_y][bd_x]='S'
    if user_mv=='e':
        bd_x=bd_x+1
        ground[bd_y][bd_x]='S'
    if user_mv=='s':
        bd_y=bd_y-1
        ground[bd_y][bd_x]='S'
    if user_mv=='n':
        bd_y=bd_y+1
        ground[bd_y][bd_x]='S'
    return ground

def hit_the_wall():
    while True:
        snake_mv()
        if x==0 or x==num-1 or y==0 or y==num-1 :
            print('You are dead on the wall')
            break
        else:
            ground[y][x]='S' 

def snake_body():
    snake_body=[]
    length=ate_food_num()+1#how many food
    for i in range (length):
        snake_body.append('S')
    return snake_body

def ate_food_num():
    food_count=0
    if x==food_x and y==food_y:
        food_count=food_count+1
    return food_count



def display_board():
  for line in ground:
    for element in line:
      print(element,end='')
    print()

#game status
game_on=True
game_over=False

#main code
ground=wall()
ground[1][1]='S'
food()
display_board()
y,x=find('S')
food_x,food_y=find_food('O')
print(food_x,food_y)
while True:
    user_mv=input('type "e":move right; "w":move left; "n":move up; "s":move down')
    snake_mv()
    while ate_food_num()>0:
        food()
        snake_bd_mv()
    if x==0 or x==num-1 or y==0 or y==num-1:
        break
    else:
        display_board()

print('game over')
    




