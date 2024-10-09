# Ran Somewhere

## Steps

```bash
wget https://huntress.ctf.games/files/24195417a40ca879da23e0cc925872b1/ran_somewhere.eml

# pull apart the contents of the email, base64 decode them

# raw email content html
cat email_html_b64 | base64 -d > email_html_b64_decoded
# discover this url - https://sites.google.com/view/id-10-t/home?authuser=0

# attachments
cat company_logo.png_b64 | base64 -d > company_logo.png_b64_decoded.png

# 4e 6f 74 65 == Note.txt
cat note.txt_b64| base64 -d > note.txt_b64_decoded.txt
# file is in hex too, convert it, mentions find it lol with the clues

# 66 69 6e 64 20 69 74 20 79 65 74 == find it yet
cat find_it_yet_b64 | base64 -d > find_it_yet_b64_decoded
file find_it_yet_b64_decoded # it's a jpg

#run exiftool to see what data
exiftool find_it_yet_b64_decoded > find_it_yet_metadata.txt
# no location data, open image, try to reverse search it in google and others

```

## Flag

```


```
