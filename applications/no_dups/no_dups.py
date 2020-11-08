
def no_dups(s):
    # Your code here
    cache = {}

    word_str = s.split()

    for word in word_str:
        if word not in cache:
            cache[word] = None

    return ' '.join(cache.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
