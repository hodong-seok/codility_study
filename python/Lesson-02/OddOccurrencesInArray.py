# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    result = 0
    for i in A:
        result ^= i

    # result = reduce(lambda:x,y, x^y, A)
    # 이 코드가 더욱 깔끔하다.
    return result
