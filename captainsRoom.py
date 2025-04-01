def findRoom(listofNum: list, k:int):
    dic_room = {}
    for i in listofNum:
        value = dic_room.get(i, 0) + 1
        dic_room[i] =value
    
    for i in dic_room:
        if dic_room[i]<k:
            return int(i)

k = int(input())
inputOfroom = input()
listofNum = inputOfroom.split()
print(findRoom(listofNum, k))