text = "abbclllppak"
if text[0:3] == "abc":
    text = text.replace("abc", "www")
else:
    text += "zzz"

print(text)