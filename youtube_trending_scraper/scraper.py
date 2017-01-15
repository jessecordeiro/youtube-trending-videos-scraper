import requests
import json
import html
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


class Scraper:
	"""
	Scraper for the trending page on YouTube.
	"""

	URL = "https://www.youtube.{0}/feed/trending"

	@staticmethod
	def scrape(country_code="com"):
		json_array = []

		try:
			response = requests.get(Scraper.URL.format(country_code))
		except ConnectionError as err:
			json_array.append({"error": str(err)})
			return json.dumps(json_array)

		soup = BeautifulSoup(response.text, "html.parser")
		trending_videos = soup.find_all(attrs={"class": "expanded-shelf-content-item"})
		for video_element in trending_videos:
			video_obj = dict()
			thumbnail = video_element.find(attrs={
					"class": ["yt-thumb", "video-thumb"]
					}).find(attrs={"class": "yt-thumb-simple"}).find("img")
			# Fallback on data-thumb attr if present to avoid capturing gif instead of jpg
			if thumbnail.get("data-thumb") is not None:
				video_obj["video_thumbnail"] = thumbnail["data-thumb"]
			else:
				video_obj["video_thumbnail"] = thumbnail["src"]
			title_content = video_element.find(attrs={"class": "yt-lockup-title"})
			link_meta = title_content.find("a")
			video_obj["video_url"] = link_meta.get("href")
			video_obj["video_title"] = link_meta.get("title")
			video_obj["video_time"] = title_content.find(attrs={"class": "accessible-description"}).string.split(": ")[1][:-1]

			profile_content = video_element.find(attrs={"class": "yt-lockup-byline"})
			profile_meta = profile_content.find("a")
			video_obj["profile_url"] = profile_meta.get("href")
			video_obj["profile_name"] = profile_meta.string

			meta_info = video_element.find(attrs={"class": "yt-lockup-meta-info"})
			video_obj["upload_date"] = meta_info.contents[0].string
			video_obj["view_count"] = meta_info.contents[1].string.split(" ")[0]

			description_content = video_element.select("div.yt-lockup-description")
			video_description = ""
			if len(description_content) > 0:
				video_description = description_content[0].text
			video_obj["video_desc"] = html.escape(str(video_description))
			json_array.append(video_obj)

		return json.dumps(json_array, sort_keys=True)
