# Nightmare on Hunt Street

This one is a multi-step challenge so different format, one zip for all parts is needed

## Steps

```bash
wget https://huntress.ctf.games/files/d4f1c0244518fc5429dd130388e6c8c7/logs-parts1-5.zip
unzip logs-parts1-5.zip

# geta handful of .evtx files which are event logs

# open in event viewer, see it doesn't show or parse "properly"

# then be a dumbass and take a couple days to wonder why... then lookup proper evtx file parsing

# find https://github.com/omerbenamram/evtx
# dump evtx files as json so we can do nice jq queries
evtx_dump -o json System.evtx > system.evtx.json
evtx_dump -o json Application.evtx > application.evtx.json
evtx_dump -o json Security.evtx > security.evtx.json

# now read/grep through things to answer the questions

```

## Flags

### What is the IP address of the host that the attacker used?

```bash
grep IpAddress security.evtx.json | sort | uniq -c
```

```
10.1.1.42
```

### How many times was the compromised account brute-forced?

```bash
# kinda guessed this
grep "FailureReason" security.evtx.json | sort | uniq -c
```

```
32
```

### What is the name of the offensive security tool that was used to gain initial access?

```
psexec
```

### How many unique enumeration commands were run with?

```

```

### What password was successfully given to the user created?

```bash
# returns a few, but can see the longer ones was failed as didn't meet reqs
grep "/ADD" security.evtx.json | sort | uniq -c
```

```
Susan123!
```
