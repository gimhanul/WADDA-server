from django.shortcuts import render
from .models import Sight
import json
import datetime
from django.core.exceptions import ImproperlyConfigured
import requests

def weather():
    weather_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'    
    
    with open('secrets.json') as secret_file:
        secretkey = json.load(secret_file)
    service_key = secretkey["SERVICE_KEY"]

    now = datetime.datetime.now()
    #(년, 월, 일, 시, 분, 초, 머있음또)
    base_date = now.strftime('%Y%m%d')
    
    nx = 96
    ny = 76

    if now.hour<5 or (now.hour==5 and now.minute<=10): # 2시 11분~5시 10분 사이
        base_time="0200"
    elif now.hour<8 or (now.hour==8 and now.minute<=10): # 5시 11분~8시 10분 사이
        base_time="0500"
    elif now.hour<=11 or now.minute<=10: # 8시 11분~11시 10분 사이
        base_time="0800"
    elif now.hour<14 or (now.hour==14 and now.minute<=10): # 11시 11분~14시 10분 사이
        base_time="1100"
    elif now.hour<17 or (now.hour==17 and now.minute<=10): # 14시 11분~17시 10분 사이
        base_time="1400"
    elif now.hour<20 or (now.hour==20 and now.minute<=10): # 17시 11분~20시 10분 사이
        base_time="1700"
    elif now.hour<23 or (now.hour==23 and now.minute<=10): # 20시 11분~23시 10분 사이
        base_time="2000"
    else: # 23시 11분~23시 59분
        base_time="2300"

    payload = "serviceKey=" + service_key + "&" +\
        "numOfRows" + 290 + "&" +\
        "dataType=json" + "&" +\
        "base_date=" + base_date + "&" +\
        "base_time=" + base_time + "&" +\
        "nx=" + nx + "&" +\
        "ny=" + ny
    
    res = requests.get(weather_url + payload)

    items = res.json().get('response').get('body').get('items')

    data = dict()
    for item in items['item']:
        print('item')



def q(request, question_id):
    return

def sight(request, sight_id):
    sight = Sight.objects.get(id = sight_id)
    print(sight.tags)

    context = {
        's': sight
    }
    return render(request, 'sight.html', context)
