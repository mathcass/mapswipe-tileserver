#!/usr/bin/env python3
"""Implements a simple tile server for MapSwipe.

"""

from collections import namedtuple, Counter
import os

import mercantile
from flask import Flask, Response
import requests

Tile = namedtuple('Tile', ['x', 'y', 'z'])

BING_KEY = os.environ.get('BING_KEY', None)
if not BING_KEY:
    raise RuntimeError('Missing configuration environment variable BING_KEY')

tile_counter = Counter()


class BingTile:
    key = BING_KEY

    def __init__(self, *tile):

        if len(tile) == 1:
            tile = tile[0]
        else:
            tile = Tile(*tile)

        quadkey = mercantile.quadkey(tile)
        self.url_fmt = f'http://t0.tiles.virtualearth.net/tiles/a{quadkey}.jpeg?g=854&mkt=en-US&token='

    @property
    def url(self):
        return self.url_fmt + str(self.key)


app = Flask(__name__)


@app.route("/tile/<int:x>/<int:y>/<int:z>/")
def tile(x, y, z):
    t = Tile(x, y, z)
    tile_url = BingTile(t).url
    r = requests.get(tile_url)
    image = r.content
    tile_counter[t] += 1
    return Response(image, mimetype='image/jpeg')


@app.route("/count/<int:x>/<int:y>/<int:z>/")
def tile_count(x, y, z):
    t = Tile(x, y, z)
    count = tile_counter[t]
    return f'Tile {x}, {y}, {z} has been seen {count} times'
