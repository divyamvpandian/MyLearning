from queue import Queue
class StackusingQ:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, element):
        self.q2.put(element)

        while (not self.q1.empty()):
            topelement = self.q1.queue[0]
            self.q2.put(topelement)
            self.q1.get()

        self.temp = self.q2
        self.q2 = self.q1
        self.q1 = self.temp

    def pop(self):
        topelement=""
        topelement = self.q1.get()
        return topelement

def main():
    d = StackusingQ()
    d.push(10)
    d.push(20)
    d.push(30)
    d.push(40)
    print(d.pop())
    print(d.pop())
    print(d.pop())
    print(d.pop())


if __name__ == "__main__":
    main()


