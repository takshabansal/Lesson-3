#input a word
text=str(input("Enter a string beside this message"))

#Reverse String
# using step value -1 to iterate in reverse
revText=text[::-1]
text=revText
print("Reverse of String is:")
print(text)
print(text.upper())