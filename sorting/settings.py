from configparser import ConfigParser

# --- Description ---
# For creating a .ini file with data.

config = ConfigParser()

config["DEFAULT"] = {
    "last_subtitle_download": "2024-02-01",
}

with open("settings.ini", "w") as file:
    config.write(file)