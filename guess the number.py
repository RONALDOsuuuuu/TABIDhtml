import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
         print("There iscurrently no high score it's your for taking!")
    else:
         print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
     random_number = it(random.randit(1,10))
     print("Hey There! Welcome to the game of gusses!")
     player_name = input("enter your name!")
     wanna_play = input("Hi, {}, would you like to play the gussing game? (enter yes/no".format(player_name))
     attempts = 0
     show_score()
     while wanna_play.lower() == "yes":
          try:
               guess = input("pick a number between 1 and 10")
               if int(guess) < 1 or int(guess) > 10:
                    raise ValueError("Please guess  number within the given range")
               if int(guess) == random_number:
                    print("Congrats! you gussed it right")
                    attempts += 1
                    attempts_list.append(attempts)
                    print("It took you {} attempts".format(attempts))
                    play_again = input("Would you like to play again? (Enter Yes/No)".format(player_name))
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1,10))
                    if play_again.lower() == "no":
                         print("that's cool I have nice day!")
                         break
                elif int(guess) < random_number:
                    print("its lower")
                    attempts += 1
                elif int(guess) < random_number:
                     print("its higher")
                     attempts += 1
            except ValueError as err:
               print("Oh l, that is not a valid value. try again....")
               print("({})".format(err))
        else:
            print("Thats cool i have a nice day")
if __name__== '__main__':
     start_game()