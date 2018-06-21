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
  '''
  This function calculates the infinity norm. Result is the norm of the vector. For every element in the vector, the algorithim takes the
  absolute value of the element. If the element is bigger, then the algorithim takes the number as the new result. If the element is
  smaller than the previous element, then the algorithim keeps the previous result. The algorithim goes until there are no more
  elements in the list.
  '''
  result = 0
  for i in range(len(vector)):
    if result <= abs(vector[i]):
      result = abs(vector[i])
  return result
