import requests
print("downloading with requests")
url = 'https://www.bestsign.cn/openpage/contractDownload.page?mid=ac3219a6e9664206a39894bd31b7762f&fsdid=1493792227436LLDL2&status=3&sign=IuiVpv0vnPKjX9EFYVvTrB%2F6LGCS%2B0bvMHV52JF9RSjBwlkEjF2df7jiINxRS%2FbkDlD6zmNl2pQM8uZaYCWrvydtIan4yKeYutiILU83VZceFJYg9AEEgKXGDYzidj1YaaM%2BABYW9EFn12frN9qwwQo1UjJadMZyncu%2FnTT0Ops%3D'
r = requests.get(url)
with open("E:\document\mine\渠道接入\贵阳农商行\合同模板\contract20170504.zip", "wb") as code:
     code.write(r.content)

print("download completed")