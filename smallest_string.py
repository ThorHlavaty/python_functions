#Here's our list the user will give us.
strings = []
#This is the escape from the loop when the user is done
esc = "y"
#This functions takes a bunch of strings, checks the shortest, and tells you what it is and how long the shortest is.
def smallest_strings(strings):
    valid = 'y'
    while valid == 'y':
        while True:
            strings.append(input('Give me some things to compare. When your done, submit "q". '))
            if strings[-1] == 'q':
                strings.pop(-1)
                break
        for string in strings:
            shortstring = ""
            length = len(strings[0])
            if len(string) < length:
                length = len(string)
                shortstring = string
        print(f"Your shortest string is:\n{shortstring}\nIt's length is {length}")
        shortstring = ""
        length = 0
        valid = input("Want to do another? [y/n]: ")
#This function is the same-ish as above, but for the longest string. It's a little weirder.
def largest_strings(strings):
    valid = 'y'
    while valid == 'y':
        while True:
            strings.append(input('Give me some things to compare. When your done, submit "q". '))
            if strings[-1] == 'q':
                strings.pop(-1)
                break
        longstring = ""
        for string in strings:
            if len(string) > len(longstring):
                length = len(string)
                longstring = string
                
        
        print(f"Your longest string is:\n{longstring}\nIt's length is {length}")
        longstring = ""
        length = 0
        valid = input("Want to do another? [y/n]: ") 
#Starts the program.
print("Hello there!")
#Runs the user through what they want to do/
while esc == "y":
    choice = input('Do you want to know your "shortest" string or your "longest" string?: ').lower()
    if choice == "shortest":
        smallest_strings(strings)
        esc = "y"
        while esc == "y":
            to_start = input("Would you like to do something else? [y/n]: ")
            if to_start == 'y':
                break
            elif to_start == 'n':
                esc = "n"
            else:
                print("Sorry, I didn't catch that.")
    elif choice == "longest":
        largest_strings(strings)
        esc = "y"
        while esc == "y":
            to_start = input("Would you like to do something else? [y/n]: ")
            if to_start == 'y':
                break
            elif to_start == 'n':
                esc = "n"
            else:
                print("Sorry, I didn't catch that.")
    else:
        print("Sorry, I didn't catch that!")
#This says goodbye. Very easy to implement: slap it to the end of any code at the highest level of indentation.
print("Okay, goodbye!\n\n\n\n\n\n\n❤️❤️❤️ i love u ❤️❤️❤️")
