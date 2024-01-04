# wordhuntsolver

## About
This is a small application that solves the game "Word Hunt"

## Installation
You must install first install [tesseract](https://github.com/tesseract-ocr/tesseract).

Then you can clone the repository or download as a zip file. After that you should run this command to install dependencies:
```
pip install .
```

## Usage

You must have a screenshot of the gameboard, preferably square. You must also have a word list; I recommend one of the Collin's scrabble dictionaries.

When in the directory the program is installed, you simply run:
```
python3 -m wordhuntsolver <path_to_image> <path_to_word_list>
```
*Note: The word list must be separated by newlines, for example:*
```
HELLO
WORD
LIST
```

If tesseract is not working, double check the `config.toml` has the correct path to your binary.
