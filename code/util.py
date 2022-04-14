def generateCharsList(chars):
  newChars = []
  for char in chars:
    num = chars[char]
    for i in range(num):
      newChars.append(char)

  return newChars