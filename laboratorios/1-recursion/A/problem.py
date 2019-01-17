#Cristian Andres Galeano Poveda
import json
from sys import stdin


    

# TODO Complete!!
def reverse(text):
    if len(text)== 1:
        return texto
    else:
        return text[::-1]
def main():
    text = stdin.readline().strip()
    print(reverse(text))
main()


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
