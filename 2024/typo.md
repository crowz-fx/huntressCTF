# Typo

## Steps

```bash
# Password is "userpass"
ssh -p 30178 user@challenge.ctf.games

# get a train lol, tried with -C to cat .bashrc, nothing of note in there

# force a sh not the default /bin/bash
ssh -p 30178 user@challenge.ctf.games -t /bin/sh

cat flag.txt
```

## Flag

```
flag{36a0354fbf59df454596660742bf09eb}
```
