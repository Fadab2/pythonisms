class Stack:
    def __init__(self, top=None):
        self.top = None

    def __iter__(self):
        def value_generator():
            current = self.top
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        return len(Stack(iter(self)))

    def push(self, value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None

            return temp.value

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.top.value

    def __str__(self):
        if self.isEmpty():
             print("Stack is empty")
             exit(0)
        else:
            current = self.top
            stack = " "

            while(current):
                stack += (f'{{ {current.value} }} -> ')
                current = current.next
            stack = (f'{stack}NULL')
            return stack

    def isEmpty(self):
        if self.top == None:
            return True
        return False
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    stack1 = Stack()

    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)
    #print(stack1.__str__())
    # stack1.pop()
    # stack1.pop()
    # stack1.pop()
    # print(stack1.__sizeof__())
    stack1.__str__()
    stack1.peek()
    num_gen = stack1.__iter__()
    for i in range(4):
        try:
            print(next(num_gen))
        except StopIteration:
            print("Stack is empty")

