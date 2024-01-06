# Extensions
EXTENSION_VIDEOS = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp']
EXTENSION_AUDIOS = ['.mp3', '.wav', '.ogg', '.aac', '.flac', '.m4a', '.wma', '.amr', '.mid', '.midi', '.ac3']
EXTENSION_ARCHIVES = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2', '.tar.xz']
EXTENSION_SUBTITLES = [ # TODO: Add more here.
    ".srt",
    ".vtt",
    ".sub",
    ".ass",
]

# Lists
#LIST_UPLOADERS = ["yifi", "GalaxyRG"]
LIST_ALL_SPECIAL_CHARACTERS = ['.', ',', '!', ':', ';', '"', "'", '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '/', '?', '[', ']', '{', '}', '|', '\\']
LIST_VIP_ACTORS = [
    'will forte',
    'ben affleck'
]

# Regular Expression
#RE_WEBSITE = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
RE_VIDEO_PIXELS = "(480|720|1080|1440|2160|7680)" # 2K: (1440p) 4K: (2160p) 8K: (7680)
RE_YEAR = "((18|19|20|21)[0-9]{2})"
RE_SERIE = "([Ss]\d{2}[Ee]\d{2})" #"(?i)(s\d{1,2}e\d{1,2}|(\d+of\d+)|(season\s?\d+\s?episode\s?\d+))"
RE_NUMBERS = "\d+"
# ^season (\d+) episode (\d+)$


# Paths
PATH_MOVIES = r"D:\Videos\Movies"
PATH_SERIES = r"D:\Videos\Series"
PATH_ALL_SUBTITLES = r"D:\Documents\GitHub\boring-automation\sorting\data" # TODO: Make this base on the python file somehow. Because it dosent work in other machines.

# Names
NAME_ALL_SUBTITLES = "subtitles_all.txt"
NAME_ALL_SUBTITLE_ZIP = "subtitles_all.txt.gz"