fibonacciList = [0,1]
newValor = 0

def isFibonacci(entry):
    while entry > fibonacciList[-1]:
        newValor = fibonacciList[-1] + fibonacciList[-2]
        fibonacciList.append(newValor)

    if entry in fibonacciList:
        return True
    return False

entry = input()
entry = int(entry)

if isFibonacci(entry):
    print("O número " + str(entry) + " pertence a sequência de Fibonacci")
else:
    print("O número " + str(entry) + " não pertence a sequência de Fibonacci")