import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0"
                  ".3809.100 Safari/537.36"
    }

url = "https://www.toutiao.com/api/pc/feed/?max_behot_time=1565260555&category=__all__&utm_source=toutiao&widen=1&" \
      "tadrequire=false&as=A1B5BD942C65341&cp=5D4C45A364E15E1&_signature=wRuZvBAdnGHIV-Opw8soycEbma"
session = requests.session()
print(url)
res = session.get(url=url, headers=headers)
print(res.text)
