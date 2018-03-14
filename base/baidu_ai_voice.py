from aip import AipSpeech
#content_data 文本内容
#baidu_3args	字典
#baidu_3args.keys()={'app_id','api_key','secret_key'}
#filename	输出文件名
baidu_3args={'app_id':'', 'api_key':'', 'secret_key':''}
def translate_voice(content_data,filename):
	print (baidu_3args)
	client = AipSpeech(baidu_3args['app_id'], baidu_3args['api_key'], baidu_3args['secret_key'])
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
	result  = client.synthesis(content_data, 'zh', 1, {'vol': 12,})
	if not isinstance(result, dict):
			with open(filename, 'ab+') as f:
				f.write(result)
			return True
	else:
			return False
def translate_voice_bytes(content_data):
	global baidu_3args
	client = AipSpeech(baidu_3args['app_id'], baidu_3args['api_key'], baidu_3args['secret_key'])
	result  = client.synthesis(content_data, 'zh', 1, {'vol': 13,})
	if not isinstance(result, dict):
		return result
	else:
		return -1