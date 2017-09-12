# -*- coding: utf-8 -*-
history_weather = {}
weather_info = {}

def getWeather(file_path = "E:\\py101-004\\chap1\\resource\\weather_info.txt"):
    data = {}
    try:
	    with open(file_path, 'r', encoding='utf-8') as f:
		    data_raw = f.readlines()
    except:
        return getWeather(input("找不到天气相关文件，请重新输入路径:"))
    else:
        for i in data_raw:
            data[i.split(',')[0]] = i.split(',')[1]
        return data
		
def printHelp():
    print(
	'''
	
	输入城市名，返回该城市的天气数据；
	输入h或help，打印帮助文档；
	输入history，打印查询历史；
	输入quit，退出程序。
	'''
	)
	
def inquiryWeather(city):
    try:
	    weather =weather_info[city]
    except KeyError:
        print("没有该城市信息")
        return 0
    else:
        print(city + "的天气情况是：" + weather)
        history_weather.update({city: weather})
        return {city: weather}
		
def printHistory():
    for city in history_weather:
        print(city + "\t" + history_weather[city])
		
def checkCommand():
    command = input("请输入指令或城市名：")
    if command == "help" or command =="h":
        printHelp()
    elif command == "history":
        printHistory()
    elif command =="quit":
        return 0
    else:
        inquiryWeather(command)
    return checkCommand()
	

weather_info = getWeather()
checkCommand()