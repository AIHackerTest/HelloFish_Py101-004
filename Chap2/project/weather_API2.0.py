# 用request模块获取API数据
import requests
import json

def fetch_weather(location):
	location = user_input
	result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': 'a3gtzy7glcuzsxvh',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=15) 
	weather_result = result.json()
	if 'status' in weather_result.keys():
		response = '请输入正确的城市名称：'
		return response
	else:
		weather_dict = weather_result['results'][0]
		city = weather_dict['location']['name']
		weather_now_text = '天气状况为：' + weather_dict['now']['text']
		weather_now_temperature = '气温：' + weather_dict['now']['temperature'] + '℃'
		weather_time = '更新时间为：' + weather_dict['last_update']
		weather = city + weather_now_text + weather_now_temperature + weather_time
		return weather 
    
def print_help():
    help = '''
    欢迎使用天气查询MVP！
    输入城市名，返回该城市的天气数据；
    输入指令‘help’或者‘h’，打印帮助文档；
    输入指令‘history’，打印查询历史；
    输入指令‘quit’或者‘q’，打印查询历史并退出程序。
    '''
    return print(help)
    
def add_history():
    history.append(weather)
    return history 
    
def print_history():
    if len(history)==0:
        print('您还没有开始查询呢!')
    else:
        for i in range(len(history)):
            print(history[i])

print_help()
history = []
          
while True:
    user_input = input("请输入城市名称：")
    weather = fetch_weather(user_input)
    if user_input in ['quit', 'q']:
        print_history()
        break
    elif user_input in ['h']:
        print_help()
    elif user_input in ['history']:
        print_history()
    else:
        print(fetch_weather(user_input))
        add_history()