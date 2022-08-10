# Author: Colin
# Python text-based luhn algorithm 

# takes in a credit card number
def findsum(cardNum):
  newList = []
  numList = []
  sumDigits = 0
  first = False
  # take out last digit of the sequence
  for x in range(len(cardNum) - 1):
    newList.append(cardNum[x])
  # starting from the end of the sequence (excluding the last digit)
  for x in reversed(newList):
    if first:
      numList.append(x)
      first = False
      continue
    # double the value of every other digit
    if not first:
      x = int(x) + int(x)
      x = str(x)
      numList.append(x)
      first = True
      continue
  # add the values up
  for x in numList:
    if len(x) == 1:
      sumDigits = sumDigits + int(x)
    # for two-digit numbers, add the tens and ones digit separately
    elif len(x) == 2:
      sumDigits = sumDigits + int(x[0]) + int(x[1])
  return sumDigits

# using the calculated sum and credit card number, verify
def luhn(sumDigits, cardNum):
  sumDigits = int(sumDigits)
  checkDigit = int(cardNum[-1])
  if 10 - (sumDigits%10) == checkDigit:
    return True
  else:
    return False


# takes in credit card number and returns its validity
def cccheck():
  # user inputs credit card number
  cardNum = input("Please enter a credit card number: ")
  sumDigits = findsum(cardNum)
  # returns true or false
  valid = luhn(sumDigits, cardNum)
  if valid:
    print("The credit card number you entered passed the Luhn Check and is therefore a valid credit card number!")
  if not valid:
    print("The credit card number you entered failed the Luhn Check. It's not valid, did you make a typo?")


cccheck()

  