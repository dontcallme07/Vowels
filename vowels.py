import sys
text = sys.argv[1]
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)