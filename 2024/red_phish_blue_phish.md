# Red Phish Blue Phish

## Steps
```bash
# spin up instance
nc -C -vvv challenge.ctf.games 31960



EHLO pyrchdata.com
MAIL FROM: harder@pyrchdata.com
RCPT TO: swilliams@pyrchdata.com
DATA
354 End data with <CR><LF>.<CR><LF>
Date: Wed, 30 September 2024 06:04:34
From: harder@pyrchdata.com
Subject: You're being fired unless you fill this out
To: swilliams@pyrchdata.com
Body




EHLO pyrchdata.com
MAIL FROM: swilliams@pyrchdata.com
RCPT TO: swilliams@pyrchdata.com
DATA 


```

## Flag
```

```