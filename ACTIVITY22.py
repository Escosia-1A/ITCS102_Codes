
paper_type = ["letter", "long", "A4"]
anime_title = []

while True:
    ans = input("Do you know paper sizes? yes/no")

    if ans.lower() == 'yes':
        print("What size? select from the list")
        for x in paper_type:
            print(x)
        anime_type = input("size --> ")

        title = input("What is the size of the paper? ")
        anime.