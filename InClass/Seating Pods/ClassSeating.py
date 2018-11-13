# Author: Adrian T. Neumann
# Date: November 6, 5018
# Description: Class seating arrangement. 


def main():
 
 
    # Input and Variables
    
    # Vriables initialized
    Pods = []
    NumberOfPods = 7
    PodNames = []

    # Processing

    # Pods 1-7 hard coded

    # Pod one
    PodOne = []
    PodOne.append("Adrian")
    PodOne.append("Hunter")
    PodOne.append("Marcus")

    Pods.append(PodOne)

    # Pod two
    PodTwo = []
    PodTwo.append("Pat")
    PodTwo.append("Ken")
    PodTwo.append("Michael")

    Pods.append(PodTwo)

    # Pod three
    PodThree = []
    PodThree.append("Matt")
    PodThree.append("Jamie")
   
    Pods.append(PodThree)

    # Pod four
    PodFour = []
    PodFour.append("Christine")
    PodFour.append("Tom")
    PodFour.append("Abraham")

    Pods.append(PodFour)

    # Pod five
    PodFive = []
    PodFive.append("Cole")
    PodFive.append("Ben")
    PodFive.append("Jim")

    Pods.append(PodFive)

    # Pod six
    PodSix = []
    PodSix.append("Tim")
    PodSix.append("Houston")
    
    Pods.append(PodSix)

    # Pod seven
    PodSeven = []
    PodSeven.append("Stacey")
    PodSeven.append("Jones")
    PodSeven.append("Mark")

    Pods.append(PodSeven)


    # Output
    for steps in range(len(Pods)):
        print("")
        print("Pod #:",steps + 1)
        for student in Pods[steps]:
            print(student)

    
if __name__ == "__main__":
    main()
