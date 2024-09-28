import random

def generate_secret_number():
  """
  Generates a random number between 1 and 100 (inclusive).
  """
  return random.randint(1, 100)

def get_user_guess():
  """
  Prompts the user for a guess and validates it.
  """
  while True:
    try:
      guess = int(input("Enter your guess (1-100): "))
      if not 1 <= guess <= 100:
        raise ValueError("Invalid guess. Please enter a number between 1 and 100.")
      return guess
    except ValueError as e:
      print(f"Error: {e}")

def compare_guess(secret_number, guess):
  """
  Compares the user's guess with the secret number and provides feedback.
  """
  if guess == secret_number:
    print(f"Congratulations! You guessed the number!")
  elif guess < secret_number:
    print("Your guess is too low. Try again.")
  else:
    print("Your guess is too high. Try again.")

def play_game():
  """
  Runs the main game loop.
  """
  secret_number = generate_secret_number()
  guesses = 0

  while True:
    guess = get_user_guess()
    guesses += 1
    compare_guess(secret_number, guess)

    if guess == secret_number:
      print(f"You guessed the number in {guesses} guesses!")
      break

  play_again = input("Would you like to play again? (y/n): ")
  if play_again.lower() == "y":
    play_game()
  else:
    print("Thanks for playing!")

if __name__ == "__main__":
  play_game()
