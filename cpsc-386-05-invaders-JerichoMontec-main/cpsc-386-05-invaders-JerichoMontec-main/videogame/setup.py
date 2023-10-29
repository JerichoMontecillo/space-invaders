""" Simple setup.py """

from setuptools import setup

setup_info = {
    "name": "videogame",
    "version": "0.1",
    "description": "A package to support writing games with PyGame",
    "author": "Jericho Montecillo",
    "author_email": "jerichomontec@csu.fullerton.edu",
    "bullet_credit": "joemaya on OpenGameArt.org",
    "ship_credit": "jlunesc on OpenGameArt.org",
    "enemies_credit": "Atrus on OpenGameArt.org"
}

setup(**setup_info)