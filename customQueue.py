def enqueue(queue, element):
    queue.insert(0, element)


def dequeue(queue):
    try:
        queue.remove(queue[-1])
    except:
        print('nothing to  from an empty queue')


def viewQueue(queue):
    try:
        print(queue[-1])
    except:
        print('nothing to read from an empty queue')


testQueue = [1, 2, 3]

print(testQueue)
enqueue(testQueue, 4)
print(testQueue)
dequeue(testQueue)
print(testQueue)
dequeue(testQueue)
print(testQueue)
dequeue(testQueue)
print(testQueue)
dequeue(testQueue)
print(testQueue)
dequeue(testQueue)
