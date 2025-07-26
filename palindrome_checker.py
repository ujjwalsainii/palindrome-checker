while True:
    text = input("Enter a string (or type 'exit' to quit): ")
    if text.lower() == 'exit':
        print("Byebye!")
        break
    if text == text[::-1]:
        print("Palindrome!")
    else:
        print("Not a palindrome.")