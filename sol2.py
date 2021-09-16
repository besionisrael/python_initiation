import re
def text_match(text):
        patterns = '^[a-z|A-Z|0-9|_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))
print(text_match("Python_Exercises_ 1"))


#^[a-z]+[A-Z]+[0-9]+$
