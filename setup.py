#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="kanocreator",
      version="1.0",
      description="KanoCreator made using Qt",
      license="GPL",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="http://kano.me",
      keywords= "kano creator python raspberry computing",
      packages=find_packages(),
      entry_points = {
        'console_scripts': [
            'kanocreator = kanocreator.kanocreator:main',
        ],
      },
      zip_safe = True)