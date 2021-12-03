data = [line.strip() for line in open("d3.data")]

def mostCommon(numbers):
    nums = [(0,0) for i in range(len(numbers[0]))]
    for line in numbers:
        for ind in range(len(line)):
            tup = nums[ind]
            if (line[ind] == "0"):
                res = (tup[0] + 1, tup[1])
            else:
                res = (tup[0], tup[1] + 1)
            nums[ind] = res
    return nums

def part1():
    nums = mostCommon(data)
    gamma = ""
    epsilon = ""
    for b1, b2 in nums:
        if b1 > b2:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    answer = int(gamma, 2) * int(epsilon, 2)
    print(answer)


def bitFilter(myFilter):
    filteredData = data
    for i in range(len(data[0])):
        acceptedValues = []
        commonForEachIndex = mostCommon(filteredData)
        for d in filteredData:
            if myFilter(d[i], i, commonForEachIndex):
                acceptedValues.append(d)
        filteredData = acceptedValues
        if (len(filteredData) == 1):
            break
    return filteredData

def oxygenFilter(bit, ind, commonForEachIndex):
    b1, b2 = commonForEachIndex[ind]
    if b1 > b2:
        if bit == "0":
            return True
        return False
    return bit == "1"

def co2ScrubFilter(bit, ind, commonForEachIndex):
    b1, b2 = commonForEachIndex[ind]
    if b1 <= b2:
        if bit == "0":
            return True
        return False
    return bit == "1"


def part2():
    oxGenRating = bitFilter(oxygenFilter)[0]
    co2ScrubRating = bitFilter(co2ScrubFilter)[0]
    answer = int(oxGenRating, 2) * int(co2ScrubRating, 2)
    print(answer)


part2()
