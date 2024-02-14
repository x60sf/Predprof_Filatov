File = 'game.txt'
def read_txt(filename):
    '''Open the file and read it into a string.'''
    with open(filename, 'r') as f:
        return f.read()


Game_Array = read_txt(File).split('\n')
Game_ndArray=[]
'''Create a list of lists'''
for game in Game_Array:
    Game_ndArray.append(game.split('$'))
Game_ndArray = sorted(Game_ndArray[1:])

counter = 0
If_Found=False
character = input('Введите имя персонажа: ')
for game in Game_ndArray:
    if character == game[1] and counter < 5:
        print(game[0])
        counter += 1
        If_Found=True
    elif character == game[1] and counter == 5:
        print(game[0])
        print('и др.')
        counter += 1
        If_Found=True
    else:
        counter = 0
if If_Found == False:
    print('Этого персонажа не существует')