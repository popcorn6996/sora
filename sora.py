from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Pexels API key
pexels_api_key = '4jAY2WJOL5dygyFcUTl5JxX1fggxo1zmRuYKtqnSfgtZPMHX5PKAcd3s'

@app.route('/process_input', methods=['POST'])
def process_input():
    try:
        # Get user input from the request
        user_input = request.json.get('user_input', '')

        # Process user input using spaCy
        # (You can replace this with your own logic)
        breakdown_components = user_input.split()

        # Fetch videos for each breakdown component from Pexels
        video_urls = fetch_videos_from_pexels(breakdown_components)

        return jsonify({'video_urls': video_urls})
    except Exception as e:
        return jsonify({'error': str(e)})

def fetch_videos_from_pexels(breakdown_components):
    video_urls = []

    for component in breakdown_components:
        # Use Pexels API to fetch videos based on the breakdown component
        pexels_url = f'https://api.pexels.com/videos/search?query={component}'
        headers = {'Authorization': pexels_api_key}

        response = requests.get(pexels_url, headers=headers)

        if response.status_code == 200:
            videos_data = response.json().get('videos', [])
            if videos_data:
                # Extract video URL (modify based on Pexels API response)
                video_url = videos_data[0].get('video_files', [])[0].get('link', '')
                video_urls.append(video_url)
    return video_urls

if __name__ == '__main__':
    app.run(debug=True)
