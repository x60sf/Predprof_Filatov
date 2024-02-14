File = 'game.txt'
def read_txt(filename):
    '''Open the file and read it into a string.'''
    with open(filename, 'r') as f:
        return f.read()

def merge(left, right):
    '''Merge two sorted lists into one sorted list.'''
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
def mergesort(array):
    '''Sort a list of lists.'''
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left, right)

Game_Array = read_txt(File).split('\n')
Game_ndArray=[]
'''Create a list of lists'''
for game in Game_Array:
    Game_ndArray.append(game.split('$'))
Game_ndArray = Game_ndArray[1:]
Game_ndArray = mergesort(Game_ndArray)
'''Find count of error in each game'''
Game_Dict = {}
GameName_Pred = Game_ndArray[0][0]
counter=0
for index in range(1,len(Game_ndArray)):
    GameName = Game_ndArray[index][0]
    if GameName_Pred == GameName:
        counter+=1
    else:
        Game_Dict[GameName_Pred]=counter+1
        counter=0
    GameName_Pred=GameName

'''Print out the count of error in each game'''
counter2=0
for i in Game_Dict.keys():
    counter2+=1
    print(f'Игра{counter2} - количество багов:{Game_Dict[i]}')