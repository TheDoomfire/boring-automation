import re

def extract_season_episode(file_name):
    # Check for 's01e02' format
    match = re.search(r's(\d+)e(\d+)', file_name, re.IGNORECASE)
    if match:
        season = match.group(1)
        episode = match.group(2)
        return int(season), int(episode)

    # Check for 'Season 1 Episode 02' format
    match = re.search(r'season (\d+) episode (\d+)', file_name, re.IGNORECASE)
    if match:
        season = match.group(1)
        episode = match.group(2)
        return int(season), int(episode)

    else:
        return None, None