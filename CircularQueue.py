q_size = 5
list = [None]*q_size
front = 0
rear = 0


def isEmpty():
    if (front == rear):
        print("Empty")
        return True

    else:
        return False


def isFull():
    if rear == q_size:
        print("Full")

        return True
    else:
        return False


def enQueue(e):
    global front, rear
    if not isFull():
        list[rear] = e
        rear += 1


def deQueue():
    global front, rear
    if not isEmpty():
        list[front] = None
        front += 1
        print("잘나감")


enQueue(3)
enQueue(4)
enQueue(5)
enQueue(6)
enQueue(7)
enQueue(8)

deQueue()
enQueue(6)
print(list)
