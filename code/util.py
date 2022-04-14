import os

def generateCharsList(chars):
  newChars = []
  for char in chars:
    num = chars[char]
    for i in range(num):
      newChars.append(char)

  return newChars

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)