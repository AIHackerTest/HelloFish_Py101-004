from flask import Flask, url_for, render_template, request 
import requests

history_list = []
def fetch_weather(location):
	result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': 'a3gtzy7glcuzsxvh',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=5) 
	weather_result = result.json()
	weather_dict = weather_result['results'][0]
	city = weather_dict['location']['name']
	weather_now_text = '天气状况为：' + weather_dict['now']['text']
	weather_now_temperature = '气温：' + weather_dict['now']['temperature'] + '℃'
	weather_time = '更新时间为：' + weather_dict['last_update']
	weather = city + weather_now_text + weather_now_temperature + weather_time
	return weather 

app = Flask(__name__)
history_list = []

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/user_request')
def handle_request():
	try:
		if request.args.get('help') == "帮助":
			return render_template('help.html')
		elif request.args.get('query') == "查询":
			city = request.args.get('city')
			weather = fetch_weather(city)
			history_list.append(weather)
			return render_template('query.html', weather=weather)
		elif request.args.get('history') == "历史":
			return render_template('history.html', history_list=history_list)
	except KeyError:
		return render_template('404.html')
		
if __name__=='__main__':
	app.run(debug=True)