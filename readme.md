# AsciiTtv

A simple twitch.tv to console ascii converter. Made in under a day, so don't mind the weirdness.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage-tips)
- [TODO](#todo)
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

Install all requirements, edit [config.json](#config), run

```sh
pip install -r requirements.txt
python3.11 stream.py
```

## Usage tips
At watchable resolutions, the program uses a lot of symbols at once, thus requiring you to zoom out. To do so, either use `ctrl+scroll wheel`, or `crtl+-`. Do so before rendering kicks in, however (when it says it will start). As for what terminal to use, the app is cross-platform, so as long as your terminal can handle text, it can run this! However, GPU-Enabled terminals such as wezterm, kitty or ghostty are recommended since, for example, the default Windows command prompt is... lacking.

## TODO
Actual interface, audio maybe?

## Config

Config options are streamer, resolution, tileset, colored and usechafa. 

- Streamer: Specifies which stream to put in the terminal. Use the same as its shown in the url (all lowercase).
- Resolution: specifies how many pixels will be skipped (so higher = smaller output).
- Tileset: What symbols to use for ASCII display. For correct behavior, make it a single string with no spaces. To the left the "white" tiles, making a gradient into "black" tiles.
- Colored: Defines if your terminal will be colored or monochrome. Note that making the output colored *severely* impacts rendering speeds. (1 = true, 0 = false. Off by default.)
- Use Chafa: Chafa is a *very* reasonable library that allows for incredibly crisp output. The downside is a severe lack of recognizable ASCII charm. Also the speed, as is with colored ANSI, is very slow. Even more so because, well, look at it. Off by default.

## Support

Please [open an issue](https://github.com/DuhonDoesCode/AsciiTtv/issues) for support.

## Contributing

Please contribute! This is a small project, if you wish to contribute, please contact me for it. Discord is `duhon`.
