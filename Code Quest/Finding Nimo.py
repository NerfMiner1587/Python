cases = int(input().rstrip())

letters = []
spaces = 1

for i in range(cases):
    line = input().rstrip()
    
    for j in line:
        letters.append(j)
        
    for k in range(len(letters)):
        if letters[k] == " ":
            spaces += 1
        if letters[k] == "N":
            if len(letters)>k+1:
                if letters[k+1] == "i":
                    if len(letters)>k+2:
                        if letters[k+2] == "m":
                            if len(letters)>k+3:
                                if letters[k+3] == "o":
                                    print(spaces)
            
            
    letters.clear()
    spaces = 1
