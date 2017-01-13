## Youtube Trending Videos Scraper

This is a Python scraper for YouTube's trending feed of videos.

## Contents

* [Requirements/Installation](#req/install)
* [Usage](#usage)
* [Output](#output)
* [Contribute](#contribute)
* [License](https://github.com/jessecordeiro/youtube-trending-videos-scraper/blob/master/LICENSE)

## <a name="req/install"></a>Requirements/Installation

Follow the steps below to start an instance of Chatr within minutes

1. **Install requirement(s):**
  + [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
  + [pip](https://pip.pypa.io/en/stable/installing/)

2. **Clone repository:**

  ```bash
  git clone https://github.com/jessecordeiro/youtube-trending-videos-scraper.git
  cd youtube-trending-videos-scraper
  ```

3. **Install dependencies:**

  ```bash
  python setup.py develop
  ```

## <a name="usage"></a>Usage
```python
import youtube_trending_scraper

youtube_trending_scraper.Scraper.scrape()
```

## <a name="output"></a>Output
```js
[{
  "profile_name": "Lorem ipsum", 
  "profile_url": "/user/loremipsumdolor", 
  "upload_date": "1 day ago", 
  "video_desc": "Lorem ipsum dolor sit amet, hymenaeos sodales in, scelerisque at.",
  "video_thumbnail": "https://..",
  "video_time": "2:12", 
  "video_title": "Lorem ipsum dolor sit amet", 
  "video_url": "/watch?v=loR3MIpSUMgd", 
  "view_count": "3,151,740"
}]
```

## <a name="contribute"></a>Contribute
1. Fork the repository
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Implemented x feature'`
4. Push to the feature branch: `git push origin x-feature`
5. Open a pull request