# My Original Thinking
Decrypt the string into "_" so that the player can have a look at how many letters there are. The player will lose if the lives run out, or the player guess the word. They cannot guess more than one letter, but they are allow to guess the whole word. They can see their guess, and how many lives they have left at the end.
# What are the states of a game like Hangman?
Correct(guess one letter correctly)
Wrong(wrong answers)
Win(guess the word)
Lost(lives run out)
# What variables are required?
secret word, lives/turns, guessed answers, player's guess
# What are the rules and invariants?
Correct - lives remain unchanged
Wrong - lives minus 1
Invariant: secret_word
# What kind of bugs and edge cases should we be careful about?
Answers that are not letters, answer with more than one letter
Compound words(ice cream, living room)
Hyphenated compound words(Mother-in-law, runner-up)
Uppercase and lowercase

# Copilot Suggestions
# App states 
For a Hangman-style game, think in terms of a small state machine. The core states are:

INIT
Set up the game: choose secret word, reset lives, clear guesses.

WAITING_FOR_GUESS
Prompt player for input.

VALIDATING_GUESS
Check if input is valid (letter/word, alphabetic, not duplicate).

APPLY_GUESS
Update game data:

reveal letters if correct
reduce lives if wrong
track guessed letters
CHECK_END_CONDITION
Decide next state:
if word fully revealed -> WIN
if lives == 0 -> LOSE
else -> back to WAITING_FOR_GUESS
WIN
Show victory message and final board.

LOSE
Show defeat message and reveal word.

PLAY_AGAIN
Ask replay question:

yes -> INIT
no -> EXIT
EXIT
End program cleanly.

# App Variables
Great question. For Hangman, keep a small set of core variables and derive the rest.

secret_word: str
The word/phrase to guess (store in one case, usually lowercase).

lives: int
How many wrong guesses remain.

guessed_letters: set[str]
Letters already guessed ({"a", "e", ...}) to block duplicates fast.

guessed_words: set[str] (optional but useful)
Whole-word guesses already tried, so repeated full guesses can be rejected.

display_chars: list[str]
Current visible board, e.g. ["_", "_", "e", "_"] (or with spaces/hyphens preserved).

game_state: str
State machine value like INIT, WAITING_FOR_GUESS, WIN, LOSE, etc.

current_guess: str
Latest input from player (letter or full-word attempt).

max_lives: int (optional)
Useful for reset/replay and UI display (lives/max_lives).

play_again: bool
Controls replay loop.

If you want to keep it minimal, you can start with just:
secret_word, lives, guessed_letters, display_chars, current_guess.
Everything else can be derived or added when needed.

# App Rules and Invariants
For your Hangman game, a good way to separate them is:

Rules = what the player is allowed to do and what happens.
Invariants = things that must always stay true during the game.
Rules

Player can guess either one letter or the full word.
Guesses must be alphabetic (a-z) only.
Repeated guesses are not counted as new turns.
Correct letter guess reveals all matching positions.
Wrong guess decreases lives by 1.
Correct guess does not change lives.
If full-word guess is correct, game ends immediately with win.
If lives reaches 0, game ends with loss.
If all letters are revealed, game ends with win.
Spaces and hyphens are shown from the start and never need guessing.
Invariants

secret_word does not change after game start.
len(encrypted) == len(secret_word) always.
encrypted[i] is either:
the real character from secret_word[i] (if revealed), or
_ for hidden letters, or
space/hyphen if that character is non-letter.
lives >= 0 always.
guessed_letters only contains lowercase alphabetic guesses.
Once a letter is revealed in encrypted, it never goes back to _.
A guess is processed at most once (duplicates don’t change state).
Win and loss are mutually exclusive states (cannot both be true).

# App Bugs
Here are the most common bugs in Word Guess / Hangman implementations, plus a few that are already visible in your current code.

High-Impact Bugs (General)

Infinite game loops when win/lose is detected but the loop never breaks.
Re-initializing game state every turn (board/guesses reset unexpectedly).
Duplicate guesses still consuming turns/lives.
Input validation holes:
empty input
non-letters
multiple letters when only one is allowed
mixed-case mismatch (A vs a)
Wrong win condition logic (checking old board state before applying guess).
Lives going negative (-1, -2) instead of stopping at zero.
Phrase handling bugs:
spaces/hyphens hidden when they should be auto-revealed
.isalpha() rejecting phrase guesses with spaces/hyphens
Full-word guess logic bugs:
correct full-word guess not ending game
incorrect full-word guess not penalized (if your rule says it should)
Mutable type mismatch bugs (list vs set) causing unexpected behavior.
Replay prompt logic always failing due boolean condition mistakes.