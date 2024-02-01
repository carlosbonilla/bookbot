def main():

  number_of_words = 0

  with open("books/frankenstein.txt", "r") as f:
      file_contents = f.read()
  
  number_of_words = count_words(file_contents)

  print( number_of_words )


def count_words(text):
  words = text.split()

  return len(words)
   

main()