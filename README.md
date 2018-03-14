## 须知说明
* ####天气来源
 *  [DT阿凡达数据](http://avatardata.cn/),需要api_key
 *  [腾讯天气](http://tianqi.qq.com/index.htm),无需key
* ####语音来源
 * [百度Ai开放平台](http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top)(需要申请key,在线合成mp3文件,文本长度有限制，但声音好听)
 * [pyttsx3语音库](https://pypi.python.org/pypi/pyttsx3)(不用在线转语音,不生成mp3文件,直接播放,声音一般)
##环境
- python 3.+
- 库依赖
```
# baidu-aip==2.2.0.0
# certifi==2018.1.18
# chardet==3.0.4
# idna==2.6
# pypiwin32==223
# pyttsx3==2.7
# pywin32==223
# requests==2.18.4
# urllib3==1.22
#一步安装方法:需要到[我的项目]下载req.txt
pip install -r req.txt
```
## 文件结构
```
│  map.txt//创建城市数据表
│  test.py//测试运行文件
│  zh_map.db//国内省市数据库
├─base
│  │- avata_weather.py//DT阿凡达数据模块实现
│  │- baidu_ai_voice.py//百度语音合成接口处理模块
│  │- weather.py//主要是天气信息的百度ai语音合成模块
│  │- wisqqcom_weather.py//腾讯天气数据解析模块     
│  
└─model
    │- map_db.py//国内省市数数据库模块
```
## 示例图片
![test.JPG](https://upload-images.jianshu.io/upload_images/4413333-bf326df275666b43.JPG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 关键代码
### - wisqqcom_weather.py
  * 获取腾讯天气的json数据
```
def get_wethear_from_wisqqcom(province,city):
    #parse.quote()这个函数调用很重要，主要是将字符串转为url编码
	province=parse.quote(province)
	city=parse.quote(city)
	url_data='http://wis.qq.com/weather/common?
	source=pc&weather_type=observe%7Cforecast_24h%7
	Cindex%7Calarm%7Ctips&province='+province+'&city='+city+'
	&county=&callback='
	with urllib.request.urlopen(url_data) as response:
		str = response.read().decode('UTF-8','strict')
		return json.loads(str)
```
 *  腾讯天气数据组合成需要的天气预报文本:
```
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
```
### -baidu_ai_voice.py
* 百度Ai 语音合成与保存
```
def translate_voice(content_data,filename):
	print (baidu_3args)
	client = AipSpeech(baidu_3args['app_id'], baidu_3args['api_key'], baidu_3args['secret_key'])
	#对文本长度进行检测，截取区间为0-512，然后进行拼接，直到长度小于512
	while len(content_data)>512:
		content =content_data[0:512]
		print (content)
		result  = client.synthesis(content, 'zh', 1, {'vol': 12,})
		if not isinstance(result, dict):
			with open(filename, 'ab+') as f:
				f.write(result)
		else:
			return False
		content_data=content_data[512:len(content_data)]
		#print(content_data)
	#剩余的或者小于512的一段直接合成
	result  = client.synthesis(content_data, 'zh', 1, {'vol': 12,})
	if not isinstance(result, dict):
			with open(filename, 'ab+') as f:
				f.write(result)
			return True
	else:
			return False
```
### -test.py
* 如果要测试百度ai语音的weather.info_by_wisqqcom请自己把baidu_3args的参数配置好，赋值给weather.config['baidu_3args']
* 同样如果要获取阿凡达的天气请配置config['avata_key']的值,调用函数为`weather.info(province,city) `
* 注意config['avata_key']，weather.config['baidu_3args']不需要同时配，看你的需求
```
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
```
## 其他
+ 对于为什么要创建数据库的原因是,因为查询天气时需要省份参数也需要城市参数，为了实现输入城市直接匹配省份而建立了省和城市两个数据表
+  使用百度ai语音合成注意事项:
```

联网调用http接口 。[REST API] 仅支持最多512字（1024 字节)的音频合成，合成的文件格式为mp3。
没有其他额外功能。
如果需要使用离线合成等其它功能，请使用Android或者iOS 合成 SDK
请严格按照文档里描述的参数进行开发。请注意以下几个问题：
1.  合成文本长度必须小于1024字节，如果本文长度较长，可以采用多次请求的方式。切忌不可文本长度超过限制。
2.  语音合成 rest api初次申请默认请求数配额 200000次/天，如果默认配额不能满足需求，请申请提高配额。
3.  必填字段中，严格按照文档描述中内容填写。
```

## 项目地址
[weather_helper by Cendeal](https://github.com/Cendeal/weather_helper)
