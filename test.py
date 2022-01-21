import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse
class dd:
    def req(self):
  #把第二步中获取到的 timestamp和sign拼接到URL中


        timestamp = str(round(time.time() * 1000))
        secret = 'SEC95e0c54ee2482e44124f1feecccf5b1f05a72aafb2c896028f967f32ac968e14'  # 这里填的就是上面获取的加签密钥
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url = 'https://oapi.dingtalk.com/robot/send?access_token=6f353ab3203878bcf0ba3360a2748c40cb6c9f1c452a96fe59f6d7634a0b4369' \
               '&timestamp=' + timestamp + \
               '&sign=' + sign
        h = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        #d里面的at参数是需要at的人参数，只有at的人存在这个参数里面才会@成功
        d = json.dumps({"msgtype": "text", "text": {"content": "准备下班拉，记得打卡哦爸爸@13047050282"},
                            "at": {"atMobiles": ["13047050282"], "isAtAll": "false"}})
        req = requests.post(url, data=d, headers=h)
        print(req.text)

if __name__ == '__main__':
    dd().req()
