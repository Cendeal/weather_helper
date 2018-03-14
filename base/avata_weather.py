#天气预报查询接口
import requests
avata_key=''
#city 城市
#avata_key 阿凡达数据开发key
def showmsg(city):
	value={
		'key':avata_key,
		'cityname':city,
	}
	url='http://api.avatardata.cn/Weather/Query'
	js=requests.get(url,params=value).json()
    #显示时间
	s=''
	date=js['result']['realtime']
	s+=('地点:{0},日期：{1} ,农历：{2} ,时间为:{3}'.format(date['city_name'],date['date'],date['moon'],date['time']))
    #预报天气状况

	weather=js['result']['weather']
	#print(weather)
	dateline={'dawn':'早上','day':'白天','night':'晚上'}
	for k,v in weather[0]['info'].items():
		v[1]=''
		v[5]=''
		s+=('%s:%s。'%(dateline[k],v))
    #显示污染指数
	pm=js['result']['pm25']['pm25']
	s+=('今天污染指数：\npm25为{0}、 pm10为{1}, 污染等级{2}:{3}.\n生活建议：{4}'.format(pm['pm25'],pm['pm10'],pm['level'],pm['quality'],pm['des']))
    #显示生活建议
	info=js['result']['life']['info']
	f={'ziwaixian':'紫外线','kongtiao':'空调','wuran':'污染','ganmao':'感冒','xiche':'洗车','yundong':'运动', 'chuanyi':'穿衣'}
	for k,v in info.items():
		s+=('%s:%s,'%(f[k],v))

	return ('正在播报天气:%s,播报结束!')%s