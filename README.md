# Boring Automation

Automation for unzipping files, sorting, finding files for download, backup and more.

The point is whenever I have something I want to automate I can come here to do it.

## Known Issues

1. Sorting: can't move files that already exist in the new folder.


## TODO

1. Unzip files
1. Find filetypes
1. Check if serie or movie.
1. Move to the appropiate folder.
1. Get data from IMDbPY to check if movie/serie?
1. Check if a file has subtitles?


1. Extract movie name.
1. Check if movie.
1. Check if it has any subtitles files or in video.
1. Move & rename folder
1. Downloads the subtitle


Try using MediaInfo OR ffmpeg (ffmpeg seems to be the best) to check if it has subtitles.

## Assets

1. [Dump of subtitle data](https://dl.opensubtitles.org/addons/export/)
1. [Download Dump of subtitle data](https://dl.opensubtitles.org/addons/export/subtitles_all.txt.gz)

## Installations

Create a venv `python -m venv .venv` //Name the folder whatever you want.

Activate it - Win: `source .venv/Scripts/activate` <!--  Mac: `source .venv/bin/activate` -->

### Requirements

`pip freeze > requirements.txt` - Create the requirements.txt
`pip install -r requirements.txt` - Installs it.