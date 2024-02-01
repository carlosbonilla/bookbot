def main():

  book_path = "books/frankenstein.txt"
  number_of_words = 0
  number_of_letters = 0

  with open(book_path, "r") as f:
      book = f.read()
  
  number_of_words = count_words(book)
  number_of_letters = count_letters(book)

  print_report(book_path, number_of_words, number_of_letters)

def count_words(book):
  words = book.split()

  return len(words)

def count_letters(book):
   letters = {}

   for each_letter in (book):
      key = each_letter.lower()
      if key in letters:
        letters[key] += 1
      else:
        letters[key] = 1

   return letters
   
def print_report(book_path, number_of_words, number_of_letters):
  
  letters_report = []
  
  for letter in number_of_letters:
    letters_report.append((letter, number_of_letters[letter]))

  print(f"--- Begin report of {book_path} ---")
  print(f"{number_of_words} words found in the document")
  print("")

  for each_letter in sorted(letters_report, key=lambda x: x[1], reverse=True):
    if each_letter[0].isalpha():
      print(f"{each_letter[0]}: {each_letter[1]}")

  print("--- End report ---")
main()