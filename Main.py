import json
def main():
    print("Welcome to ImageRunner")
    Loop_var = True
    First_prompt = True
    while Loop_var:
        while First_prompt:
            #loop runs at least once and requests 2 inputs from the user
            result = input("Please enter the file path and the programming language separated by a comma\n").split(",")
            print(len(result))
            if(len(result) != 2):
                print("Missing one of the inputs")
            else:
                First_prompt = False
        #after confirming the user gave 2 inputs they are stored
        path = result[0]
        lang = result[1]
        print(path, lang)
        #OCR_main()



        #prompts the user to run the program again or exits
        print('Would you like to input another file? (Yes, yes, Y, y, or No, no, N, n)')
        x = input()
        if(x == 'No' or 'N' or 'n' or 'no'):
            Loop_var = False
        if(x == 'Yes' or 'Y' or 'y' or 'yes'):
            First_prompt = True


if __name__ == "__main__":
    main()