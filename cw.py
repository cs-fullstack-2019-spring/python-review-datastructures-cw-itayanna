def main():
    # problem1()
    # problem2()





# this fuction loops untill user enters quit then prints what they entered in a list


def problem1():
    userInput= ''
    names= []
    while userInput!='q':
        userInput= input("enter a name, enter q to quit")
        names.append(userInput)
    names.pop(len(names)-1)
    print(names)

# this function sotrs the list given based on the users choice

def problem2():
    myDictionaryList = [
        {
            "name": "Kelvin",
            "age": 30
        },
        {
            "name": "Bob",
            "age": 50
        },
        {
            "name": "Alex",
            "age": 21
        }
    ]



    def sorting(x):
        if userInput=="age":

            return x["age"]
        elif userInput=="name":

            return x["name"]




    userInput= ''
    while userInput!="q":
        for eachEl in myDictionaryList:
            print("Name:",eachEl["name"],'\n',"Age:",eachEl["age"])

        userInput= input("How would you like this list sorted?")
        myDictionaryList.sort(key=sorting)
























if __name__ == '__main__':
    main()