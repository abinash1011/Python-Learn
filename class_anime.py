class Anime:
    def __init__(self, name, rank, no_of_episodes):
        self.name = name
        self.rank = rank
        self.no_of_episodes = no_of_episodes
    def intro(self):
        print(f'\033[1m{self.name} \033[0m-' )
        print(f" Rank {self.rank} in myanimelist.net. It has {self.no_of_episodes} episodes")
       

anime1 = Anime("Fullmetal Alchemist: Brotherhood", 1, 64)
anime2 = Anime("Shingeki No Kyojin", 2, 10)
anime3 = Anime("Steins Gate", 3, 24)
anime4 = Anime("Gintama", 4, 51)
anime5 = Anime("Fruits Basket", 5, 13)

anime1.intro()
anime2.intro()
anime3.intro()