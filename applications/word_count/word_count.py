def word_count(s):
    result = {}
    
    # words = s.lower().translate(s.maketrans('','', '":;,.-+=/\\|[]{}()*^&')).split()
    words = s.lower().translate({ord(i):None for i in '":;,.-+=/\\|[]{}()*^&'}).split()

    for word in words:
        if word:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
                

    return result



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))