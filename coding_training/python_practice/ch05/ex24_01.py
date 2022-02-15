# 연습문제 24. 애너그램 점검

print("Enter two strings and I`ll tell you if they are anagrams:")

firstStr = input("Enter the first string: ")

secondStr = input("Enter the second string: ")

def isAnagram (str1, str2):
	compareLen = lambda str3, str4:	True if len(str3) == len(str4) else False

	while compareLen(str1, str2):
		char0 = str1[0]
		str1 = str1.replace(char0, '')
		str2 = str2.replace(char0, '')

		if not len(str1):
			if not len(str2):
				return True

	return False

print('"{}" and "{}" are{} anagrams.'.format(firstStr, secondStr, '' if isAnagram(firstStr, secondStr) else ' not'))