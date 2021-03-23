import math
def binary_search_rotated(arr, key):
  #TODO: Write - Your - Code

  #Recursive binary search
  #Start with an array covering the original array
  #Compare key with the middle of the array
  #If key> middle divide right, and vice versa
  def recursive_binary(arr,low,high,key):  


    if low>high:
      return -1
   
    middle = low + int((high-low)/2)

    if arr[low]==key:
        return low
    if arr[high]==key:
       return high
    if key==arr[middle]:
      return middle
    if key>arr[middle]:
      low=middle
      
      return recursive_binary(arr,low,high,key)
    return recursive_binary(arr,low,middle,key)

  return recursive_binary(arr,0,len(arr)-1,key)
  # return -1
