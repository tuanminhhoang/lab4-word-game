import random

word_list = ["apple","banana","orange","guitar","planet","window","forest","rocket","mother-in-law","ice cream"]

def choose_word():
	"""Return a random secret word from the predefined list."""
	return random.choice(word_list)

def encrypt(secret_word, guess_letters):
	"""Build the masked display of the secret word.

	Spaces and hyphens are always visible. Letters are revealed only if they
	appear in guess_letters.
	"""
	encrypted = []
	for char in secret_word:
		if char == " ":
			encrypted.append(" ")
		elif char in guess_letters:
			encrypted.append(char)
		elif char == "-":
			encrypted.append("-")
		else:
			encrypted.append("_")
	return encrypted
	
def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str], int, str]:
	"""Update game state for one guess and return status.

	Returns a tuple: (guessed_letters, lives, status), where status is one of
	"Duplicate", "Invalid", "Victory", "Correct", or "Wrong".
	"""
	if guess in guessed_letters:
		return guessed_letters, lives, "Duplicate"
	if not guess.isalpha():
		if guess == secret_word:
			guessed_letters.append(guess)
			return guessed_letters, lives, "Victory"
		return guessed_letters, lives, "Invalid"
	
	guessed_letters.append(guess)
	if guess == secret_word:
		return guessed_letters, lives, "Victory"
	if guess in secret_word:
		return guessed_letters, lives, "Correct"
	if guess not in secret_word:
		lives -= 1
		return guessed_letters, lives, "Wrong"
				

def play():
	"""Run the interactive game loop until the player quits."""
	playing = True
	while playing:
		secret_word = choose_word()
		guess_letters = []
		lives = 6
		mask = encrypt(secret_word, guess_letters)
		print("The word is:", "".join(mask))
		while lives > 0 and "_" in mask:
			
			guess = input("Your guess: ").lower()
			guess_letters, lives, ans = update_game_state(secret_word, guess_letters, guess, lives)
			mask = encrypt(secret_word, guess_letters)

			if ans == "Invalid":
				print("Invalid syntax!")
				continue
			if ans == "Duplicate":
				print("Already guessed!")
				continue
			elif ans == "Wrong":
				print(f"Incorrect, lives remaining: {lives}")
			elif ans == "Correct":
				print(f"Good guess! The word:","".join(mask))
			elif ans == "Victory":
				break

		if lives == 0:
			print(f"Defeated! The word is: {secret_word}")
		else:
			print("Good job! You won!")

		ask = input("Continue playing (y/n): ").lower()
		if ask == "n":
			print("Thanks for playing!")
			playing = False	

if __name__ == "__main__":
	play()