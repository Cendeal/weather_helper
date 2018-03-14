from base  import avata_weather
from base  import baidu_ai_voice
from base  import wisqqcom_weather
import os
import time
config={}
config['avata_key']=''
config['baidu_3args']={}
#通过阿凡达信息平台天气合成语音,需要提供key
def info(city):
	if(config['avata_key']==''):
		print('请配置config[\'avata_key\']!!!')
		return ''
	avata_weather.avata_key=config['avata_key']
	
	msg=avata_weather.showmsg(city)
	name=int(time.time())
	baidu_ai_voice.translate_voice(msg,('yubao%s.mp3'%str(name)))
	return ('yubao%s.mp3'%str(name))
#获取腾讯天气信息
def get_text(provice,city):
	return wisqqcom_weather.get_wethear_info_text(provice,city)
#用时间戳保存名字,并返回文件名
def info_by_wisqqcom(provice,city):
	if(config['baidu_3args']=={}):
		print('请配置config[\'baidu_3args\']!!!')
		return ''
	baidu_ai_voice.baidu_3args=config['baidu_3args']
	msg=get_text(provice,city)
	name=int(time.time())
	baidu_ai_voice.translate_voice(msg,('yubao%s.mp3'%str(name)))
	return ('yubao%s.mp3'%str(name))

def clear(filename):
	os.remove(filename)
	print('clear %s'%filename)

	