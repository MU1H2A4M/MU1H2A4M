fav_languages = {}

for i in range(4):
    name = input(f"Enter friend {i+1}'s name: ")
    language = input(f"Enter {name}'s favorite language: ")

    if name in fav_languages:
        fav_languages[name].append(language)  # Append to the list if name exists
    else:
        fav_languages[name] = [language]  # Create a new list

print("\nFavorite languages dictionary:")
print(fav_languages)
