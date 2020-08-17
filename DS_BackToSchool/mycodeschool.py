from timeit import timeit
import sys

class LinkedList:

    def __init__(self):
        self.head = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def inorderdisplay(root):
    if root is None:
        return None
    inorderdisplay(root.left)
    print(root.data)
    inorderdisplay(root.right)


class BinaryTree(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.left = None
        self.right = None\


## This has all problems of Programming interview Qns Playlist under mycodeschool channel - https://www.youtube.com/playlist?list=PL2_aWCzGMAwLPEZrZIcNEq9ukGWPfLT4A
def binarysearch(arr, val, occurence):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if val == arr[mid]:
            result = mid
            ## for first occurentce search again before the mid element
            if occurence == "First":
                high = mid - 1
            elif occurence == "Last":
                ## for the last occurence search again after mid element
                low = mid + 1
        elif val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result


def noofrotationsinarr(rotatedarr):
    rotatedarr = [8, 11, 12, 2, 3, 5]
    prev = 0
    cnt = 0
    for i in rotatedarr:
        if i < prev:
            return cnt
            break
        else:
            prev = i
            cnt += 1


def noofrotationsinarroptimized(rotatedarr):
    rotatedarr = [8, 11, 12, 2, 3, 5]
    low = 0
    high = len(rotatedarr) - 1
    while low <= high:
        mid = (low + high) // 2
        if rotatedarr[low] < rotatedarr[high]:
            return low
        elif rotatedarr[mid] <= rotatedarr[mid - 1] and rotatedarr[mid] <= rotatedarr[mid + 1]:
            return mid
        elif rotatedarr[mid] <= rotatedarr[high]:
            high = mid - 1
        elif rotatedarr[mid] >= rotatedarr[low]:
            low = mid + 1
    return -1


def circularArrySearch(val, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if val == arr[mid]:
            return mid
        elif arr[mid] <= arr[high]:
            if val > arr[mid] and val <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if val >= arr[low] and val < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1


def printspiralOrder(arr):
    m = len(arr[0])
    n = len(arr)
    top = 0
    bottom = n - 1  ##3
    left = 0
    right = m - 1  ##3
    dir = 0
    while top <= bottom and left <= right:
        if dir == 0:
            i = left
            while i <= right:
                print(arr[top][i])
                i += 1
            top += 1
            dir = 1
        if dir == 1:
            i = top
            while i <= bottom:
                print(arr[i][right])
                i += 1
            right -= 1
            dir = 2
        if dir == 2:
            i = right
            while i >= left:
                print(arr[bottom][i])
                i -= 1
            bottom -= 1
            dir = 3
        if dir == 3:
            i = bottom
            while i >= top:
                print(arr[i][left])
                i -= 1
            left += 1
            dir = 0


def reverselinkedlist(curr):
    prev = None
    while curr != None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def printList(node):
    s = ""
    while node is not None:
        s = s + " " + str(node.val)
        node = node.next
    print("The list is " + str(s))


def recreverselinkedlist(curr, prev):
    if curr is None:
        printList(prev)
    else:
        temp = curr.next
        curr.next = prev
        prev = curr
        recreverselinkedlist(temp, prev)


def reverseprintList(node):
    if node is None:
        return
    reverseprintList(node.next)
    print(node.val)


def stackReverse(node):
    print("Reversing a list using stack")
    stack = []
    while node != None:
        stack.append(node)
        node = node.next
    prev = stack.pop()
    while len(stack) != 0:
        temp = stack.pop()
        prev.next = temp
    prev.next = None

def isBST(root,min,max):
    if root is None:
        return True
    if root.data > min and root.data < max and isBST(root.left,min,root.data) and isBST(root.right,root.data,max):
        return True
    else:
        return False

def findsubArr(arr,sum):
    start=0
    currsum=arr[0]
    n = len(arr)
    i=1
    while i <= n:
        while currsum > sum and start < i-1:
            currsum -= arr[start]
            start+=1

        if currsum==sum:
            print("Subarray found in ",start,i-1)
            return

        if i < n:
            currsum += arr[i]
        i +=1
    print("No subArr found")

def main():
    ## 1 Binary Search for first or last occurence
    arr = [2, 4, 10, 10, 10, 18, 19, 20]
    val = 10
    occurence = 'First'
    print("#1 Binary search for first occurence", binarysearch(arr, val, "First"))
    print("#1 Binary search for last occurence", binarysearch(arr, val, "Last"))

    ##2 count of element in a sortedlist

    list = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8]
    val = 8
    minVal = binarysearch(list, val, occurence="First")
    maxVal = binarysearch(list, val, occurence="Last")
    print("#2 count element in a sortedList is {}".format(maxVal - minVal + 1))

    ##3 Given a sorted Array. How many times its rotated..

    rotatedarr = [8, 11, 12, 2, 3, 5]
    print("#3 The array is rotated for around (regular iterative)", noofrotationsinarr(rotatedarr), " times")
    rotatedarr = [15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12]
    print("#3 The array is rotated for around (regular iterative)", noofrotationsinarroptimized(rotatedarr), " times")
    # print(timeit('noofrotationsinarr()', setup='from __main__ import noofrotationsinarr'))
    # print(timeit('noofrotationsinarroptimized()', setup='from __main__ import noofrotationsinarroptimized'))

    ##4 search element in circular sorted array
    cirrotatedarr = [8, 11, 12, 2, 3, 5]
    val = 12
    print("#4 position of given val in array is  ", circularArrySearch(val, cirrotatedarr))

    ## Given 2D Array and print in spiral order
    T = [[11, 12, 5, 2], [15, 6, 10, 5], [10, 8, 12, 5], [12, 15, 8, 6]]
    print("#5 Priting Array in 2d Spiral fashin as below\n ")
    printspiralOrder(T)

    ## 6 and 8 Reverse a linked list iteration and Recursion

    n1 = ListNode(5)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(7)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    # printLis(reverselinkedlist(n1)) ##6
    # recreverselinkedlist(n1,None) ##8

    ## 7  print list in reverse order in recursion
    printList(n1)

    ## 9 Reverse a list using stack
    stackReverse(n1)

    ## 11 if Binary Tree is BST
    root = Node(7)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(8)
    root.right.right = Node(12)
    min = -4294967296
    max = 4294967296
    if (isBST(root,min,max)):
        print("Is BST")
    else:
        print("Is Not a BST")
    print("Displaying a BinaryTree")
    root.display()
    print("Inorder Displaying a BinaryTree")
    inorderdisplay(root)

    arr=[15,2,4,8,9,5,10,23]
    sum=23
    print(findsubArr(arr,sum))

if __name__ == "__main__":
    main()
