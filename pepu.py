import random
import time

def main():

    attendees = [
        "Person1",
        "Person2",
        "Person3"
    ]

    phrases = [
        "Seuraavaksi putoaa...",
        "Nyt tipahtaa...",
        "Sitten tippuu...",
        "Tänä perjantaina pulloa ei saa...",
        "Seuraavan henkilön ryysvuori ei kasva...",
        "Seuraavan henkilön pää menee tyynyyn...",
        "Mount Everyystiä ei valloita...",
        "Veitsensä pakkaa..."
    ]

    def popNext():
        time.sleep(2)
        print(random.choice(phrases) + "\n")
        time.sleep(3)
        print(attendees.pop() + "\n")
    
    random.shuffle(attendees)

    print("\n" + "Aloitetaan arvonta. Osallistujia on " + str(len(attendees)) + ".")
    time.sleep(3)
    print("\n" + "Ensimmäisenä putoaa..." + "\n")
    time.sleep(3)
    print(attendees.pop() + "\n")

    while len(attendees) > 1:

        if len(attendees) == 5:
            time.sleep(2)
            print("\n"+ "Enää viisi kilpailijaa jäljellä!" + "\n")
            time.sleep(2)
            print("Top 5 on: " + "\n")

            for person in attendees:
                print(person)

            random.shuffle(attendees)
            time.sleep(6)
            print("\n" + "Jatketaan arvontaa!" + "\n")
            popNext()

        elif len(attendees) == 2:
            time.sleep(2)
            print("\n" + "Jäljellä on enää kaksi finalistia!" + "\n")
            time.sleep(1)
            print("He ovat " + attendees[0] + " ja " + attendees[1] + "!")

            random.shuffle(attendees)
            time.sleep(4)
            print("\n" + "Jännitys tiivistyy..." + "\n")
            time.sleep(2)
            print("Rumpujen pärinää..." + "\n")
            time.sleep(2)
            print("Ryys vuori kasvaa..." + "\n")
            time.sleep(3)
            print("Tämän perjantaipullon voittaa....." + "\n")
            
            winner = attendees.pop()
            time.sleep(3)
            print(winner.upper() + "!!!" + "\n")
            
            time.sleep(1)
            print("Onnea voittajalle!" + "\n")

        else:
            popNext()


if __name__ == "__main__":
    main()