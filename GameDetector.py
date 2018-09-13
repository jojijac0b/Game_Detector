class TrieNode:
    children = {}
    isGame = False
    game = ''
    tag = ''
    def __init__(self):
        self.children = {}
        self.isGame = False
        self.game = ''
        self.tag = ''

class GameDetector:
    def detectGame(self, map, doc):
        # builds trie and returns root
        root = self.buildTrie(map)
        # adds tags to doc and returns list of modified strings
        ret = self.addTags(map, doc, root)

        return ret

    def addTags(self, map, doc, root):
        ret = []

        for s in doc:
            toAdd = ''
            i = 0
            while i < len(s):
                curr = root
                prev = curr
                index = -1
                for j in range(i, len(s)):
                    if s[j] not in curr.children:
                        break
                    else:
                        curr = curr.children[s[j]]
                        if curr.isGame:
                            prev = curr
                            index = j

                if index >= 0 and curr.isGame:
                    toAdd += '{' + curr.game + ',' + curr.tag + '}'
                    i = index
                else:
                    toAdd += s[i]
                i += 1

            ret.append(toAdd)
        return ret

    def buildTrie(self, map):
        root = TrieNode()

        for game in map:
            for tag in map[game]:
                curr = root
                for i in range(0, len(tag)):
                    if tag[i] not in curr.children:
                        curr.children[tag[i]] = TrieNode()
                    curr = curr.children[tag[i]]

                curr.isGame = True
                curr.game = game
                curr.tag = tag


        return root
