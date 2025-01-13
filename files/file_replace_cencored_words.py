words = ["bad","donkey","ganda","bawalat"]

with open("files/cen_words.txt","r") as f:
    content = f.read()

for word in words:
        content = content.replace(word,"#" * len(word))

with open("files/cen_words.txt", "w") as f:
    f.write(content)