#to print the frequency of maximum
name=input("Enter a string: ")
print("the original string: " + name)
freq={}
for i in name:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
 
# finding the character with maximum frequency
max_char = max(freq, key=freq.get)
print("The maximum of all characters in name is : " + (max_char))         
