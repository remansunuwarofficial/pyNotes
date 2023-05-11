while True:
    t = input("Enter note title (q for quit): ")
    d = input("Enter note description (q for quit): ")
    if(t.lower() == "q"):
        break
    elif(d.lower() == "q"):
        break
    else:
        class Notes():
            def __init__(self, title, description):
                self.title = title
                self.description = description 

            def addNote(self):
                    data = {
                        "title": f"{self.title}",
                        "description": f"{self.description}"
                    }
                    
                    f = open(file="data.txt", mode="a")
                    f.write(f"{data}")
                    f.close()
            def viewData(self):
                data = {
                        "title": f"{self.title}",
                        "description": f"{self.description}"
                }
                    
                f = open(file="data.txt", mode="r")
                print(f.read())
                f.close()
        a = Notes(t, d)
        a.addNote()
        doyou = input("Do you want to view data:(y/n) ")
        if doyou.lower() == "y":
            a.viewData()
        else:
            print("Thanks")