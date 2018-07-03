import sys
import collections


class Node:
    element = ''
    t = 0
    i = 0
    j = 0

    def __init__(self, el, time, x, y):
        self.element = el
        self.t = time
        self.i = x
        self.j = y


def expansion(matter, i, j, time, universeMap, fQueue):
    if i >= 0 and j >= 0 and i < 1000 and j < 1000:
        if universeMap[i][j] == '.':
            universeMap[i][j] = matter
            fQueue.append(Node(matter, time + 1, i, j))
            return False
        elif (universeMap[i][j] == '+' and matter == '-') or (universeMap[i][j] == '-' and matter == '+') or (universeMap[i][j] == '*' and matter == '+') or (universeMap[i][j] == '*' and matter == '-'):
            universeMap[i][j] = '*'
            return True
        else:
            return False
    else:
        return False


def main():
    try:
        myfile = open(sys.argv[1])
        universe = [[' ' for x in range(1000)] for y in range(1000)]
        floodQueue = collections.deque()
        i = 0
        j = 0
        # reading from file
        data = myfile.read(1)
        while data:
            if data == '\n':
                i = i + 1
                j = 0
            elif data == ' ':
                throw_away = data
            else:
                universe[i][j] = data
                if data == '+' or data == '-':
                    n = Node(data, 0, i, j)
                    floodQueue.append(n)
                j = j + 1
                endj = j
            data = myfile.read(1)

        if i == 0:
            endi = 1
        else:
            endi = i

        flag = 0
        timeofend = 0
        it = floodQueue[0]
        while floodQueue:
            i = it.i
            j = it.j
            if (expansion(it.element, i - 1, j, it.t, universe, floodQueue)):
                timeofend = it.t + 1
                flag = 1
            if (expansion(it.element, i + 1, j, it.t, universe, floodQueue)):
                timeofend = it.t + 1
                flag = 1
            if (expansion(it.element, i, j - 1, it.t, universe, floodQueue)):
                timeofend = it.t + 1
                flag = 1
            if (expansion(it.element, i, j + 1, it.t, universe, floodQueue)):
                timeofend = it.t + 1
                flag = 1
            it = floodQueue.popleft()
            if floodQueue:
                it = floodQueue[0];
            else:
                it = None;
            if floodQueue:
                if it.t >= timeofend and flag == 1:
                    print(timeofend)
                    break
            else:
                if flag == 1:
                    print(timeofend)
                else:
                    print('the world is saved')

        # printing the map of the world
        for i in range(endi + 1):
            if i != 0:
                print('\n', end='')
            for j in range(endj):
                print(universe[i][j], end='')


    finally:
        myfile.close()


main()        