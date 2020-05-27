class Solution:
    @staticmethod
    def group_anagrams(words):
        """
        My strategy for solving this is sorting each word
        and using the sorted word as the key in a dictionary.
        :param words: a list containing words
        :return: list[list[str]]:  maximum profit to be made
        """
        groups = {}
        for word in words:
            # sort the current word
            sorted_word = ''.join(sorted(word))
            # check if the sorted word is a key in the dict
            if sorted_word not in groups:
                groups[sorted_word] = [word]
            else:
                groups[sorted_word].append(word)

        return groups.values()
