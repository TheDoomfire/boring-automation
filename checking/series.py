import re

def extract_season_episode(filename):
    # Check for 's01e02' format
    match = re.search(r's(\d+)e(\d+)', filename, re.IGNORECASE)
    if match:
        season = match.group(1)
        episode = match.group(2)
        return int(season), int(episode)

    # Check for 'Season 1 Episode 02' format
    match = re.search(r'season (\d+) episode (\d+)', filename, re.IGNORECASE)
    if match:
        season = match.group(1)
        episode = match.group(2)
        return int(season), int(episode)

    else:
        return None, None