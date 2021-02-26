import random
import time

def main():

    attendees = [
        "Person1",
        "Person2",
        "Person3"
    ]

    random.shuffle(attendees)

    print("\n" + "Ensimmäisenä putoaa..." + "\n")
    time.sleep(3)
    print(attendees.pop() + "\n")

    while len(attendees) > 1:
        loser = attendees.pop()
        time.sleep(2)
        print("Seuraavana putoaa..." + "\n")
        time.sleep(3)
        print(loser + "\n")

    winner = attendees.pop()

    time.sleep(2)
    print("Ja voittaja on..." + "\n")

    time.sleep(3)
    print("Jännitys tiivistyy..." "\n")

    time.sleep(3)
    print(winner.upper() + "!!!" + "\n")
    
    time.sleep(1)
    print("Onnea voittajalle!" + "\n")


if __name__ == "__main__":
    main()