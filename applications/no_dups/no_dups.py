def no_dups(s):
    words = {}
    result = ""
    
    for w in s.split():
        if w not in words:
            # check if it's not the first word to add space
            if words:
                result += " "
            
            result += w
            words[w] = w

    return result
        

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))