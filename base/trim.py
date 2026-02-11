def trim(s):
    if not s:
        return s

    start = 0
    while start < len(s) and s[start] == " ":
        start += 1
    
    # 全是空格的情况
    if start == len(s):
        return ""
    
    end = len(s) - 1
    while end > start and s[end] == " ":
        end -= 1
    
    return s[start : end + 1]


# 测试:
if trim("hello  ") != "hello":
    print("测试失败!")
elif trim("  hello") != "hello":
    print("测试失败!")
elif trim("  hello  ") != "hello":
    print("测试失败!")
elif trim("  hello  world  ") != "hello  world":
    print("测试失败!")
elif trim("") != "":
    print("测试失败!")
elif trim("    ") != "":
    print("测试失败!")
else:
    print("测试成功!")
