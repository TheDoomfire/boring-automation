import os
import re

# --- Description ---
# Renames all subtitle files to their corresponding video file.


# TODO: Import this instead. Its not renaming.
def extract_season_episode(filename):
    # Check for 's01e02' format
    patterns = [
        r's(\d+)e(\d+)', # s01e01
        r'season (\d+) episode (\d+)', # season 1 episode 1
        r'(\d+)x(\d+)', # 01x01
        ]
    
    for pattern in patterns:
        match = re.search(pattern, filename, re.IGNORECASE)
        if match:
            season = match.group(1)
            episode = match.group(2)
            return int(season), int(episode)

    else:
        return None, None


def rename_subtitles(folder_path):
    subtitle_extension = ".srt"
    video_extensions = [".mp4", ".mkv"]
    video_files = [file for file in os.listdir(folder_path) if file.endswith(tuple(video_extensions))]
    subtitle_files = [file for file in os.listdir(folder_path) if file.endswith(subtitle_extension)]

    for video_file in video_files:
        video_base_name, video_extension = os.path.splitext(video_file)
        video_season, video_episode = extract_season_episode(video_base_name)
        
        if video_season and video_episode:
            for subtitle_file in subtitle_files:
                subtitle_base_name, subtitle_extension = os.path.splitext(subtitle_file)
                subtitle_season, subtitle_episode = extract_season_episode(subtitle_base_name)
                
                if subtitle_season == video_season and subtitle_episode == video_episode:
                    subtitle_path = os.path.join(folder_path, subtitle_file)
                    new_subtitle_name = f"{video_base_name}.srt"
                    new_subtitle_path = os.path.join(folder_path, new_subtitle_name)
                    os.rename(subtitle_path, new_subtitle_path)
                    break


def main():
    folder_p = r"D:\Videos\Series\Game Of Thrones\Season 6"
    rename_subtitles(folder_p)


if __name__ == '__main__':
    main()
