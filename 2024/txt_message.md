# Text Message

## Steps

```bash

# mentions dns and link to od which prints octal

# dig all DNS records for the domain, see the TXT which looks like octal
dig TXT ctf.games +short

# put the TXT record into cyberchef with a "From Octal"

```

## Ouput

```
146 154 141 147 173 061 064 145 060 067 062 146 067 060 065 144 064 065 070 070 062 064 060 061 144 061 064 061 143 065 066 062 146 144 143 060 142 175
```

## Flag

```
flag{14e072f705d45882401d141c562fdc0b}
```
