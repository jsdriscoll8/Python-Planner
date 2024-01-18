import io
def main():
    # Intro
    print("Welcome to the planner!")

    # Validate the different parts of these dates
    dateValid = False
    month = None
    day = None
    year = None

    while dateValid == False:
        date = input("\nEnter a date in MM-DD-YY format, or type 'quit' to quit: ")
        if date == 'quit':
            break
        elif len(date) != 8:
            print("Invalid date!")
        else:
            dateValid = True
            try:
                month = int(date[0:2])
            except:
                print("Invalid month!")
                dateValid = False

            try:
                day = int(date[3:5])
            except:
                print("Invalid day!")
                dateValid = False

            try:
                year = int(date[6:])
            except:
                print("Invalid year!")
                dateValid = False

    print("Thanks for using the planner!")
    return 0

if __name__ == "__main__":
    main()