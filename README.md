# mapswipe-tileserver

This implements a simple tile server to help count the number of times a particular tile has been seen. 

## Instructions

First, install the necessary requirements. 

Then, set the environment variables

* `FLASK_APP=app.py`
* `FLASK_DEBUG=1` (if you'd like to enable debugging)
* `BING_KEY` set to your Bing maps developer key

Now, run `flask run` to run the server. In development, you can visit the url [http://localhost:5000/tile/1/2/3/](http://localhost:5000/tile/1/2/3/) to see the actual tile. After you've visited a tile a few times, visit [http://localhost:5000/count/1/2/3/](http://localhost:5000/count/1/2/3/) to see the number of times it has been viewed.
