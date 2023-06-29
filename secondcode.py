def count_occurrences(string):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    count = 0

    for i in range(len(string) - 3):
        if string[i] in vowels and string[i + 1] in vowels and string[i + 2] in consonants and string[i + 3] in consonants:
            count += 1

    return count
string = input("Enter a string: ")
occurrences = count_occurrences(string)
print("Consonants -", occurrences)
print("Vowels -", occurrences)
