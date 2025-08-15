#count the number of vowels and consonants in as tring
text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = consonant_count = 0
for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonant:", consonant_count)
