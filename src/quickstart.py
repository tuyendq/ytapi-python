import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
YOUTUBEAPI_KEY = os.getenv("YOUTUBEAPI_KEY")

def get_video_details(video_id):
    """Get video details"""
    youtube = build('youtube', 'v3', developerKey=YOUTUBEAPI_KEY)
    request = youtube.videos().list(part='snippet,statistics', id=video_id)
    response = request.execute()
    return response

def get_channel_details(forUsername):
    """Get Channel details"""
    youtube = build('youtube', 'v3', developerKey=YOUTUBEAPI_KEY)
    request = youtube.channels().list(part="snippet,contentDetails,statistics",
        forUsername=forUsername
    )
    response = request.execute()
    return response

def get_channel_details_channelid(channel_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBEAPI_KEY)
    request = youtube.channels().list(part='snippet,statistics', id=channel_id)
    response = request.execute()
    return response

def get_playlist_details(playlist_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBEAPI_KEY)
    request = youtube.playlists().list(part='snippet', id=playlist_id)
    response = request.execute()
    return response


# video_id = 'dQw4w9WgXcQ'
# details = get_video_details(video_id)
# print(details)

# channelUsername = 'ConDuongKienTinh'
# channelUsername = 'DrWynnTranOfficial'
# channelUsername = 'GoogleDevelopers'
# details = get_channel_details(channelUsername)
# print(details)

channel_id = 'UCsXVk37bltHxD1rDPwtNM8Q'
channel_id = 'UCLRScapcqNPayCby65I_tWg'  #@tuyendangquoc
channel_id = 'UChMzQMqYNb6pY1E5XLBkxtQ'  #@ConDuongKienTinh
details = get_channel_details_channelid(channel_id)
print(details)

# playlist_id = 'PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'
# details = get_playlist_details(playlist_id)
# print(details)