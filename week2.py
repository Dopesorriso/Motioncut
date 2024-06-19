def count_words(input_string):
    words = input_string.split()
    return len(words)
def main():
    while True:
        input_string = input("Enter a sentence or paragraph: ")
        if len(input_string) == 0:
            print("Please enter a non-empty string.")
        else:
            word_count = count_words(input_string)
            print(f"The number of words in the input is: {word_count}")
            break
if __name__ == "__main__":
    main()
