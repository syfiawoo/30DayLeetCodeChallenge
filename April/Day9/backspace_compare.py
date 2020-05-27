class Solution:
    BACKSPACE_CHAR = '#'  # backspace character

    @staticmethod
    def backspace_compare(word1: str, word2: str) -> bool:
        """
        My strategy for solving this is to use a stack data structure,
        where letters are pushed onto the stack and are popped off
        whenever the backspace character is encountered
        :param word1: a string of characters
        :param word2: a string of characters
        :return: bool:  whether or not the 2 words are the same after applying backspace
        """
        word1_list = Solution.backspace(word1)
        word2_list = Solution.backspace(word2)
        return word1_list == word2_list

    @staticmethod
    def backspace(word: str):
        """
        This function deletes characters that come before the backspace character
        :param word: a string of characters
        :return: list[str]:  a list of characters after backspace has been applied
        """
        new_word = []
        for char in word:
            if new_word and char == Solution.BACKSPACE_CHAR:
                # there is an item on our stack and the current char is backspace
                # pop from stack
                new_word.pop()
            elif char.isalpha():
                # current char is a letter so push on stack
                new_word.append(char)

        return new_word
