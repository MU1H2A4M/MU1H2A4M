dict = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "पानी": "Water",
    "खुशी": "Happiness",
    "पढ़ाई": "Study",
    "भोजन": "Food",
    "मित्र": "Friend",
    "संगीत": "Music",
    "प्यार": "Love",
    "घर": "Home"
}

a=str(input("enter the words from your dictionary "))
translation=dict.get("the traanslation of your word from the list is",a)
print({translation})
