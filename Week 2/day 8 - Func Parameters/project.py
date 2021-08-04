alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def code(text, shift, direction):
    return_str = ''

    for letter in text:
      if letter in alphabet:
        if direction == 'encode':
          new_letter_index = alphabet.index(letter) + shift

          if new_letter_index > 25:
            new_letter_index -= 26
          return_str += alphabet[new_letter_index]
        else:
          new_letter_index = alphabet.index(letter) - shift

          if new_letter_index < 0:
            new_letter_index += 26
          return_str += alphabet[new_letter_index]  
      else:
        return_str += letter

    print(return_str)

keep_going = True

while keep_going:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  

  code(text, shift, direction)
  
  if input('Do you want to continue? Y or N ') == 'N':
    keep_going = False

