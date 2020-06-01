import time


try:
    print("  888   888          888          88888888      88888  888             000000000008            =====            I888         8888I    1018888888888   ")
    print("  888  888          88888         888888888      888   888             000000000088           /_/  \_\          |8|888      888|8|    0108888888888   ")
    print("  888 888          8888888        888    888     888   888             008       88          /_/    \_\         |8| 888    888 |8|    001     8 888   ")
    print("  888888          888   888       888    888     888   888             008  8888888         /_/ ==== \_\        |8|   888 888  |8|    100888888       ")
    print("  888888         888 888 888      888888888      888   888             008  8  88888       /_/ ====== \_\       |8|     8888   |8|    001888888       ")
    print("  888  888     888         888    888            888   888       010   008       888      /_/          \_\      |8|            |8|    888     8 888   ")
    print("  888   888   888           888   888            888   8880101010188   0088888888888     /_/            \_\     |8|            |8|    8088888888888   ")
    print("  888    888 888             888  888           88888  8880101010188   0088888888888    /_/              \_\    |8|            |8|    9808888888888   ")

    print()
    print()
    print()
    print()
    print()

    Score = 0

    # Creating functions

    def Question1():
        print("Hey Solve this Quize for next--\n")
        My_First_num = input("Enter Some numbers like 888890: ")

        Length = len(My_First_num)
    if Length >= 6:
        print("Good Job Buddy! You entered  ", +
              My_First_num + "  That is Correct Format")

    else:
        print("Ohh Sorry! You have entered worng numbers,Please entered correct numberes..........")
        Question1()
    My_Second_num = input("Enter Next numbers like 888890: ")
    Length = len(My_Second_num)

    if Length >= 6:
        print("Good Job Buddy! You entered  ", +
              My_Second_num + "  That is Correct Format")

    else:
        print("Ohh Sorry! You have entered worng numbers,Please entered correct numberes..........")
        Question1()

    result1 = My_First_num + My_Second_num

    print("Now time to solve those input.........\n")
    print("Add both numberes\n")

    result2 = input("Enter Your Result Here: ")

    if result2 == result1:
        Score += 1
        print("You Have Passed Beacause you Solved this quize ")

    else:
        Score -= 1
        print("Ohh Sorry! You Have Entered Wrong Addition")

        # Creating the second functions
    print()
    print()
    print()

    def Question2():
        print("Hey Solve this Quize for next--\n")
    My_First1_num = input("Enter Some numbers like 888890: ")

    Length = len(My_First1_num)
    if Length >= 6:
        print("Good Job Buddy! You entered  ", +
              My_First1_num + "  That is Correct Format")

    else:
        print("Ohh Sorry! You have entered worng numbers,Please entered correct numberes..........")
        Question2()
    My_Second1_num = input("Enter Next numbers like 888890: ")
    Length = len(My_Second1_num)

    if Length >= 6:
        print("Good Job Buddy! You entered  ", +
              My_Second1_num + "  That is Correct Format")

    else:
        print("Ohh Sorry! You have entered worng numbers,Please entered correct numberes..........")
        Question2()

    result3 = My_First1_num - My_Second1_num

    print("Now time to solve those input.........\n")
    print("Add both numberes\n")

    result4 = input("Enter Your Result Here: ")

    if result4 == result3:
        Score += 1
        print("You Have Passed Beacause you Solved this quize ")

    else:
        Score -= 1
        print("Ohh Sorry! You Have Entered Wrong Substraction")

    print("Your Score is ", +Score)

    Question1()
    Question2()


except Exception as err:
    print(err)
