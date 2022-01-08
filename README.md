# youtube uploader

As I couldn't find a working youtube uploader in github which does not use the
youtube API, I've implemented my own one.

## Setup

```bash
git clone https://gitlab.com/vargab95/youtube-uploader.git
cd youtube-uploader
python3 setup.py install
```

## Example code

```python3
from youtube_uploader.upload import YouTubeUploader, Video
from youtube_uploader.webdriver import UndetectedChromeWebDriver


webdriver = UndetectedChromeWebDriver()
uploader = YouTubeUploader(webdriver)

v = Video(path="video path",
          thumbnail="thumbnail path",
          title="title",
          description="description",
          category=1,
          tags="tag1, tag2")

uploader.login()
uploader.upload(v)
```
