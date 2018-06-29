def norm1(vector):
  result = 0
  for i in range(len(vector)):
    result = result + abs(vector[i])
  return result

def norm2(vector):
  '''
  This function calculates the two norm. The result is the norm of the vector. This takes the absolute value of every element and squares
  them. This adds the result of the after each element is squared. Then, the function takes the square root of the result to return
  the two norm.
  '''
  result = 0
  for i in range(len(vector)):
    result = result +abs(vector[i])**2
    #Takes each element and squares the element and adds them together.
  result = result**.5
  #This takes the result and raises it to the half power, which is equivalent to a square root.
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
