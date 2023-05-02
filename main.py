import csvlinked as linked
import csvfree as free

def main():
    option = 10
    while option != 0:
        print("Menu for files creation(1 to 3 only)")
        print("1.- Conected files")
        print("2.- Disconected files")
        print("3.- Bye")
        print("\n")
        option = input("Choose . . . . ")
        if option == '1':
            qty = input("How many records? ")
            linked.conected_files(int(qty))
            print("Look for the files in the source folder")
        elif option == '2':
            qty = input("How many records? ")
            free.file_manager(int(qty))
            print("Look for the files in the source folder")
        elif option == '3':
            break
        else:
            continue
    
if __name__ == "__main__":
    main()