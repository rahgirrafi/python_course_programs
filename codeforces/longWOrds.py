n = int(input())

while(n>0):
    word = input()  
    if len(word) > 10:
        print(word[0]+str(len(word)-2)+word[-1]) #concatanation
    else:
        print(word)

    n= n-1
