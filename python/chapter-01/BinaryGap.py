# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binaryN = str(format(N, "b"))

    zeroMaxLength=0;
    tmp=0
    for i in range(len(binaryN)):
        if binaryN[i]=="1":
            zeroMaxLength = tmp if zeroMaxLength < tmp else zeroMaxLength
            tmp = 0
        elif binaryN[i]=="0":
            tmp += 1

    return zeroMaxLength
