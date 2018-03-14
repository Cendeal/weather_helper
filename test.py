import model.map_db as db
import base.weather as weather
import pyttsx3
#baidu_3args={
#	'app_id':'',
#	'api_key':'',
#	'secret_key':''
#}
#weather.config['avata_key']=''
#weather.config['baidu_3args']=baidu_3args
#db.initdata('zh_map.db','map.txt') 城市地图数据库建立与初始化

city=input('城市:')

province=db.search_province_by_city('zh_map.db',city)
if province!='':
	#weather.info(province,city) #阿凡达
	#data=weather.info_by_wisqqcom(province,city) #腾讯
	#print('已保存为%s'%data)
	
	##以下是pyttsx3语音，不是百度ai语音
	engine = pyttsx3.init()
	msg=weather.get_text(province,city)
	#打印天气预报信息
	print(msg)
	engine.say(msg)
	engine.runAndWait()
else:
	print('获取失败')
