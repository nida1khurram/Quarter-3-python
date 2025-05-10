
def generate_lyrics(word:str):
    print("\n")
    with open("./lyrics.txt", "r", encoding="utf-8") as file:
        lines = file.readlines() 
        find = list(filter(lambda x : x[0].lower() == word.lower() , lines))

        if find:
            count = 1
            for i in find:
                print(f"{count} : {i}")
                count += 1
        else:
            print("Not Found Your Lyrics")


def main():
    user_input = input("\nEnter alphabet : ")
    if user_input == "":
        print("\nPlease enter alphabet")
    else:
        generate_lyrics(user_input)


if __name__ in "__main__":
    main()