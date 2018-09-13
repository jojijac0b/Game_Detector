import GameDetector
import unittest

class HelloWorldTests(unittest.TestCase):
    def test_one(self):
        test = GameDetector.GameDetector()

        map = {"CallOfDutyWW2": ["Call of duty world war two", "COD WW2", "COD WWII","WW2COD"],
            "Fortnite": ["Fortnite", "Fort Nite"],
            "Destiny": ["Destiny", "original Destiny game"],
            "Destiny2": ["Destiny 2", "the last Destiny game", "Destiny II"],
            "WorldOfWarcraft": ["WoW the game", "world of warcraft"]}

        doc = ["I liked the last Destiny game, now I play Fortnite",
            "Lol, no comment about that",
            "I'm still playing world of warcraft since ww2",
            "Destiny 2"]

        sol = ['I liked {Destiny2,the last Destiny game}, now I play {Fortnite,Fortnite}','Lol, no comment about that',
              'I\'m still playing {WorldOfWarcraft,world of warcraft} since ww2', '{Destiny2,Destiny 2}']
        list = test.detectGame(map,doc)

        self.assertEqual(list, sol)

    def test_two(self):
        test = GameDetector.GameDetector()

        map = {"GodOfWar": ['GOW', 'the viking GOW', 'the last god of war','god of war', 'God of War'],
            "NBA2k18": ['2k', 'nba game', 'last 2k'],
            "Fifa17": ['fifa 17'],
            "Fifa18": ['fifa 18', 'soccer game', 'fif', 'the new fifa'],
            "DragonballFighterz": ['Dragonball Fighterz', 'dbz game']}

        doc = ["I liked the viking GOW, now I play fifa",
            "I heard GOW is good",
            "I'm still playing 2k, havent beat the last level yet",
            "Finally got the new fifa after playing fifa 17 for so long",
            "Tha dbz game is good too, but i dont know if its better that fif",
            "God of War is the best game ever",
            "Really? god of war?"]

        sol = ['I liked {GodOfWar,the viking GOW}, now I play fifa',
            'I heard {GodOfWar,GOW} is good', "I'm still playing {NBA2k18,2k}, havent beat the last level yet",
            'Finally got {Fifa18,the new fifa} after playing {Fifa17,fifa 17} for so long',
            'Tha {DragonballFighterz,dbz game} is good too, but i dont know if its better that {Fifa18,fif}',
            '{GodOfWar,God of War} is the best game ever', 'Really? {GodOfWar,god of war}?']

        list = test.detectGame(map,doc)

        self.assertEqual(list, sol)

    def test_empty_map(self):
        test = GameDetector.GameDetector()

        map = {}

        doc = ['hello']

        sol = ['hello']

        list = test.detectGame(map,doc)

        self.assertEqual(list, sol)

    def test_empty_doc(self):
        test = GameDetector.GameDetector()

        map = {"NBA2k18": ['2k', 'nba game', 'last 2k'],
        "Fifa17": ['fifa 17']}

        doc = []

        sol = []

        list = test.detectGame(map,doc)

        self.assertEqual(list, sol)

    def test_repeating_elemnts(self):
        test = GameDetector.GameDetector()

        map = {"NBA2k18": ['2k', 'nba game', 'last 2k'],
        "Fifa18": ['fifa 18', 'the new fifa']}

        doc = ['I got the new nba nba game',
        'the new new fifa is good',
        'fifa fifa fifa 18']


        sol = ['I got the new nba {NBA2k18,nba game}',
        'the new new fifa is good',
        'fifa fifa {Fifa18,fifa 18}']

        list = test.detectGame(map,doc)

        self.assertEqual(list, sol)



if __name__ == '__main__':
    unittest.main()
