# AsciiTtv

A simple twitch.tv to console ascii converter. Made in under a day, so don't mind the weirdness.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage-tips)
- [TODO]
- [Config file](#config)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Clone, create a virtual environment (python 3.11)

```sh
git clone https://github.com/DuhonDoesCode/AsciiTtv.git
cd AsciiTtv
python3.11 -m venv .venv
source .venv/bin/activate
```

Install all requirements, edit [config.json](#config), run with utf8 flag

```sh
pip install -r requirements.txt
python3.11 -Xutf8 stream.py
```

## Usage tips
At watchable resolutions, the program uses a lot of symbols at once, thus requiring you to zoom out. To do so, either use `ctrl+scroll wheel`, or `crtl+-`.

## TODO
Add a color toggle, and actual interfacing

## Config

Config options are streamer, resolution and tileset. 

- Streamer: Specifies which stream to put in the terminal. Use the same as its shown in the url (all lowercase).
- Resolution: specifies how many pixels will be skipped (so higher = smaller).
- Tileset: What symbols to use for ASCII display. For correct behavior, make it a single string with no spaces. To the left the "white" tiles, making a gradient into "black" tiles.

## Support

Please [open an issue](https://github.com/DuhonDoesCode/AsciiTtv/issues) for support.

## Contributing

Please contribute! This is a small project, if you wish to contribute, please contact me for it. Discord is `duhon`.
