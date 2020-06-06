#MadLibs.
print("1->To play our madlib game with our StoryLine.")
print("2->Create your own storyline and words replacement.")
choice = input("Enter your choice: ")

if(choice == "1"):
    print("Roses are red.\nViolets are blue.\nI love you.")

    #We replace the red,Violets and you by the input that we provide.

    color = input("Enter a color: ")
    plural_noun = input("Enter a plural noun: ")
    celebrity = input("Enter a celebrity name: ")
    print("\n")
    print("Below is the new story line.")
    print("Roses are",color,".")
    print(plural_noun,"are blue.")
    print("I love",celebrity,".")

elif(choice == "2"):
    StoryLine = input("Enter you story line.")
    j = input("Enter the number of words you like to alter.")
    k = int(j)
    for i in range(0,k):
        a = input("Enter the word you would like to alter.")
        b = input("Enter the alternate word.")
        StoryLine = StoryLine.replace(a,b)

    print(StoryLine)
