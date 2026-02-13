#a)count number of vowel in given string

string=input("Enter string")
vowels=0
for i in string:
   if i in 'aAeEiIoOuU':
      vowels = vowels+1
print("Number of vowels are:")
print(vowels)

#b) Count Length of string (donot use len() )

s ="python"
l= sum (1 for i in s)
print(l)

#c) Reverse string
s= "python is easiest language"
reverse=''.join(reversed(s))
print(reverse)
#d) Find and replace operation
s="python is powerful,python is fun"
res= s.replace("python","coding")
print(res)

#e) check whether string entered is a palindrome or not
s="madam"
rev= '' .join (reversed(s))
if s ==rev:
    print("yes")
else:
    print("no")
    


