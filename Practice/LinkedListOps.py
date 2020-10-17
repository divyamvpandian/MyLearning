def findMid(head):
    curr=head
    next=head
    while next.next!=None:
        if next.next.next==None:
            return curr.next.data
        next=next.next.next
        curr=curr.next
    return curr.data


def rotateLL(head, k, n):
    i = 0
    newpos = n - k
    # // to rotate k times, find the head
    curr = head
    prev = head
    while curr != None:
        if i == newpos:
            newhead = curr
            prev.next = None
        prev = curr
        curr = curr.next
        i += 1
    prev.next = head
    return newhead


class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = self.tail.next

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

def reverseList(head):
    prev = head
    curr = prev.next
    prev.next=None
    while curr!=None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head

def printlist(head):
    curr=  head
    while curr!=None:
        print(curr.data)
        curr=curr.next

def findMergept(head1,head2):
    c1=0
    c2=0
    curr1=head1
    curr2=head2
    while curr1!=None:
        c1+=1
        curr1=curr1.next
    while curr2!=None:
        c2+=1
        curr2=curr2.next
    d = abs(c1-c2)
    curr1=head1
    curr2=head2
    for i in range(0,d):
        curr1 = curr1.next
    for i in range(0,c2):
        if curr1.data==curr2.data:
            return curr1.data
        curr1=curr1.next
        curr2=curr2.next
    return -1

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n1 = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n1)

        # n2 = int(input())
        # arr2 = list(map(int, input().strip().split()))
        # print(arr2)
        # head2 = createList(arr2, n2)
        # print(findMid(head))
        # head = reverseList(head)
        k=3
        newhead = rotateLL(head, k, n1)
        printlist(newhead)
        # mergepoint = findMergept(head1,head2)
        # print(mergepoint)