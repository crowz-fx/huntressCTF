# I Can't SSH

## Steps

```bash
wget https://huntress.ctf.games/files/983408e881ef2245efc4e2e68b43fc15/id_rsa

# jump on box, pwd userpass
ssh -i id_rsa -p 30442 user@challenge.ctf.games

# get the error "Load key "id_rsa": error in libcrypto" which means the priv
# key is incorrectly formatted, check for ctrl+m, eol etc.

# was missing EOL, edit, new line and remove, save

ssh -i id_rsa -p 30442 user@challenge.ctf.games

# works!
cat flag.txt
```

## Flag

```
flag{ee1f28722ec1ce1542aa1b486dbb1361}
```
