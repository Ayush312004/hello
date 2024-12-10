def Display_word_with_longest_length():
    Str = input("Enter the main string: ").strip()  # Remove leading/trailing spaces
    if not Str:
        print("Empty string provided.")
        return

    words = Str.split()  # Split by spaces
    longest_word = max(words, key=len, default="")
    print(f"\tWord with longest length is '{longest_word}' having length {len(longest_word)}\n")

def Determine_frequency_of_occurrence_of_particular_character_in_string():
    Str = input("Enter the string: ")
    C = input("Enter the character: ")

    if len(C) != 1:
        print("Please enter a single character.")
        return

    count = Str.count(C)
    print(f"\tCharacter '{C}' occurs {count} times in the string.\n")

def Check_for_palindrome():
    Str = input("Enter the string to be checked: ").strip()
    if not Str:
        print("Empty string provided.")
        return

    if Str == Str[::-1]:
        print(f"\t'{Str}' is a palindrome string.\n")
    else:
        print(f"\t'{Str}' is not a palindrome string.\n")

def display_index_of_first_appearance_of_the_substring():
    M = input("Enter the main string: ")
    S = input("Enter the sub string to check: ")

    if len(S) == 0:
        print("Empty substring provided.")
        return

    index = M.find(S)
    if index != -1:
        print(f"Substring '{S}' found at index {index}\n")
    else:
        print(f"Substring '{S}' not found in the main string.\n")

def Count_occurrences_of_each_word_in_given_string():
    Str = input("Enter the main string: ").strip()
    if not Str:
        print("Empty string provided.")
        return

    words = Str.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("\tWord occurrences:")
    for word, count in word_count.items():
        print(f"\t{word:15}: {count}")
    print()

def main():
    while True:
        print("\t\t  **** STRING OPERATIONS ****")
        print("\t\t1 : Display word with longest length")
        print("\t\t2 : Determine the frequency of occurrence of particular character in the string")
        print("\t\t3 : Check whether given string is palindrome or not")
        print("\t\t4 : Display index of first appearance of the substring")
        print("\t\t5 : Count the occurrences of each word in a given string")
        print("\t\t6 : Exit")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        if ch == 6:
            print("End of Program")
            break
        elif ch == 1:
            Display_word_with_longest_length()
        elif ch == 2:
            Determine_frequency_of_occurrence_of_particular_character_in_string()
        elif ch == 3:
            Check_for_palindrome()
        elif ch == 4:
            display_index_of_first_appearance_of_the_substring()
        elif ch == 5:
            Count_occurrences_of_each_word_in_given_string()
        else:
            print("Wrong choice entered! Try again.")

if __name__ == "__main__":
    main()
