# 参考: https://qiita.com/bakira/items/00743d10ec42993f85eb

import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

url = "https://api.twitter.com/1.1/statuses/update.json"

print("What's happening?")
tweet = input(">> ")
print("Tweeting...")

params = {"status": tweet}

res = twitter.post(url, params=params)  # post送信

if res.status_code == 200: # 正常に投稿できた場合
    print("Success!")
else:  # 正常に投稿できなかった場合
    print("Failed! : %d" % res.status_code)
