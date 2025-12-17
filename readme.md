# AsciiTtv

A simple twitch.tv to console ascii converter. Made in under a day, so don't mind the weirdness.

## Table of Contents

- [Installation](#installation)
- [Config file](#config)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Clone, create a virtual environment (python 3.11)

```sh
git clone https://github.com/DuhonDoesCode/AsciiTtv.git
python3.11 -m venv .venv
source .venv/bin/activate
```

Install all requirements, edit [config.json](#config), run with utf8 flag

```sh
pip install requirements.txt
python3.11 -Xutf8 stream.py
```

## Config

Config options are streamer, resolution and tileset. 

- Streamer: Specifies which stream to put in the terminal. Use the same as its shown in the url (all lowercase).
- Resolution: specifies how many pixels will be skipped (so higher = smaller output).
- Tileset: What symbols to use for ASCII display. For correct behavior, make it a single string with no spaces. To the left the "white" tiles, making a gradient into "black" tiles.

## Support

Please [open an issue](https://github.com/DuhonDoesCode/AsciiTtv/issues) for support.

## Contributing

Please contribute! This is a small project, if you wish to contribute, please contact me for it. Discord is `duhon`.
