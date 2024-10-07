import base64
import zlib

PAYLOAD = ""

with open("obfuscated.txt", "r") as f:
    PAYLOAD = f.read()

for i in range(51):
    # reverse
    if i != 50:
        PAYLOAD = PAYLOAD[::-1]

    # b64 decode
    PAYLOAD = base64.b64decode(PAYLOAD)

    # zlib decompress
    PAYLOAD = zlib.decompress(PAYLOAD)

    # they are python execs, so extract the payload only
    PAYLOAD = str(PAYLOAD).split("b'")[1].split("')")[0]

print(PAYLOAD)
