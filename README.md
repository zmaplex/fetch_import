# fetch_import

It is convenient to quickly import Python packages from the network.

## How to use？

```python
from fetch_import import import_attr


# equivalent "from youtube_downloader import YoutubeDownloader"
@import_attr(
    "https://raw.githubusercontent.com/zmaplex/fetch_import/main/example/youtube_downloader.py",
    "YoutubeDownloader")
def main():
    ydl_opts = {
        'f': 'bestvideo+bestaudio[ext=m4a]',
        'ratelimit': 1024 * 1024 * 1024,
        'merge-output-format': 'mp4'}

    job_args = {
        "job_id": "63ba4e4e67cf417ab6a27365cecabec5",
        "plugin_args": {
            "url": "https://www.youtube.com/watch?v=UvuJx7rVUxg",
            "ydl_opts": ydl_opts
        }
    }
    yd = YoutubeDownloader()
    yd.run(**job_args)
```