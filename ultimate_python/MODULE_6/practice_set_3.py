spam_message=["Make a lot of money", "buy now", "subscribe this", "click this", "Write a program to detect these spams"]

message=input("enter the message ").lower()
detected_message=[text for text in spam_message if text in message]

if detected_message:
    print("This is a spam message",",".join(detected_message))

else:
    print("This is not a spam message ")