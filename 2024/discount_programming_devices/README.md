# Discount Programming Devices

## Steps

```bash
wget https://huntress.ctf.games/files/f20261ff13c0ee646374b15fa8a0466f/oops.py

# can see it does a b64 decode on a reversed string and then zlib decompress

# make another py file to do the reverse, discover it's run multiple times

# sneaky last one, on the 50th go it's not reversed! almost got me lol

python revserse.py
```

## Flag

```
flag{2543ff1e714bC2eb9ff78128232785ad}
```
