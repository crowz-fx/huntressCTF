# MatryoshkaQR


## Steps
```bash
wget https://huntress.ctf.games/files/53881786dd23c23cb50807b8361e4582/qrcode.png

# run file and some others
file qrcode.png
exiftool qrcode.png

# looks okay, open it with phone camera, it shows bytes for what looks like a png

# use python to encode back into the png
python encode.png

# open png, another barcode, use phone camera to show flag value

```

## Flag
```
flag{01c6e24c48f48856ee3adcca00f86e9b}
```
