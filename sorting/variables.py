# Extensions
EXTENSION_VIDEOS = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp']
EXTENSION_AUDIOS = ['.mp3', '.wav', '.ogg', '.aac', '.flac', '.m4a', '.wma', '.amr', '.mid', '.midi', '.ac3']
EXTENSION_COMPRESSIONS = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2', '.tar.xz']
EXTENSION_SUBTITLES = [ # TODO: Add more here.
    ".srt",
    ".vtt",
    ".sub",
    ".ass",
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


