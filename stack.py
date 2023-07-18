def view(stack):
        try:
            return stack[-1]
        except:
            print('Es kann nichts vom Leeren Stack gelesen werden.')

def push(stack, element):
    stack.append(element)

def pop(stack):
    try:
        stack.remove(stack[-1])
    except:
        print('Es kann nichts vom Leeren Stack genommen werden.')

stack = []