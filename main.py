def main():

  number_of_words = 0

  with open("books/frankenstein.txt", "r") as f:
      book = f.read()
  
  number_of_words = count_words(book)
  number_of_letters = count_letters(book)

  print(number_of_words)
  print(number_of_letters)



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
   

main()