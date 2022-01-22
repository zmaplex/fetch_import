# Fetch-import

It is convenient to quickly import Python packages from the network.

## Docs

Example remote module file is  `"https://fastly.jsdelivr.net/gh/zmaplex/fetch_import@main/example/sets.py"
`

### @im_fetch 

Using this Decorator, you can load resources remotely as conveniently as **import**.

1. Replace `import`
```python
import sets
sets.def_function()
```
Equivalent:
```python
from fetch_import import im_fetch

url = "https://fastly.jsdelivr.net/gh/zmaplex/fetch_import@main/example/sets.py"

@im_fetch(url)
def main():
    sets.def_function()

```
2. Replace `from package import *`
```python
from sets import *

obj = ObjectClass()
def_function()
```
Equivalent:
```python
from fetch_import import im_fetch

@im_fetch(url,["*"])
def main():
    obj = ObjectClass()
    def_function()
```
3. Replace `from package import attr1,attr2`
```python
from sets import ObjectClass,def_function

obj = ObjectClass()
def_function()
```
Equivalent:
```python
from fetch_import import im_fetch

@im_fetch(url,["ObjectClass","def_function"])
def main():
    obj = ObjectClass()
    def_function()
```
## How to use？

**step 1**

```bash
pip install fetch-import
pip -r requirements.txt
```

**step 2**

```python
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

```
