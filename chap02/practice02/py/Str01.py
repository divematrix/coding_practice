str = input("문자열을 입력해 주세요")

# 문자열 포매팅 방법 1
# print("What is the input string? %s\n%s has %d characters." % (str, str, len(str)))

# 문자열 포매팅 방법 2 - https://blockdmask.tistory.com/424
print("What is the input string? {0}\n{0} has {1} characters.".format(str, len(str)))
