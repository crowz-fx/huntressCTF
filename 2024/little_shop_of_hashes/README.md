# Little Shop of Hashes

This is another group of challenges using the same fileset

## Steps

```bash
wget https://huntress.ctf.games/files/10cbe497410970911b21629afba4baf5/little_shop_of_hashes_logs.zip

unzip little_shop_of_hashes_logs.zip

# more event log files... yay not

evtx_dump -o json hosts/HOSTA/System.evtx > host_a_system.evtx.json
evtx_dump -o json hosts/HOSTA/Application.evtx > host_a_application.evtx.json
evtx_dump -o json hosts/HOSTA/Security.evtx > host_a_security.evtx.json

evtx_dump -o json hosts/HOSTB/System.evtx > host_b_system.evtx.json
evtx_dump -o json hosts/HOSTB/Application.evtx > host_b_application.evtx.json
evtx_dump -o json hosts/HOSTB/Security.evtx > host_b_security.evtx.json

# some dumb shit to note, tool dumps escaped win paths so
#   C:\\Users\\DeeDee\\Documents\\nc.exe
# is actually the answer but like
#   C:\Users\DeeDee\Documents\nc.exe
```

## Flags

### What is the name of the service that the attacker ran and stopped, which dumped hashes on the first compromised host?

```
remote registry
```

### What lateral movement technique did the threat actor use to move to the other machine?

```
pass the hash
```

### What is the full path of the binary that the threat actor used to access the privileges of a different user with explicit credentials?

```
C:\Users\DeeDee\Documents\runasc.exe
```

### How many accounts were compromised by the threat actor?

```
3
```

### What is the full path of the binary that was used to attempt a callback to the threat actor's machine?

```
C:\Users\DeeDee\Documents\nc.exe
```
