from setuptools import setup

setup(name='youtube-trending-videos-scraper',
      version='1.0',
      description='Python script to scrape videos that are trending on YouTube',
      url='https://github.com/jessecordeiro/youtube_trending_scraper',
      author='Jesse Cordeiro',
      author_email='jesse.cordeiro@mail.utoronto.ca',
      license='MIT',
      packages=[
        'youtube_trending_scraper'
      ],
      install_requires=[
        'apscheduler',
        'gitpython',
        'datetime',
        'bs4',
        'requests'
      ])
