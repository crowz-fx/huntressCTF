# Keyboard Junkie

## Steps

```bash
wget https://huntress.ctf.games/files/0e79939d78e993778da1bec62f146ca6/keyboard_junkie

# get a pcap file, open in wireshark

# install tshark

# found this guide, follow steps
# https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/usb-keystrokes

# get keystrokes
tshark -r keyboard_junkie -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keystrokes.txt

# get and run script, pops the flag
wget https://raw.githubusercontent.com/TeamRocketIst/ctf-usb-keyboard-parser/refs/heads/master/usbkeyboard.py
python usbkeyboard.py keystrokes.txt
```

## Flag

```
flag{f7733e0093b7d281dd0a30fcf34a9634}
```
