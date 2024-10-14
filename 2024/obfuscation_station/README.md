# Obfuscation Station

## Steps

```bash
wget https://huntress.ctf.games/files/1c3755690403e7eebcc1989c5e0c4a81/Challenge.zip
7z x -pinfected Challenge.zip

# get a ps1 file, copy b64 out, decode it
base64 -d b64_payload > b64_payload_decoded

file b64_payload_decoded # get 'data'

# look at values in xxd
xxd b64_payload_decoded > data

# now the rest of the command
# this nugget was clever, it returns 'Iex' -> $env:comspec[4,15,25]

# i run the non-fuck up your shit part and it output the flag
```

```powershell
echo (nEW-objECt  SYstem.iO.COMPreSsIon.deFlaTEStREAm( [IO.mEmORYstreAM][coNVERt]::FROMBAse64sTRING( 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA') ,[io.COmPREssioN.coMpreSSioNmODE]::DeCoMpReSS) | %{ nEW-objECt  sYStEm.Io.StREAMrEADeR($_,[TeXT.encodiNG]::AsCii)}|%{ $_.READTOENd()})
```

## Flag

```
flag{3ed675ef0343149723749c34fa910ae4}
```
