# import random
# import time
#
# names=['abcd','edf','ere','jy','tjhyu5','htr','rg4er','trh','gtryht','oofe']
# majors=['gwefe','rgre','gerger','werg','gerg','gerg','erger','gergre','qwrqwr','kuy']
#
# def main():
#     # nums = [1,2,3,4,5]
#     # myg= genfunc(nums)
#     # print(list(myg))
#     # for i in myg:
#     #     print(i)
#     t1=time.clock()
#     people = getpeople(1000000)
#     t2=time.clock()
#
#     print('Total time taken with list is {}'.format(t2-t1))
#     ##Gen works fir large list iteration because not all has to be on memory
#     t3=time.clock()
#     people = genpeople(100000)
#     t4=time.clock()
#     print('Total time taken with generator is {}'.format(t4-t3))
#
# def genfunc(nums):
#     for i in nums:
#         yield i*i
#
# def getpeople(n):
#     result=[]
#     for i in range(n):
#         person = {'id': i ,
#                   'name': random.choice(names),
#                 'majors':random.choice(majors)
#                 }
#         result.append(person)
#     return result
#
# def genpeople(n):
#     for i in range(n):
#         person = {'id': i ,
#                   'name': random.choice(names),
#                   'majors':random.choice(majors)
#                   }
#         yield person
#


def main():
    lists = [
        [1,2,3,4,5,6],
        [2,5,7,8],
        [3,9,10,12],
        [0,1,2,8]]
    res = lists[0]
    for i in range(1,len(lists)):
        res = listjoin(res,lists[i])
    print(res)
def listjoin(a1,a2):
    res =[]
    i=0
    j=0
    while i < len(a1) and j<len(a2):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i+=1
        elif a1[i] >= a2[j]:
            res.append(a2[j])
            j+=1
    while i < len(a1):
        res.append(a1[i])
        i+=1
    while j < len(a2):
        res.append(a2[j])
        j+=1
    return res
if __name__ == '__main__':
    main()
