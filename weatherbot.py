from bottle import route,run,request,Bottle
import requests
import json

app = Bottle()

# TOKEN for your team from Slack
TOKEN = ''
# openweathermap api access token
OWM_API_KEY=''

@app.route('/weatherin',method='POST')
def getweather():
    if request.form['token'] != TOKEN:
        reply = "Sorry, I cant answer you. You are not authorized."
    else:
        api_url='http://api.openweathermap.org/data/2.5/weather?id='+request.form['text']+'&mode=json&units=metric&APPID='+OWM_API_KEY
        try:
            response = requests.post(api_url)
        except requests.exceptions.ConnectionError as e:
            reply = "Can't reach openweathermap to get the weather data."
            return reply
        if response.status_code == 404:
            reply = ":interrobang: Looks like you have entered invalid City Id. The City Id's list can be found [here](http://openweathermap.org/help/city_list.txt). "
        elif response.status_code == 200:
            json_response = json.loads(response.text)
            reply=":thumbsup: The weather in "+json_response['name']+" is "+str(json_response['main']['temp'])+" degrees"
    return reply


if __name__ == '__main__':
    app.run(host='localhost')
