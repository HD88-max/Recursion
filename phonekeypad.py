keypad = ["","", "abc", "def", "jkl", " mno", "pqrs", "tuv", "wxyz"]

def printCombination(combination, current, output, n):
    if current == n:
        print(*output, sep=",")
        return
    
    for i in range(len(keypad[combination[current]])):
        output.append(keypad[combination[current]][i])
        printCombination(combination, current + 1, output, n)

        output.pop()
        if (combination[current] == 0 or combination[current]) == 1:
            return

combination = [4,3,4]
n = len(combination)
printCombination(combination, 0, [], n)