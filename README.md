# Yt-Buddy

A Python script to track new videos from multiple YouTube channels and log their links. The script compares previously stored video IDs with current ones and reports any new uploads.

## Features

- Fetches video IDs from multiple YouTube channels concurrently using threads.
- Logs new video links with timestamps and channel names.
- Updates a local data file with the latest video IDs for future comparisons.
- Uses yt-dlp for retrieving video information.

## Requirements

- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## How to Run

### Install Dependencies
1. Clone this Repo
2. Install the required Packages using
  ```
  pip install -r requirements.txt
  ```

### Configuration
