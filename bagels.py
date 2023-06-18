import random


def main():
    num_len = 3
    max_guesses = 10

    while True:
        end = 0
        print("Bagels, a deductive logic game.\n"
              "By Al Sweigart\n"
              "\n"
              "I am thinking of a {}-digit number. Try to guess what it is.\n"
              "Here are some clues:\n"
              "When I say:\t\tThat Means:\n"
              "  Pico\t\t\tOne digit is correct but in the wrong position.\n"
              "  Fermi\t\t\tOne digit is correct and in the right position.\n"
              "  Bagels\t\tNo digit is correct.\n".format(num_len))

        number = get_number(num_len)
        print("I thought of a number.\n"
              "You have {} guesses.".format(max_guesses))

        guess = 1
        while guess <= max_guesses:
            print("Guess {}".format(guess))
            print(number)

            user_guess = input("> ")
            if user_guess == number:
                print("You guess the number right! The number was {}!".format(number))
                break

            get_clues(user_guess, number)
            guess += 1
        if guess > max_guesses:
            print("Sorry you ran out of guesses!")

        print("Would you like to play again(y/n)?")
        while end == 0:
            yorn = input('> ')
            if yorn == 'y' or yorn == 'Y':
                end = 1
                continue
            elif yorn == 'n' or yorn == 'N':
                print("Thanks for playing!\n"
                      "Goodbye.")
                return 0
            else:
                print("invalid input")


def get_clues(guess, num):
    clues = ''
    number = num
    for i in guess:
        for j in number:
            if i == j:
                if guess.index(i) == number.index(j):
                    clues += 'fermi '
                elif guess.index(i) != number.index(j):
                    clues += 'pico '
                number = number.replace(j, ' ', 1)
    if len(clues) < 1:
        return 'Bagels'

    words = clues.split(' ')
    clues = ''
    words.sort()
    for i in words:
        clues += i
        clues += ' '
    print(clues)


def get_number(digits):
    numbers = list('0123456789')
    random.shuffle(numbers)
    num = ''
    for i in range(digits):
        num += str(numbers[i])
    return num


if __name__ == '__main__':
    main()