# Meows

A small Python command-line program that uses `cowsay` to make a cat say a word or sentence.

## Requirements

- Python 3
- `cowsay`

Install the required package with:

```bash
pip install -r requirements.txt
```

## Usage

Run the program with:

```bash
python meows.py
```

By default, the cat says `meow` once.

Use `-n` or `--number` to choose how many times the word is repeated:

```bash
python meows.py -n 3
```

Use `-w` or `--word` to choose a different word or sentence:

```bash
python meows.py -w "hello"
```

You can combine both options:

```bash
python meows.py -n 3 -w "hello"
```

## Help

To see all command-line options:

```bash
python meows.py --help
```
