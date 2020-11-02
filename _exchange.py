import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

secilen_kur = input("İşlem yapacağınız Döviz Birimini Giriniz :")
para_biriminiz = input("Para Biriminizi Yazınız :")
nekadar = int(input(f"Ne kadar {secilen_kur} bozdurmak istiyorsunuz :"))

result = requests.get(api_url+secilen_kur)
result = json.loads(result.text)
print(result)
print("{0} = {1} {2} ".format(secilen_kur, result["rates"][para_biriminiz],para_biriminiz))
print("{0} {1} = {2} {3} ".format(nekadar, secilen_kur,nekadar*result["rates"][para_biriminiz],para_biriminiz))










