def view(stack):
        try:
            return stack[-1]
        except:
            print('nothing to read from an empty stack.')

def push(stack, element):
    stack.append(element)

def pop(stack):
    try:
        stack.remove(stack[-1])
    except:
        print('nothing to delete from an empty stack')

stack = []