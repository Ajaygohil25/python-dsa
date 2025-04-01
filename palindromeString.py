class palindrome:
    def ispalindrome(self, string):
        if not string or len(string) == 0:
            return True
        left, right = 0, len(string)-1
        while left < right:

            while (left < right and not self.isAlpha(string[left])):
                left = left + 1
            while (left < right and not self.isAlpha(string[right])):
                right = right - 1

            if self.lowercase(string[left]) != self.lowercase(string[right]):
                return False

            left += 1
            right -= 1
        return True


    def isAlpha(self,ch):
        return('A' <=ch <='Z') or ('a' <=ch<='z') or ('0'<=ch<='1')
    
    def lowercase(self,ch):
        if 'A' <=ch<= 'Z':
            return chr(ord(ch)+32)
        return ch

    




if __name__ == '__main__':
    checker = palindrome()
    input_string = "0 Madam, in Eden, I'm Adam 0"
    result = checker.ispalindrome(input_string)
    print("Is string palindrome : ",result)
    
