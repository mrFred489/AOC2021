def getXYFromPair(pair):
    x, y = pair.split(",")
    return (int(x), int(y))

def extractCoordsFromLine(line):
    start, end = line.strip().split(" -> ")
    return (getXYFromPair(start), getXYFromPair(end))

data = [extractCoordsFromLine(line) for line in open("d5.data")]



def getRangeBetween(s1, s2):
    if s1 > s2:
        return range(s2, s1 + 1)
    return range(s1, s2 + 1)

def part1():
    coords = dict()
    for start, end in data:
        if start[0] != end[0] and start[1] != end[1]:
            continue
        if start[0] == end[0]:
            # print("0", len(list(getRangeBetween(start[1], end[1]+1))), start[1], end[1]+1)
            # if len(list(getRangeBetween(start[1], end[1]))) == 0:
            #     print("it is zero", start, end)
            for y in getRangeBetween(start[1], end[1]):
                coord = (start[0], y)
                if coord not in coords:
                     coords.update({coord: 1})
                else:
                    coords[coord] += 1
        else:
            # print("1", len(list(getRangeBetween(start[0], end[0]))), start[0], end[0]+1)
            for x in getRangeBetween(start[0], end[0]):
                coord = (x, start[1])
                if coord not in coords:
                    coords.update({coord: 1})
                else:
                    coords[coord] += 1
    # for coord in coords:
    #     print(coord, coords[coord])
    coordsWithOverlapping = [c for c in coords if coords[c] > 1]
    print(len(coordsWithOverlapping))
    # print(coordsWithOverlapping)



def getLineInclDiagonal(start, end):
    if start[0] == end[0]:
        ycoords = getRangeBetween(start[1], end[1])
        return [(start[0], y) for y in ycoords]
    elif start[1] == end[1]:
        xcoords = getRangeBetween(start[0], end[0])
        return [(x, start[1]) for x in xcoords]
    else:
        xrange = list(getRangeBetween(start[0], end[0]))
        yrange = list(getRangeBetween(start[1], end[1]))
        if xrange[0] != start[0]:
            xrange = list(reversed(xrange))
        if yrange[0] != start[1]:
            yrange = list(reversed(yrange))
        line = []
        for i in range(len(xrange)):
            line.append((xrange[i], yrange[i]))
        # print("diag line", start, end, line, )
        return line


def part2():
    coords = dict()
    for start, end in data:
        line = getLineInclDiagonal(start, end)
        for coord in line:
            if coord not in coords:
                coords.update({coord: 1})
            else:
                coords[coord] += 1
    coordsWithOverlapping = [c for c in coords if coords[c] > 1]


    for y in range(10):
        xline = ""
        for x in range(10):
            if (x, y) in coords:
                xline += str(coords[(x, y)])
            else:
                xline += "."
        # print(xline)
    print(len(coordsWithOverlapping))






part2()
