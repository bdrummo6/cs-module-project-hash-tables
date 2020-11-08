
import re

def word_count(s):
    # Your code here
    cache = {}

    word_str = re.sub(r'[^A-Za-z0-9\' ]+', ' ', s).lower().split()

    for word in word_str:
        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))