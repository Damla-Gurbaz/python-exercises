"""  Write a method that takes an array of consecutive (increasing)
  letters as input and that returns the missing letter in the 
  array. You will always get an valid array. And it will be 
  always exactly one letter be missing. The length of the array
   will always be at least 2. The array will always contain 
   letters in only one case.

Example:
['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!) """


def missing_letter(s):
  alfabe="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(len(s)-1):
    if s[i] in alfabe:
      y=alfabe[alfabe.index(s[i])+1]
      if y==s[i+1]:
        pass
      else:
       return y
print(missing_letter(['a','b','c','d','f']))
print(missing_letter(["O","Q","R","S"]))