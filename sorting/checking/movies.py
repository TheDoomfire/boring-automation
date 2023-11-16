import re

def get_movie_name(file_name):
    # Define a regular expression pattern to match movie names
    # Examples: "movie name (2013) [720p]" or "strange.world.2022.1080p.webrip.hevc.x265.rmteam"
    pattern = re.compile(r'^(.+?)(?:\s*\(\d{4}\))?[\s\.\[\(_]*(?:\d{3,4}p)?.*$')

    # Use the pattern to match and extract the movie name
    match = pattern.match(file_name)
    
    if match:
        return match.group(1).strip()
    else:
        return None