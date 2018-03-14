import urllib.request
from urllib import parse
import json

#quote() 和 unquote()
#forecast_24h 1
#index 
#status 200
#tips，observe	
wheather_keywords={
	'alarm':'天气预警:',
    'airconditioner': "空调指数",
    "allergy":"过敏指数",
	"carwash": "洗车指数",
	"chill":"风寒指数",
	"clothes": "穿衣指数",
	"cold":  "感冒指数",
	"comfort":"舒适度指数",
	"diffusion":"空气污染扩散指数",
	"drying": "晾晒指数", 
	"heatstroke": "中暑指数",
	"makeup":  "化妆指数",
	"sports": "运动指数",
	"traffic":  "交通指数",
	"ultraviolet": "紫外线强度指数",
	"umbrella": "雨伞指数"
        }
today_weather_keyword={"time": "今天为","day_weather": "白天",
	"day_wind_direction": "风向",
	"day_wind_power": "风力",
	"max_degree": "最高温",
	"min_degree": "最低温",
	"night_weather": "晚上",
	"night_wind_direction": "风向",
	"night_wind_power": "风力"
	}
def get_wethear_from_wisqqcom(province,city):
	province=parse.quote(province)
	city=parse.quote(city)
	url_data='http://wis.qq.com/weather/common?source=pc&weather_type=observe%7Cforecast_24h%7Cindex%7Calarm%7Ctips&province='+province+'&city='+city+'&county=&callback='
	with urllib.request.urlopen(url_data) as response:
		str = response.read().decode('UTF-8','strict')
		return json.loads(str)
def get_wethear_info_text(province,city):
	dict=get_wethear_from_wisqqcom(province,city)
	if dict['status']!=200:
		return '获取%s天气失败,请重试'%city
	today=dict['data']['forecast_24h']['1']
	msg=''
	for k,v in today_weather_keyword.items():
		
		msg+=v+':'+today[k]+','
	#print (msg)
	
	today_tips=dict['data']['index']
	tips=''
	for k,v in wheather_keywords.items():
		if k=='alarm':
			continue
		tips+=v+today_tips[k]['detail']
	if dict['data']['alarm'] != '':
		tips=wheather_keywords['alarm']+'无,'+tips
	#print(tips)
	return '正在为你播报'+province+city+'天气'+msg+tips+'播报结束！'

 
	
	
