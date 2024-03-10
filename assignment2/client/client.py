import xmlrpc.client

class Client:
    def __init__(self):
        self.server = xmlrpc.client.ServerProxy('http://localhost:8000')
    
    def getNotes (self):
        topic = input("Enter topic: ")
        notes = self.server.getNotes(topic)
        if notes:
            for note in notes:
                print(note)
        else:
            print("No note found")

    def newNote (self):
        getTopic = input("Enter topic: ")
        name = input("Enter name: ")
        text = input("Enter text: ")
        print(self.server.appendNote(getTopic, name, text))


if __name__ == "__main__":
    client = Client()

    while True:
        print("1. Add new note")
        print("2. Get notes")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            client.newNote()
        elif choice == "2":
            client.getNotes()
        elif choice == "3":
            break
        else:
            print("Unknown command. Try 1-3.")