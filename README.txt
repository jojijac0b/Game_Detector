Game Detector

  Goal:

    Given: A large mapping from a game id to a list of possible n-grams used to refer to the game, and
          a very large body of documents in the form of an array of strings (map, docs)
    Return: The documents with tagged games


  Approach 1:
      Iterate over the docs list, and for every element in said list, try to match every tag found in
      the given mappings using a string matching algorithm, and keep track of the modified Strings

      Time Complexity: O(n*m*k) where n = # of strings in docs, m = # of keys in map,
                                k = time complexity of string matching algorithm(simple matching algorithm runs
                                    in O(x^2 * y), where x = string in doc, y = tag from map)

      Auxiliary Space Complexity: O(1)


      Ok solution, but it is very inefficient for big sets of data, like the one we are expected to be working with

  Approach 2:
      Use a trie to log all the tags that are of interest to us. Then iterate over the docs list, and as you see a tag
      that is assigned to a game, modify string and add to return list.

      Time Complexity: O(a) to build trie where a = total # characters found in all tags in map
                        +
                       O(n*m^2) to iterate over doc Strings where n = # of strings in docs,
                                m = longest length of String in doc

      Auxiliary Space Complexity: O(n) where n = number of characters in all tags combined


    Since the problem statement stressed the fact that we would be working with large sets of data, Approach 2 using
    a trie is the best option. Even though it uses more space, it is faster, allowing us to work with bigger sets of
    data in less time.

  Pseudocode:

    * build trie:
        - For simplicity make a trienode class that keeps track of a nodes children, whether it is a game, and the name and tag
          of the game if it is one.

    * update docs:
        - Iterate over docs using trie to match substrings with tags.
        - This will be n^2 operation, where n = length of string, for every element in docs because at each index, we check if
          that index is the start of a tag string
        - Since strings are immutable in python, we would need to create, and build up our answer instead of modifying the original
          string.

  Things to note:
      - My solution will be case sensitive.
      - My solution will tag a substring even if it is within another. For example if I had a key value pair {Spiderman : {spider game}}, and
        the string "that sssspider game" would be modified to "that sssTAG{Spiderman,spider game}". I chose to do this because I wanted to get
        any tag even if it is in a typo. Even if it is a typo it is still a mention so I felt like it was unnecessary to deal with this case.

  Edge Cases:

      * sequels/tags within tags:
          - Problem: If both 'Destiny' and 'Destiny 2' are in our mappings for 'Destiny' and 'Destiny2' respectively, when given a doc 'Destiny 2'
            we should return '{Desting2 , Destiny 2}' instead of '{Destiny , Destiny} 2'
          - Solution: Do not stop traversing string once you've found a valid tag. Instead, keep searching until the substring is no longer
            valid and return the most recent game found.
