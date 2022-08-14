def rotate(s):
  word = s
  rotations = [s]
  for i in range(len(s)-1):
    character = s[i]
    word = word[1:] + character
    rotations.append(word)
  return(rotations)

def bwt(s, eof):
  s = s + eof
  rotations = rotate(s)
  rotations = sorted(rotations, key=str.lower)
  result = ''
  for i in rotations:
    result += i[-1]
  return(result)

def ibwt(s, eof):
  matrix = []
  for i in range(len(s)):
    matrix.append(s[i])
  for i in range(len(s)-1):
    temp = sorted(matrix.copy(), key=str.lower)
    for j in range(len(s)):
      matrix[j] += temp[j][-1]
  for i in matrix:
    if i[-1] == eof:
      word = ''.join(i)
      if eof != '':
        word = word[:-1]
      return(word)
