import random
import hashlib
import owner


class math():

    running = True

    def point_plotter(max_x, max_y, min_x, min_y):
        x = min_x
        y = min_y

        point_plot = True
        while point_plot:
            cords = (y, x)
            if x != max_x:
                x += 1
                print(f"yx: {cords}")
            elif y != max_y:
                y += 1
                x = min_x
                print(f"yx: {cords}")
            else:
                print(f"yx: {cords}")
                point_plot = False

    def hash():
        text = input("Enter a string to hash: ")
        hashed_text = hashlib.sha256(text.encode()).hexdigest()
        print(f"SHA-256 hash: {hashed_text}")

    def letter_to_binary():
        text = input("Enter a string to convert to binary: ")
        binary_string = ' '.join(format(ord(char), '08b') for char in text)
        print(f"Binary representation: {binary_string}")

    def binary_to_letter():
        binary_string = input("Enter a binary string to convert to text: ")
        binary_values = binary_string.split()
        ascii_string = ''.join(chr(int(b, 2)) for b in binary_values)
        print(f"Text representation: {ascii_string}")

    def dec_to_bin(num):
        if num > 1:
            math.dec_to_bin(num // 2)
        print(num % 2, end='')

    def dec_to_hex(num):
        hex_string = hex(num)[2:]
        print(hex_string)

    def hex_to_bin(hex_string):
        scale = 16  # hexadecimal
        num_of_bits = len(hex_string) * 4
        print(bin(int(hex_string, scale))[2:].zfill(num_of_bits))

    def hex_to_dec(hex_string):
        print(int(hex_string, 16))

    def bin_to_dec(bin_string):
        print(int(bin_string, 2))

    def bin_to_hex(bin_string):
        num_of_bits = len(bin_string)
        hex_string = hex(int(bin_string, 2))[2:].zfill(num_of_bits // 4)
        print(hex_string)

    def test():
        print("Testing point_plotter:")
        try:
            math.point_plotter(5, 5, -5, -5)
        except Exception as e:
            print(f"Error occurred: {e} point_plotter")
        print("Testing dec_to_bin:")
        try:
            math.dec_to_bin(10)
        except Exception as e:
            print(f"Error occurred: {e} dec_to_bin")
        print("\nTesting dec_to_hex:")
        try:
            math.dec_to_hex(10)
        except Exception as e:
            print(f"Error occurred: {e} dec_to_hex")
        print("Testing hex_to_bin:")
        try:
            math.hex_to_bin("a")
        except Exception as e:
            print(f"Error occurred: {e} hex_to_bin")
        print("Testing hex_to_dec:")
        try:
            math.hex_to_dec("a")
        except Exception as e:
            print(f"Error occurred: {e} hex_to_dec")
        print("Testing bin_to_dec:")
        try:
            math.bin_to_dec("1010")
        except Exception as e:
            print(f"Error occurred: {e} bin_to_dec")
        print("Testing bin_to_hex:")
        try:
            math.bin_to_hex("1010")
        except Exception as e:
            print(f"Error occurred: {e} bin_to_hex")

    # test()

    def converter():
        print("Choose a function to use:")
        print("1. dec_to_bin")
        print("2. dec_to_hex")
        print("3. hex_to_bin")
        print("4. hex_to_dec")
        print("5. bin_to_dec")
        print("6. bin_to_hex")
        print("7. letter_to_binary")
        print("8. binary_to_letter")
        choice = input("Enter the number of the function you want to use: ")

        if choice == "1":
            try:
                math.dec_to_bin(int(input("Enter a decimal number: ")))
            except Exception as e:
                print(f"Error occurred: {e} dec_to_bin")
        elif choice == "2":
            try:
                math.dec_to_hex(int(input("Enter a decimal number: ")))
            except Exception as e:
                print(f"Error occurred: {e} dec_to_hex")
        elif choice == "3":
            try:
                math.hex_to_bin(input("Enter a hexadecimal string: "))
            except Exception as e:
                print(f"Error occurred: {e} hex_to_bin")
        elif choice == "4":
            try:
                math.hex_to_dec(input("Enter a hexadecimal string: "))
            except Exception as e:
                print(f"Error occurred: {e} hex_to_dec")
        elif choice == "5":
            try:
                math.bin_to_dec(input("Enter a binary string: "))
            except Exception as e:
                print(f"Error occurred: {e} bin_to_dec")
        elif choice == "6":
            try:
                math.bin_to_hex(input("Enter a binary string: "))
            except Exception as e:
                print(f"Error occurred: {e} bin_to_hex")
        elif choice == "7":
            try:
                math.letter_to_binary()
            except Exception as e:
                print(f"Error occurred: {e} letter_to_binary")
        elif choice == "8":
            try:
                math.binary_to_letter()
            except Exception as e:
                print(f"Error occurred: {e} binary_to_letter")
        else:
            print("Invalid choice")

    # decimal calculator functions

    def dec_add():
        try:
            num1 = int(input("Enter the first decimal number: "))
            num2 = int(input("Enter the second decimal number: "))
            print(f"The sum is: {num1 + num2}")
        except Exception as e:
            print(f"Error occurred: {e} dec_adder")

    def dec_subtract():
        try:
            num1 = int(input("Enter the first decimal number: "))
            num2 = int(input("Enter the second decimal number: "))
            print(f"The difference is: {num1 - num2}")
        except Exception as e:
            print(f"Error occurred: {e} dec_subtractor")

    def dec_multiply():
        try:
            num1 = int(input("Enter the first decimal number: "))
            num2 = int(input("Enter the second decimal number: "))
            print(f"The product is: {num1 * num2}")
        except Exception as e:
            print(f"Error occurred: {e} dec_multiplier")

    def dec_divide():
        try:
            num1 = int(input("Enter the first decimal number: "))
            num2 = int(input("Enter the second decimal number: "))
            if num2 != 0:
                print(f"The quotient is: {num1 / num2}")
            else:
                print("Cannot divide by zero")
        except Exception as e:
            print(f"Error occurred: {e} dec_divider")

    # hex calculator functions

    def hex_add():
        try:
            num1 = int(input("Enter the first hexadecimal number: "), 16)
            num2 = int(input("Enter the second hexadecimal number: "), 16)
            print(f"The sum is: {hex(num1 + num2)[2:]}")
        except Exception as e:
            print(f"Error occurred: {e} hex_adder")

    def hex_subtract():
        try:
            num1 = int(input("Enter the first hexadecimal number: "), 16)
            num2 = int(input("Enter the second hexadecimal number: "), 16)
            print(f"The difference is: {hex(num1 - num2)[2:]}")
        except Exception as e:
            print(f"Error occurred: {e} hex_subtractor")

    def hex_multiply():
        try:
            num1 = int(input("Enter the first hexadecimal number: "), 16)
            num2 = int(input("Enter the second hexadecimal number: "), 16)
            print(f"The product is: {hex(num1 * num2)[2:]}")
        except Exception as e:
            print(f"Error occurred: {e} hex_multiplier")

    def hex_divide():
        try:
            num1 = int(input("Enter the first hexadecimal number: "), 16)
            num2 = int(input("Enter the second hexadecimal number: "), 16)
            if num2 != 0:
                print(f"The quotient is: {hex(num1 // num2)[2:]}")
            else:
                print("Cannot divide by zero")
        except Exception as e:
            print(f"Error occurred: {e} hex_divider")

    # binary calculator functions

    def bin_add():
        try:
            num1 = int(input("Enter the first binary number: "), 2)
            num2 = int(input("Enter the second binary number: "), 2)
            print(f"The sum is: {bin(num1 + num2)[2:]}")
        except Exception as e:
            print(f"Error occurred: {e} bin_adder")

    def bin_subtract():
        try:
            num1 = int(input("Enter the first binary number: "), 2)
            num2 = int(input("Enter the second binary number: "), 2)
            print(f"The difference is: {bin(num1 - num2)[2:]}")
        except Exception as e:
            print(f"Error occurred: {e} bin_subtractor")

    def bin_multiply():
        try:
            num1 = int(input("Enter the first binary number: "), 2)
            num2 = int(input("Enter the second binary number: "), 2)
            print(f"The product is: {bin(num1 * num2)[2:]}")
        except Exception as e:
            print(f"Error occurred: {e} bin_multiplier")

    def bin_divide():
        try:
            num1 = int(input("Enter the first binary number: "), 2)
            num2 = int(input("Enter the second binary number: "), 2)
            if num2 != 0:
                print(f"The quotient is: {bin(num1 // num2)[2:]}")
            else:
                print("Cannot divide by zero")
        except Exception as e:
            print(f"Error occurred: {e} bin_divider")

    def calc():
        print("Choose a calculator:")
        print("1. Decimal Calculator")
        print("2. Hexadecimal Calculator")
        print("3. Binary Calculator")
        print("4. Converter")
        print("5. Exit")
        choice = input("Enter the number of the calculator you want to use: ")

        if choice == "1":
            print("Choose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            operation = input(
                "Enter the number of the operation you want to perform: ")
            if operation == "1":
                math.dec_add()
            elif operation == "2":
                math.dec_subtract()
            elif operation == "3":
                math.dec_multiply()
            elif operation == "4":
                math.dec_divide()
            else:
                print("Invalid operation")
        elif choice == "2":
            print("Choose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            operation = input(
                "Enter the number of the operation you want to perform: ")
            if operation == "1":
                math.hex_add()
            elif operation == "2":
                math.hex_subtract()
            elif operation == "3":
                math.hex_multiply()
            elif operation == "4":
                math.hex_divide()
            else:
                print("Invalid operation")
        elif choice == "3":
            print("Choose an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            operation = input(
                "Enter the number of the operation you want to perform: ")
            if operation == "1":
                math.bin_add()
            elif operation == "2":
                math.bin_subtract()
            elif operation == "3":
                math.bin_multiply()
            elif operation == "4":
                math.bin_divide()
            else:
                print("Invalid operation")
        elif choice == "4":
            math.converter()
        elif choice == "5":
            math.running = False
        elif choice == owner.get_name():
            password = owner.get_password()
            if input("Password: ") == password:
                print("1. change password")
                print("2. change name")
                print("2. exit")
                owner_choice = input("Enter your choice: ")
                if owner_choice == "1":
                    owner.change_password()
                    print("Password changed successfully")
                elif owner_choice == "2":
                    owner.change_name()
                    print("Name changed successfully")
                elif owner_choice == "3":
                    if input("Password: ") == "abcd1234":
                        print(f"Your name is {owner.get_name()}")
                        print(f"Your password is {owner.get_password()}")
                elif owner_choice == "4":
                    print("Exiting owner menu")
                else:
                    print("Invalid choice")
        else:
            print("Invalid choice")


class games():
    def guess_the_number(size_l, size_h):

        number = random.randint(size_l, size_h)
        attempts = 0
        guessed = False

        print("Welcome to Guess the Number!")
        print(
            f"I have selected a number between {size_l} and {size_h}. Can you guess it?")

        while not guessed:
            try:
                guess = str(input("Enter your guess: "))
                if guess == "uuddlrlrabstart":
                    print(f"Konami code activated! The number is {number}.")
                else:
                    guessnum = int(guess)
                    attempts += 1
                    if guessnum < number:
                        print("Too low! Try again.")
                    elif guessnum > number:
                        print("Too high! Try again.")
                    else:
                        guessed = True
                        print(
                            f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def rock_paper_scissors():
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        print("Welcome to Rock, Paper, Scissors!")
        print("Enter your choice (rock, paper, or scissors):")
        user_choice = input().lower()

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            return

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

    def hangman(difficulty):
        words = ["python", "hangman", "programming", "challenge", "developer"]
        word = random.choice(words)
        guessed_letters = set()
        if difficulty == "easy":
            attempts = 20
        elif difficulty == "normal":
            attempts = 6
        elif difficulty == "hard":
            attempts = 5
        elif difficulty == "cheatcode":
            attempts = hex(0xFFFFFFFF)
        else:
            print("Invalid difficulty. Defaulting to normal.")
            attempts = 6

        print("Welcome to Hangman!")
        print("Guess the word, one letter at a time.")

        while attempts > 0:
            display_word = ''.join(
                [letter if letter in guessed_letters else '_' for letter in word])
            print(f"Word: {display_word}")
            print(f"Attempts remaining: {attempts}")

            guess = input("Enter a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("Correct!")
                if all(letter in guessed_letters for letter in word):
                    print(
                        f"Congratulations! You've guessed the word '{word}'!")
                    return
            else:
                print("Incorrect!")
                attempts -= 1

        print(f"Game over! The word was '{word}'.")

    def tik_tac_toe():
        board = [' ' for _ in range(9)]
        current_player = "X"
        bot = input(
            "Do you want to play against a bot? (yes/no): ").lower() == "yes"

        def print_board():
            print(f"{board[0]} | {board[1]} | {board[2]}")
            print("--+---+--")
            print(f"{board[3]} | {board[4]} | {board[5]}")
            print("--+---+--")
            print(f"{board[6]} | {board[7]} | {board[8]}")

        def check_winner(player):
            win_conditions = [
                [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
                [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
                [0, 4, 8], [2, 4, 6]              # diagonals
            ]
            return any(all(board[i] == player for i in condition) for condition in win_conditions)

        def get_available_moves():
            return [i for i in range(9) if board[i] == ' ']

        def bot_move():
            import random
            available = get_available_moves()

            # Try to win
            for move in available:
                board[move] = "O"
                if check_winner("O"):
                    return move
                board[move] = ' '

            # Block player from winning
            for move in available:
                board[move] = "X"
                if check_winner("X"):
                    board[move] = ' '
                    return move
                board[move] = ' '

            # Prefer center, then corners, then random
            if 4 in available:
                return 4
            corners = [0, 2, 6, 8]
            corner_moves = [m for m in corners if m in available]
            if corner_moves:
                return random.choice(corner_moves)
            return random.choice(available)

        while True:
            print_board()

            if bot and current_player == "O":
                move = bot_move()
                print(f"Bot plays at position {move + 1}")
            else:
                move = input(
                    f"Player {current_player}, enter your move (1-9): ")
                if not move.isdigit() or int(move) < 1 or int(move) > 9:
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue
                move = int(move) - 1
                if board[move] != ' ':
                    print("That spot is already taken. Try again.")
                    continue

            board[move] = current_player

            if check_winner(current_player):
                print_board()
                if current_player == "O" and bot:
                    print("Bot wins!")
                else:
                    print(f"Congratulations! Player {current_player} wins!")
                break

            if all(space != ' ' for space in board):
                print_board()
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

    def diceroll():
        print("Welcome to Dice Roll!")
        sides = input("Enter the number of sides on the die (default is 6): ")
        rolls = input(
            "Enter the number of times to roll the die (default is 1): ")
        try:
            sides = int(sides) if sides else 6
            rolls = int(rolls) if rolls else 1
            if sides < 1:
                print("Number of sides must be at least 1. Defaulting to 6.")
                sides = 6
        except ValueError:
            print("Invalid input. Defaulting to 6 sides.")
            sides = 6
        try:
            rolls = int(rolls) if rolls else 1
            if rolls < 1:
                print("Number of rolls must be at least 1. Defaulting to 1.")
                rolls = 1
        except ValueError:
            print("Invalid input. Defaulting to 1 roll.")
            rolls = 1

        results = []
        for i in range(rolls):
            result = random.randint(1, sides)
            results.append(result)
            print(f"Roll {i+1}: {result}")

        if rolls > 1:
            total = sum(results)
            print(f"Total: {total}")


math.calc()
