"""
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

import itertools


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxzy"
        }

        if not digits:
            return []

        # ans is basically cartesian product of the represented letters.
        return ["".join(l) for l in itertools.product(*[phone_dict[d] for d in digits])]

    # http://www.cnblogs.com/zuoyuan/p/3779761.html
    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                dfs(num + 1, string + letter, res)

        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
                }
        res = []
        length = len(digits)
        dfs(0, '', res)
        return res

    # for loop
    # https://gengwg.blogspot.com/2018/02/leoleetcode-16-sum-closest-letter.html
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxzy"
        }

        res = []
        for d in digits:
            if len(res) == 0:
                for c in phone_dict[d]:
                    res.append(c)
            else:
                temp_res = []
                for x in res:
                    for c in phone_dict[d]:
                        temp_res.append(x + c)
                res = temp_res
        return res

    def letterCombinations(self, digits):

        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxzy"
        }

        if not digits:
            return []
        return reduce(lambda results, digit: [result + letter
                                              for result in results
                                              for letter in phone_dict[digit]],
                      digits, [''])
if __name__ == '__main__':
    print Solution().letterCombinations("23")
    print Solution().letterCombinations("234")
    print Solution().letterCombinations("")
