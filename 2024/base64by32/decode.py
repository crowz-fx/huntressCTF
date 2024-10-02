import base64

contents=""
with open("base64by32", "rb") as f:
    contents = f.read()

for i in range(32):
    contents = base64.b64decode(contents)

print(contents.decode("utf-8"))
