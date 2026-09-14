# Video/Audio Downloader

This Python script allows you to download videos and audio from a youTube link. It uses the `pytube` library to fetch and 
download the media content. The video merged the audio and video streams into a single file, while the audio is saved as an MP3 file.

## Requirements

- Python 3.6 or higher
- `pytube` library (installable via pip)

## Installation

1. Clone this repository or download the source code.

2. Install the required packages using pip:
```bash
   pip install -r requirements.txt
```
3. Run the script with a copied YouTube URL to download the video or audio.

## Usage

First, you need to copy the YouTube link of the video you want to download. Then, run the script and follow the prompts:

```bash
python videoaudio.py
```
Then, paste the copied YouTube link when prompted. The script will ask you whether you want to download the video or audio. If you 
download the video, it will be saved in the "videos" folder, and if you download the audio, it will be saved in the "audios" folder. 

