import json


# TODO Complete!
def has_more_vowels(s,voc):
    
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e'or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A'or s[i]=='E' or s[i]=='I' or s[i]=='O'or s[i]=='U':
            voc=voc+1
    if voc > len(s)//2:
        return True
    else:
        return False
            
    

if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s,0)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
