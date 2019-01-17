import json
from sys import stdin

# TODO Complete!
def arrange(numbers,a,b):
    if len(numbers)== 1:
        return a+b+numbers
    else:
        if numbers[0]%2 == 0:
            a.append(numbers[0])
            numbers.remove(numbers[0])
            return arrange(numbers,a,b)
        else:
            b.append(numbers[0])
            numbers.remove(numbers[0])
            return arrange(numbers,a,b)
        
def main():
    numbers = list(map(int,stdin.readline().strip().split(',')))
    print(arrange(numbers,[],[]))
main()

    
    
            

if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers,[],[])
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
