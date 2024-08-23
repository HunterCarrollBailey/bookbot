def openBook(file):
    with open(file) as f:
        return f.read()

def getNumWords(text):
    words = text.split()
    return len(words)

def countCharacters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    return characters

def listCs(characters):
    clist = [{'character': char, 'count': count} for char, count in characters.items()]
    clist.sort(key= lambda x: x['count'], reverse=True)
    return clist

def generateReport(text, filename):
    text = openBook(text)
    report = []
    report.append(f"--- Begin report of {filename} ---")
    report.append(f"{getNumWords(text)} words found in the document")
    for char in listCs(countCharacters(text)):
        report.append(f"The '{char['character']}' character was found {char['count']} times")
    report.append("--- End Report ---")
    return "\n".join(report)

print(generateReport('./books/frankenstein.txt', '/books/frankenstein.txt'))

