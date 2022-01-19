from fetch_import import im_fetch


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


url = "https://fastly.jsdelivr.net/gh/zmaplex/fetch_import@main/example/youtube_downloader.py"
@im_fetch(url)
def main():
    yd = youtube_downloader.YoutubeDownloader()
    yd.run(**job_args)


if __name__ == '__main__':
    main()
