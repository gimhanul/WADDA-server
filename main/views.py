from typing import ContextManager
from django.shortcuts import redirect, render
from .models import Sight, Banner, Question, Choice
import json
import datetime
from django.core.exceptions import ImproperlyConfigured
import requests


#home
def weather():
    weather_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?'    
    
    with open('secrets.json') as secret_file:
        secretkey = json.load(secret_file)
    service_key = secretkey["SERVICE_KEY"]
    now = datetime.datetime.now()
    #(년, 월, 일, 시, 분, 초, 머있음또)
    nx = '96'
    ny = '76'

    if now.hour<2 or (now.hour==2 and now.minute<=10):
        now = now.today() - datetime.timedelta(days=1)
        base_time="2300"
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



    base_date = now.strftime('%Y%m%d')
    payload = "serviceKey=" + service_key + "&" + "numOfRows=" + "290" + "&" + "dataType=json" + "&" + "base_date=" + base_date + "&" + "base_time=" + base_time + "&" + "nx=" + nx + "&" + "ny=" + ny
    
    res = requests.get(weather_url + payload)

    items = res.json().get('response').get('body').get('items')
    
    data = []
    for item in items['item']:
        if item['category'] == 'PTY':
            #없음(0), 비(1), 비/눈(2), 눈(3), 소나기(4) 
            weather_code = item['fcstValue']

            if weather_code == '0':
                continue
            elif weather_code == '3':
                weather_state = 'snow'
            else:
                weather_state = 'rain'

        elif item['category'] == 'SKY':
        #맑음(1), 구름많음(3), 흐림(4)
            weather_code = item['fcstValue']

            if weather_code == '1':
                weather_state = 'sunny'
            else:
                weather_state = 'cloudy'
        
        elif item['category'] == 'SNO':
            fcstTime = item['fcstTime']
            data.append((fcstTime[:2], weather_state))

    return data


def home(request):
    banner = Banner.objects.all()
    sights = Sight.objects.all().order_by('-id')
    weathers = weather()
    context = {
        'banner' : banner,
        'sights' : sights,
        'weathers' : weathers,
    }
    return render(request, 'home.html', context)


#schedule
def schedule(request):
    return render(request, 'schedule.html')

def q(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question_id=question_id)
    context = {
        'question' : question,
        'choices' : choices,
    }

    if request.method == 'POST':
        question_id = question_id + 1
        if question_id >= 4:
            return redirect('/schedule') #나주엥수정
        return redirect('/q/%s' %question_id)


    return render(request, 'q.html', context)

#sights
def sights(request):

    query = request.GET.get('search', '')

    if (query == ''):
        all = Sight.objects.all()
    else:
        all = Sight.objects.filter(tags__name__in=[query])

    context = {
        'all': all,
        'search': query,
    }

    return render(request, 'sights.html', context)

def sight(request, sight_id):
    sight = Sight.objects.get(id = sight_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['rt'] == 'gym':
            request.user.gym.add(sight)
        elif data['rt'] == 'nogym':
            request.user.gym.remove(sight)
    context = {
        's': sight
    }
    return render(request, 'sight.html', context)



#gym
def gym(request):
    return render(request, 'gym.html')




