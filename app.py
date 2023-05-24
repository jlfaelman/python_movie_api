from flask import Flask, jsonify
import requests 
from decouple import config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


api_key = config('MOVIE_SECRET')
api_bearer = config('MOVIE_READ_ACCESS')
api_url = config('MOVIE_URL')
headers= {
    'X-RapidAPI-Key': 'b0d9fff961mshc8f0f17b7930582p1ceed1jsna0da1d3238ea',
    'X-RapidAPI-Host': 'moviesdatabase.p.rapidapi.com'
}


@app.route('/api/list')
def list_movies():
    try:
        url = api_url + '/titles'
        print(url)
        response = requests.get(url, headers=headers)
        data = response.json()
        return jsonify(data)  
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})  



@app.route('/api/list/search')
def search_movies():
    try:
        keyword = ""
        url = api_url + '/titles/search/keyword/'+keyword
        print(url)
        response = requests.get(url, headers=headers)
        data = response.json()
        return jsonify(data) 
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}) 



if __name__ == '__main__':
    app.run(debug=True)