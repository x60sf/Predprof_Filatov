File = 'game.txt'
Write_File = 'game_new.csv'
def read_txt(filename):
    '''Open the file and read it into a string.'''
    with open(filename, 'r') as f:
        return f.read()

def write_csv(filename, Done_string):
    '''Write Done_Array to a csv file.'''
    with open(filename, 'w') as f:
        f.write(Done_string)

Game_Array = read_txt(File).split('\n')
Game_ndArray = []

'''Create a list of lists'''
for game in Game_Array:
    Game_ndArray.append(game.split('$'))
Game_ndArray = Game_ndArray[1:]

'''Find the name of the game with 55 error'''
Done_str = ''
for game in Game_ndArray:
    GameName=game[0]
    character=game[1]
    nameError=game[2]
    date=game[3]
    if nameError.count('55')>0:
        print(f'У персонажа\t{character}\tв игре\t{GameName}\tнашлась ошибка с кодом:\t {nameError}.\tДата фиксации:\t {date}')
        Done_str +=f'{GameName},{character},Done,0000-00-00\n'
write_csv(Write_File,Done_str)