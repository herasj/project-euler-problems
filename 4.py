# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = 0
product = 0
def isPalindrome(num):
    num = str(num)
    for i in range(0,int(len(num)/2)):
        if(num[i:i+1] != num[len(num)-i-1:len(num)-i]):
          return False
    return True


for x in range(100,1000):
    for y in range(100,1000):
        product = x*y
        if(product>palindrome and isPalindrome(product)):
            print('Palindrome: ', product, ' X: ',x,' Y: ',y)
            palindrome = product
