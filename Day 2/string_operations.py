#String : It is immutable data type, encloses wih quotes

from platform import architecture
text1 = "Python"
text2 = " Developer"

#common operations
print(len(text1))
print(text1[-1])
print(text2[1:3])

#built-in methods
#1.Case Modification
#2.Searching and Replacing
#3.Cleaning and Splitting
#4.Verfication and Boolean checks


#1.Case Modification
text = "hello World"
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

#2.Searching and Replacing
phrase = "banana"
print(phrase.find("an"))
print(phrase.count("a"))
print(phrase.replace("a", "o"))

#3.Cleaning and Splitting
spaced = "  code "
print(spaced.strip())
csv = "apple,banana,cherry"
splitter = csv.split(",")
print("-".join(splitter))

#4.Verification and boolean checks
text = "12"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.startswith("1"))
print(text.endswith("2"))