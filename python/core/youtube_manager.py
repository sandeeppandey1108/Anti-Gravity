"""
ANTIGRAVITY YouTube Channel Manager
Uses YouTube Data API v3 OAuth2 credentials to upload, update branding, and read analytics.
Adapted from the user's provided channel manager structure. 
"""

import pickle
from pathlib import Path

BASE_DIR = Path(__file__).parent

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    HAS_GOOGLE_API = True
except ImportError:
    HAS_GOOGLE_API = False

SCOPES = [
    'https://www.googleapis.com/auth/youtube',
    'https://www.googleapis.com/auth/youtube.upload',
    'https://www.googleapis.com/auth/youtube.force-ssl'
]

def get_authenticated_service():
    if not HAS_GOOGLE_API:
        return None

    creds = None
    token_path = BASE_DIR / 'token.pickle'
    client_secret = BASE_DIR / 'client_secret.json'

    if not client_secret.exists():
        return None

    if token_path.exists():
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(client_secret), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return build('youtube', 'v3', credentials=creds)

def upload_video(video_path, title, description, tags, category_id="22", privacy="public"):
    youtube = get_authenticated_service()
    if not youtube:
        return None

    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id,
            'defaultLanguage': 'en',
            'defaultAudioLanguage': 'en'
        },
        'status': {
            'privacyStatus': privacy,
            'selfDeclaredMadeForKids': False
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part='snippet,status', body=body, media_body=media)

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Progress: {int(status.progress() * 100)}%")

    return response.get('id')

def get_channel_analytics():
    youtube = get_authenticated_service()
    if not youtube:
        return None

    response = youtube.channels().list(part='statistics,snippet', mine=True).execute()
    if not response.get('items'):
        return None

    ch = response['items'][0]
    stats = ch['statistics']
    return {
        'name': ch['snippet']['title'],
        'subscribers': stats.get('subscriberCount', 0),
        'views': stats.get('viewCount', 0),
        'videos': stats.get('videoCount', 0)
    }
