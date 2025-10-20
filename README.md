# Yt-Buddy

A Python script to track new videos from multiple YouTube channels and log their links. The script compares previously stored video IDs with current ones and reports any new uploads.

## Features

- Fetches video IDs from multiple YouTube channels concurrently using threads.
- Logs new video links with timestamps and channel names.
- Updates a local data file with the latest video IDs for future comparisons.
- Uses yt-dlp for retrieving video information.

## Requirements

- Python 3.12+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## How to Run

### Install Dependencies
1. Clone this Repo
2. Install the required packages:
  ```
  pip install -r requirements.txt
  ```
3. Install yt-dlp. You can find the relavent information under:
   
    [yt-dlp Installation Guide](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#installation)

### Configuration
1. Semi-Constants:
```yaml
   data: data.csv # File to store video IDs
   threads: 10 # Number of threads to use
   channelLink: https://www.youtube.com/@ # Base URL for channels
   videoLink: https://www.youtube.com/watch?v= # Base URL for videos
```  
2. Custom
```yaml
   channel:  
    - SebastianLague # Add the channels you want to track
    - ...
```
3. Create the csv file you specified in config.cfg

### Run
You can run the script directly or wrap it in a small helper script for convenience.

#### *Example (Windows PowerShell or Batch)*
```Powershell
@echo off
REM This is a Wrapper for the Python skript with the same name

cd C:\Users\YOUR_USER\Documents\Python\yt_buddy

.\.venv\Scripts\python.exe  .\main.py
```

This allows you to start the program using a simple command:

```bash
yt-buddy
```

---
# Development Tasks
- Add Watchlater Storage
- Add Parameters via Typer 
  - Watchlater, Displays data 
  - Add, Add Link / ID to Watchlater
  - Rem, Remove Link / ID from Watchlater
  - FullScan (Default, adds new to Watchlater)