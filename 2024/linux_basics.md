# Linux Basics

## Steps

```bash
# start instance
nc -vvv challenge.ctf.games 30586

answer # to list all questions
answer 0 # to answer the question 0
```

## Questions

### Question 0: What's your home directory?

```
cat /etc/passwd
```

```
/home/user
```

### Question 1: Search the man pages. What command would you use to generate random permutations?

```
shuf
```

### Question 2: On what day was /home/user/myfile.txt modified? Use the date format 2019-12-31

```
1997-08-29
```

### Question 3: How big is /home/user/myfile.txt, in kilobytes? Round to the nearest whole number.

```
ls -lah # h is human friendly format
```

```
22
```

### Question 4: What user owns the file /home/user/myfile.txt

```
ls -la
# or
stat myfile.txt
```

```
root
```

### Question 5: What's the 3-digit octal permissions of the file /home/user/myfile.txt? (e.g 777)

```
ls -la
# or
stat myfile.txt
```

```
754
```

### Question 6: What is the user id of 'admin'?

```
cat /etc/passwd
```

```
1338
```

### Question 7: There is a user 'john' on the system. Can they write to /home/user/myfile.txt? (yes/no)

```
no
```

### Question 8: Can the 'admin' user execute /home/user/myfile.txt? (yes/no)

```
# admin user in admin group, group has x perms
ls -la
```

```
yes
```

### Question 9: Which user on the system, except for you, root, admin and john, can execute /home/user/myfile.txt?

```
cat /etc/passwd # check users in 1338 group
```

```
rose
```

### Question 10: /home/user/myfile.txt looks like a txt file, but it actually isn't. What kind of file is it?

```
file myfile.txt
```

```
jpeg
```

## Flag

```
flag{8873fe66f8e7a6019d7d71261864f6c5}
```
