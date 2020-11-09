def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
  
  
# main code
number = int(input("Please enter any number : "))
print("Binary Number is : ", bin(number))
print("Number of 1 in bits is : " , countSetBits(number))
