import requests

r = requests.get("http://books.toscrape.com")

sourceCode = r.text

begin = sourceCode.find("<strong>", 0)
end = sourceCode.find("</strong>", begin)
stringCut = sourceCode[begin+len("<strong>"):end]

print(stringCut)