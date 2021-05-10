#palindrome string

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "madam or nurses run"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
