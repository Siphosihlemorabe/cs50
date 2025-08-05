def main():
    sentence = input("Input something: ")
    no_vowels = remove_vowels(sentence)
    print(no_vowels)

def remove_vowels(sentence):
    vowels = "aeiouAEIOU"
    result = ""
    for char in sentence:
        if char not in vowels:
            result += char
    return result

main()
