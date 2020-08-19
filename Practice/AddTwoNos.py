# Definition for singly-linked list.
from configparser import LegacyInterpolation


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen=0
        setstr=set()
        i=0
        j=0
        n=len(s)
        res=[]
        res[:0]=s
        while i<n and j<n:
            if res[j] not in setstr:
                setstr.add(res[j])
                j+=1
                maxlen=max(maxlen,j-i)
            else:
                setstr.remove(res[i])
                i+=1

        return maxlen

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        firstIter = True
        res = None
        prev = None
        while l1 is not None or l2 is not None:
            x = 0 if l1 is None else l1.val
            y= 0 if l2 is None else l2.val
            sum = x + y + carry
            carry = 1 if sum>=10 else 0
            sum = sum % 10 if sum >= 10 else sum
            print(sum)
            newNode=ListNode(sum)
            if res is None:
                res = newNode
            else:
                prev.next = newNode
            prev = newNode
            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next

        if carry >0:
            newNode=ListNode(carry)
            prev.next=newNode

        return(res)

solution = Solution()

def reverseList(node):
    curr = node
    prev = None
    while curr!= None:
        newnode = curr.next
        curr.next = prev
        prev = curr
        if newnode is None:
            return curr
        curr = newnode

def recreverseList(node,prev):
    if node != None:
        temp1 = node.next
        node.next = prev
        prev = node
        return recreverseList(temp1,prev)
    else:
        return prev


def printList(node):
    s =""
    while node is not None:
        s= s + " " + str(node.val)
        node = node.next
    print("The list is " + str(s))

def main():
    # # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # n1 = ListNode(5)
    # # n2= ListNode(2)
    # # n3= ListNode(3)
    # # n4= ListNode(7)
    # # n1.next=n2
    # # n2.next=n3
    # # n3.next=n4
    # m1 = ListNode(5)
    # # m2= ListNode(1)
    # # m3= ListNode(4)
    # # m1.next=m2
    # # m2.next=m3
    #
    # # newheadn1 = reverseList(n1)
    # # newheadm1 = reverseList(m1)
    # printList(n1)
    # printList(m1)
    # # nh = recreverseList(n1,None)
    # # mh = recreverseList (m1,None)
    #
    # res=solution.addTwoNumbers(n1,m1)
    # printList(res)
    str="abcbc"
    res = solution.lengthOfLongestSubstring(str)
    print(res)




if __name__ == '__main__':
    main()