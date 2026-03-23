# Lab 4 - Word Game

## Run the Game

From the project folder, run:

```powershell
python main.py
```

## Autoplay Mode

When the game starts, it asks:

```text
Auto play? (y/n):
```

- Enter `n` to play manually and type your own guesses.
- Enter `y` to let the robot guess automatically.

In autoplay mode, the robot picks random letters that have not been guessed
yet, prints each guess, and keeps going until the word is solved or lives
reach zero.

## Run the Tests

Run the unit tests with:

```powershell
python -m unittest test.py
```

Optional (more details):

```powershell
python -m unittest -v test.py
```
