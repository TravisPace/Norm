def norm1(vector):
  result = 0
  for i in range(len(vector)):
    result = result + abs(vector[i])
  return result

def norm2(vector):
  result = 0
  for i in range(len(vector)):
    result = result +abs(vector[i])**2
  result = result**.5
  return result

def norm3(vector):
  result = 0
  for i in range(len(vector)):
    if result <= abs(vector[i]):
      result = abs(vector[i])
  return result
