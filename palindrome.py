class Solution:
    def isPalindrome(self, s): #type s: string #return type: boolean
    #input = input() # Write code below to complete prompt
        #input=s[-1]
        txt = s[::-1]
        #print(txt)
        if(txt==s and len(s)>6):
            return True
        else:
            return False
#TODO: Write code below to return a boolean value with the solution to the prompt. pass de
def main(): 
    tc1 = Solution() 
 
    # for i in range(0,len(input)):

    inp=input()
    print(tc1.isPalindrome(inp)) 
if __name__ == "__main__": 
    main()