## Hidden Streams

## Steps

```bash
wget https://huntress.ctf.games/files/c246b46b496579bf4d4e88f6cd2111ac/Challenge.zip
unzip Challenge.zip

# get sysmon logs in evtx
evtx_dump -o json Sysmon.evtx > sysmon.evtx.json

# think the key is to do with the 'streams', got a bit lucky searching for 'PowerShell'
# saw the "Contents" looks like b64, decoded and in the money

grep "Contents" sysmon.evtx.json
# "Contents": "ZmxhZ3tiZmVmYjg5MTE4MzAzMmY0NGZhOTNkMGM3YmQ0MGRhOX0=  ",

echo -n "ZmxhZ3tiZmVmYjg5MTE4MzAzMmY0NGZhOTNkMGM3YmQ0MGRhOX0=" | base64 -d
```

## Flag

```
flag{bfefb891183032f44fa93d0c7bd40da9}
```
