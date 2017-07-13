

def fibboncaci(n):
  if n in [1, 2]:
    return 1
 
  seq = [1, 1]
  while len(seq) < n:
	   print seq[0] + seq[1]
	   seq.append(seq[0] + seq[1])
  return seq[len(seq) - 1]
 
print fibboncaci(1)
print fibboncaci(2)
print fibboncaci(10)
 
 
def is_palindrome(word):
  first_half = None
  second_half = None
 
  if len(word) % 2 == 0:
    first_half = len(word) / 2
    second_half = len(word) / 2
 
  else:
    first_half = (len(word) / 2) + 1
    second_half = len(word) / 2
    print first_half
    print second_half

    first_half = word[:first_half]  
    second_half = word[second_half:]
    second_half = second_half[::-1]

    print first_half
    print second_half 

 
  if first_half == second_half:
     print word + ' is a palindrome!'
  else:
     print word + ' is not a palindrome...'

  
is_palindrome('kayak')
is_palindrome('race car')
is_palindrome('katniss evedreen')



