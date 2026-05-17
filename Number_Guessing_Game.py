import random
import time

# ==========================================
# Advanced Number Guessing Game
# ==========================================

# Best score (lowest attempts)
best_attempts = None

# Statistics
total_games = 0
wins = 0
losses = 0


# ==========================================
# Select Difficulty
# ==========================================
def select_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy   (1-10, 5 Attempts)")
    print("2. Medium (1-50, 7 Attempts)")
    print("3. Hard   (1-100, 10 Attempts)")

    while True:
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            return "Easy", 1, 10, 5
        elif choice == "2":
            return "Medium", 1, 50, 7
        elif choice == "3":
            return "Hard", 1, 100, 10
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


# ==========================================
# Get Valid Integer Input
# ==========================================
def get_valid_guess(min_num, max_num):
    while True:
        user_input = input("Enter Your Guess: ")

        # Input validation
        if not user_input.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(user_input)

        # Range check
        if guess < min_num or guess > max_num:
            print(f"Please enter a number between {min_num} and {max_num}.")
            continue

        return guess


# ==========================================
# Calculate Score
# ==========================================
def calculate_score(attempts):
    score = 100 - (attempts - 1) * 10
    if score < 10:
        score = 10
    return score


# ==========================================
# Show Statistics
# ==========================================
def show_statistics():
    print("\n" + " STATISTICS ".center(50, "="))
    print(f"Total Games Played : {total_games}")
    print(f"Wins               : {wins}")
    print(f"Losses             : {losses}")

    if total_games > 0:
        win_rate = (wins / total_games) * 100
        print(f"Win Rate           : {win_rate:.2f}%")

    if best_attempts is not None:
        print(f"Best Score Record  : {best_attempts} attempt(s)")

    print("=" * 50)


# ==========================================
# Play One Game
# ==========================================
def play_game():
    global best_attempts, total_games, wins, losses

    total_games += 1

    # Difficulty settings
    level_name, min_num, max_num, max_attempts = select_difficulty()

    print("\n" + f" {level_name.upper()} MODE ".center(50, "-"))
    print(f"I am thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts.\n")

    # Generate secret number
    secret_number = random.randint(min_num, max_num)

    attempts = 0
    start_time = time.time()

    while attempts < max_attempts:
        print(f"Attempt {attempts + 1} of {max_attempts}")

        guess = get_valid_guess(min_num, max_num)
        attempts += 1

        # Correct guess
        if guess == secret_number:
            elapsed_time = time.time() - start_time
            score = calculate_score(attempts)

            print(f"\nCongratulations! You guessed the number in {attempts} attempt(s).")
            print(f"Score: {score}")
            print(f"Time Taken: {elapsed_time:.2f} seconds")

            # Update statistics
            wins += 1

            # Update best score
            if best_attempts is None or attempts < best_attempts:
                best_attempts = attempts
                print("New Best Score Record!")

            return

        # Wrong guess: show only ONE hint
        difference = abs(secret_number - guess)

        if difference == 1:
            print("Extremely Close!")
        elif difference <= 3:
            print("Very Close!")
        elif difference <= 10:
            print("Getting Closer!")
        else:
            print("Far Away!")

        # Direction hint
        if guess > secret_number:
            print("Try a smaller number.")
        else:
            print("Try a larger number.")

        # Last attempt warning
        if attempts == max_attempts - 1:
            print("Last Attempt Remaining!")

        print()

    # Game Over
    losses += 1
    elapsed_time = time.time() - start_time

    print("\nGame Over!")
    print(f"The correct number was {secret_number}.")
    print(f"Time Taken: {elapsed_time:.2f} seconds")


# ==========================================
# Main Program
# ==========================================
def main():
    welcome = "Welcome to Advanced Number Guessing Game"
    print(welcome.center(70, "="))

    while True:
        play_game()
        show_statistics()

        # Play Again Option
        while True:
            choice = input("\nPlay Again? (Y/N): ").strip().upper()

            if choice == "Y":
                break
            elif choice == "N":
                print("\nThank You for Playing!")
                print(" Keep Coding and Keep Learning Python!\n")
                return
            else:
                print("Please enter Y or N.")


# Run Program
if __name__ == "__main__":
    main()

