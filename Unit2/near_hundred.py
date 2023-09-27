def near_hundred(n):
  #get distance from 100
  hundred_distance = abs(100-n)
  #get distance from 200
  two_hundred_distance = abs(200-n)
  #If either distance is 10 or less, return True
  if hundred_distance <= 10 or two_hundred_distance <= 10:
    return True
  else:
    return False
