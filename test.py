import requests
import bs4
import xmltodict
import json

def get_xml(url):
   _xml = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _xml = resp.text
   return _xml

URL = 'http://220.95.178.158:82/trainruninfo.aspx?lineno=1'

xml_type = get_xml(URL)

#xml형식의 데이터를 dict형식으로 변환
rD = xmltodict.parse(xml_type)
print(rD)
print("")

# dict 형식의 데이터를 json으로 변환
# rDJ = json.dumps(rD)
# print(rDJ)
# print("")

# json 형식을 dict형식으로 변환
# rDD = json.loads(rDJ)
# print(rDD)
# print("")

# msg = rDD['Humetro']['LineNo']
# print(len(msg))
# print("")
print('Line : ' + rD['Humetro']['LineNo']['@Line'])
print('StandardTime : ' + rD['Humetro']['LineNo']['@StandardTime'])
print('Train count : ' + str( len(rD['Humetro']['LineNo']['Train'])))

for tr in rD['Humetro']['LineNo']['Train']:
    print(tr['TrainNo'], tr['Direction'], tr['StationName'], tr['StationNo'], tr['Status'], tr['ChangeTime'])



# #get
# resp = requests.get('http://220.95.178.158:82/trainruninfo.aspx?lineno=2')
# # print(resp.text)
# # print(resp.json()) #json에서 사용 
# print("status_code : " + str(resp.status_code))
# print(resp.encoding)

# html = resp.text
# bs = bs4.BeautifulSoup(html, 'html parser' )
# tags = bs.find_all("Train")
# print(tags)

