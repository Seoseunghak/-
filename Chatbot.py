import json
import bs4
import requests
import os
import json
import urllib
from datetime import datetime
from bs4 import BeautifulSoup

year=datetime.today().year
month=datetime.today().month
month=str(month)
day=datetime.today().day 
if len(str(month)) == 1 :
    month="0"+str(month)
fanta=str(year)+str(month)+str(day)
url="http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=JGMlPMEcTuNV8sbu5JRfjhwjPXMdCv1OJ1qQefm0vVuKWGKtGHAcJEWtm63GOVyMQYAcI%2BoXUBe0nsJ4w3RiZw%3D%3D&pageNo=1&numOfRows=10&startCreateDt="+fanta+"&endCreateDt="+fanta #call back url
cola=requests.get(url).text
sida=BeautifulSoup(cola, "html.parser")
items=sida.find("items")
for item in items : 
    hapgae=item.find("gubun").string
    if hapgae == "합계" :
        incdec=item.find("incdec").string
        print("일일 확진자수 : "+incdec+"명\n")
    if hapgae == "부산" :
        incdec=item.find("incdec").string
        print("부산 확진자수 : "+incdec+"명\n")
    if hapgae == "합계" :
        deathcnt=item.find("deathcnt").string
        print("누적 사망자 : "+deathcnt+"명")
