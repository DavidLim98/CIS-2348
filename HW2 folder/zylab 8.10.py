# David Lim, 1625277

user_input = input()
normal = ""
reverse = ""
for ch in user_input.lower():
    if ch != ' ':
        normal += ch
        reverse = ch + reverse
if normal == reverse:
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")
