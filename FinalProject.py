#GROVEPI STUFF

import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('/GrovePi-EE250/Software/Python')
# This append is to support importing the LCD library.
sys.path.append('/GrovePi-EE250/Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import setRGB, setText_norefresh, setText

grovepi.set_bus("RPI_1")

#API STUFF
import requests

YOUTUBE_KEY = '7bb57b9a30msh6092dea03c45eb3p111033jsn380d3738f27c'  

#FLASK STUFF
from flask import Flask, jsonify, request
#from FinalProject import trending_channels

app = Flask(__name__)

def get_trending(querystring):
    url = "https://youtube-search-and-download.p.rapidapi.com/trending"
    headers = {
        "x-rapidapi-key": YOUTUBE_KEY,
        "x-rapidapi-host": "youtube-search-and-download.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    channel_names = []
    buf = ''

    if response.status_code == 200:
        json_trending = response.json()
        contents = json_trending.get('contents', [])

        print("Trending Videos:")
        for item in contents[:10]:
            video = item.get('video', {})
            channel_id = video.get('channelId', 'N/A')
            channel_name = video.get('channelName', 'N/A')
            length_text = video.get('lengthText', 'N/A')
            published_time = video.get('publishedTimeText', 'N/A')
            title = video.get('title', 'N/A')
            video_id = video.get('videoId', 'N/A')
            view_count = video.get('viewCountText', 'N/A')

            if channel_name != 'N/A':
                channel_names.append(channel_name)

            if len(channel_names)<=9:
                buf = buf + '#'
                setText_norefresh(buf)
                setRGB(225,165,0)
                setText_norefresh('\nLoading...')
            elif len(channel_names)==10:
                buf = buf + '##'
                setRGB(135,202,100)
                setText_norefresh('\nComplete!')

            print(f"""
            Title: {title}
            Channel Name: {channel_name} (ID: {channel_id})
            Length: {length_text}
            Published: {published_time}
            Views: {view_count}
            Video ID: {video_id}
            """)

    else:
        print(f"Error: {response.status_code}. Something went wrong.")
        error_messages = {
            400: "The server cannot process the request due to something that is perceived to be a client error.",
            401: "The request lacks valid authentication credentials for the target resource.",
            403: "Forbidden: Request is not authorized.",
            404: "Requested resource not found."
        }
        print(error_messages.get(response.status_code, "An unexpected error occurred."))

    return channel_names


def get_socials(querystring):
    
    url = "https://social-links-search.p.rapidapi.com/search-social-links"
    headers = {
        "x-rapidapi-key": YOUTUBE_KEY,
        "x-rapidapi-host": "social-links-search.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        json_response = response.json()
        data = json_response.get('data',{})
        first_items = {}

        for platform, links in data.items():
            if links:  # Check if the list is not empty
                first_items[platform] = links[0]
            else:
                first_items[platform] = None  # Assign None if the list is empty

        # Print the results
        for platform, link in first_items.items():
            print(f"{platform}: {link}")

    else:
        print(f"Error: {response.status_code} for Channel")
        error_messages = {
            400: "Client error occurred.",
            401: "Authentication credentials are missing or invalid.",
            403: "Request is not authorized.",
            404: "Requested resource not found."
        }
        print(error_messages.get(response.status_code, "An unexpected error occurred."))

#Flask routes
@app.route('/')
def home():
    with open('home.html', 'r') as html_file:  # Ensure home.html is in the same folder as this script
        content = html_file.read()
    return content
   # return "Welcome to Sifa and Evangelos' EE250 Project!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(trending_channels)

@app.route('/notes', methods=['POST'])
def submit_note():
    submitted_data = request.json
    return jsonify({"received": submitted_data, "message": "Data received successfully!"})  


if __name__ == '__main__':

    setText("")
   

    type = input("Enter type of trending video (n - now, mu - music, mo - movies, g - gaming): ").strip()
    hl = input("Enter the language for trending videos (e.g., en for English): ").strip()
    gl = input("Enter the country (e.g., US, UK, BE): ").strip()
    
    querystring = {"type": type, "hl": hl, "gl": gl}
    trending_channels = get_trending(querystring)

    for channel_name in trending_channels:
        querystring2 = {"query":channel_name,"social_networks":"facebook,tiktok,instagram,snapchat,twitter,youtube,linkedin,github,pinterest"}
        get_socials(querystring2)
        print()
    
    app.run(debug=True)



