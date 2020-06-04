def word_count(s):

    words = s.lower()

    # convert all whitespace characters to a space
    characters_whitespace = '\n \t \r'.split(" ")
    
    for whitespace in characters_whitespace:
        words = words.replace(whitespace, " ")

    # remove characters to be ignored
    characters_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for character in characters_to_ignore:
        words = words.replace(character, "")

    # turn string into an array of individual words        
    words = words.split(" ")

    words_already_seen = dict()

    for word in words:

        # skip empty strings
        if word == "":
            continue

        if word in words_already_seen:
            words_already_seen[word] += 1
        else:
            words_already_seen[word] = 1

    return words_already_seen

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))