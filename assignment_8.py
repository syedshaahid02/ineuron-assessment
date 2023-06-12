# -*- coding: utf-8 -*-
"""Assignment-8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V8iKH4Chqy45m0JdRqkwmm303iAgaPGf
"""

#1
def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

    return dp[m][n]

s1 = "sea"
s2 = "eat"
print(minimumDeleteSum(s1, s2))

#2
def isValid(s):
    stack = []
    wildcard_count = 0

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            elif wildcard_count > 0:
                wildcard_count -= 1
            else:
                return False
        elif char == '*':
            wildcard_count += 1

    while stack and wildcard_count > 0:
        stack.pop()
        wildcard_count -= 1

    return len(stack) == 0

s = "()"
print(isValid(s))

#3
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]

word1 = "sea"
word2 = "eat"
print(minDistance(word1, word2))

#5
def compress(chars):
    n = len(chars)
    if n == 0:
        return 0

    write = 0  # Pointer to write the compressed characters
    count = 1  # Count of the current character
    prev_char = chars[0]  # Previous character

    for i in range(1, n):
        if chars[i] == prev_char:
            count += 1
        else:
            chars[write] = prev_char
            write += 1

            if count > 1:
                count_str = str(count)
                for j in range(len(count_str)):
                    chars[write] = count_str[j]
                    write += 1

            prev_char = chars[i]
            count = 1

    # Write the last character and its count
    chars[write] = prev_char
    write += 1

    if count > 1:
        count_str = str(count)
        for j in range(len(count_str)):
            chars[write] = count_str[j]
            write += 1

    return write

chars = ["a", "a", "b", "b", "c", "c", "c"]
compressed_length = compress(chars)
print(compressed_length)  # Output: 6
print(chars[:compressed_length])  # Output: ["a", "2", "b", "2", "c", "3"]

#6
from collections import Counter

def findAnagrams(s, p):
    result = []
    p_freq = Counter(p)
    s_freq = Counter(s[:len(p)])

    if s_freq == p_freq:
        result.append(0)

    for i in range(len(p), len(s)):
      
        if s_freq[s[i - len(p)]] == 1:
            del s_freq[s[i - len(p)]]
        else:
            s_freq[s[i - len(p)]] -= 1

        s_freq[s[i]] += 1

        if s_freq == p_freq:
            result.append(i - len(p) + 1)

    return result

s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))

#7
def decodeString(s):
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append(current_string)
            stack.append(current_num)
            current_string = ""
            current_num = 0
        elif char == "]":
            num = stack.pop()
            prev_string = stack.pop()
            current_string = prev_string + num * current_string
        else:
            current_string += char

    return current_string

s = "3[a]2[bc]"
print(decodeString(s))

#8
def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False

    diffs = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diffs.append(i)

    return len(diffs) == 2 and s[diffs[0]] == goal[diffs[1]] and s[diffs[1]] == goal[diffs[0]]

s = "ab"
goal = "ba"
print(buddyStrings(s, goal))  # Output: True