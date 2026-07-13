import re

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled


def extract_video_id(url_or_id: str) -> str:

    patterns = [
        r"(?:youtube\.com/watch\?v=)([^&]+)",
        r"(?:youtu\.be/)([^?]+)",
        r"(?:youtube\.com/embed/)([^?]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url_or_id)

        if match:
            return match.group(1)
    
    return url_or_id


def fetch_transcript(video_id: str) -> str:

    try: 

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id, languages=['en'])

        return " ".join(item.text for item in transcript)

    except TranscriptsDisabled:
        print("No captions available for this video.")
        return ""