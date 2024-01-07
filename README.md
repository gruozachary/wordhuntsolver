# wordhuntsolver

## About
This is a small application that solves the game "Word Hunt" using optical character recognition (OCR).

## Installation
You must install first install [tesseract](https://github.com/tesseract-ocr/tesseract).

You can then install the application like so:
```
> git clone "https://github.com/gruozachary/wordhuntsolver.git"
> cd wordhuntsolver
> pip install .
```

## Usage

You must first have a screenshot of the gameboard, preferably square. You must also have a word list; I recommend one of the Collin's scrabble dictionaries.

When in the directory the program is installed, you simply run:
```
python3 -m wordhuntsolver
```

*Note: The word list must be separated by newlines, for example:*
```
HELLO
WORD
LIST
```

## Configuration

You can edit the `config.toml` in the base directory to fit your needs.

For example:

```toml
# ...

[tesseract]
command = "path_to_your_tesseract_binary"

[word_list]
default_path = "path_to_your_word_list"

# ...
```
