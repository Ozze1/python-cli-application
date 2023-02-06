import sys
import json


def main():
    if len(sys.argv) == 1:
        print("Error: No command provided.")
        return

    guestbook = []
    filename = "../guestbook.txt"

    with open(filename, "a+") as file:
        file.seek(0)
        for line in file:
            guestbook.append(line.strip())

    command = sys.argv[1]
    if command == "new":
        note = " ".join(sys.argv[2:])
        guestbook.append(note)
        with open(filename, "a") as file:
            file.write(note + "\n")
        print("Note added.")
    elif command == "list":
        for entry in guestbook:
            print(entry)
    elif command == "edit":
        index = int(sys.argv[2])
        note = " ".join(sys.argv[3:])
        if index > len(guestbook):
            print(f"Error: Note {index} not found.")
            return
        guestbook[index - 1] = note
        with open(filename, "w") as file:
            for entry in guestbook:
                file.write(entry + "\n")
        print(f"Note {index} edited.")
    elif command == "delete":
        index = int(sys.argv[2])
        if index > len(guestbook):
            print(f"Error: Note {index} not found.")
            return
        note = guestbook.pop(index - 1)
        with open(filename, "w") as file:
            for entry in guestbook:
                file.write(entry + "\n")
        print(f"Note {index} deleted.")
    elif command == "export":
        print(json.dumps(guestbook))
    else:
        print("Error: Invalid command.")


if __name__ == "__main__":
    main()
