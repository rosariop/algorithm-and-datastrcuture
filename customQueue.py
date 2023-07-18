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


queue = [1, 2, 3]

print(queue)
enqueue(queue, 4)
print(queue)
dequeue(queue)
print(queue)
dequeue(queue)
print(queue)
dequeue(queue)
print(queue)
dequeue(queue)
print(queue)
dequeue(queue)
