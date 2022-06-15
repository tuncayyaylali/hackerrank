K = int(input())
rooms = input().split()
rooms_1 = set(rooms)
distinct_rooms = list(set(rooms))
for i in distinct_rooms:
    rooms.remove(i)
rooms = set(rooms)
print(rooms_1.difference(rooms).pop())
