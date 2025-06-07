# class sentence:
#     def __init__(self, input_string: str, delimiter: str) -> None:
#         # We firstly store the string and delimiter when the object is created.
#         self.input_string = input_string
#         self.delimiter = delimiter

#     def strLength(self) -> None:
#         # We print the total number of characters in the string.
#         print(f"The length of the string is {len(self.input_string)}")

#     def cutString(self) -> list[str]:
#         # Now we split the original string by the delimiter. We then return it as a list of words.
#         return self.input_string.split(self.delimiter)

#     def showWordAt(self, word_list: list[str], index: int) -> None:
#         # We print the word at the given index to sceen. Unless the index is out of range.
#         if 0 <= index < len(word_list):
#             print(f"The word at index {index} is {word_list[index]}")
#         else:
#             print("Index is out of range, focus.")

#     def showIndexAt(self, word_list: list[str], word: str) -> None:
#         # Lastly, we print the index of the given word in the list. Unless the index is out of range.
#         if word in word_list:
#             index = word_list.index(word)
#             print(f"The index for the word {word} is {index}")
#         else:
#             print(f"The word {word} was not found.")
