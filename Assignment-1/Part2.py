class a1part2:

    def main(self):


        print(self.isStringPermutation("ssim","miss"))
        print(self.pairsThatEqualSum([3,2,1,6],5))

        # isStringPermutation(s1: “asdf”, s2: “fsda”) == true
        # isStringPermutation(s1: “asdf”, s2: “fsa”) == false
        # isStringPermutation(s1: “asdf”, s2: “fsax”) == false

    def isStringPermutation(self, s1:str, s2:str) -> bool:

        # no need to check further if this is not true
        if len(s1) != len(s2):
            return False

        map = {}

        # put all frequencies of letter in map
        for i in s2:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        # check if s1 is a permutation
        for i in s1:
            if i in map:
                # decrements a letter every time we see it in s1
                map[i] -= 1
                if map[i] == 0:
                    # if there are no more of that occurrence just remove it from map
                    del map[i]
            else:
                return False
        # if all letters are accounted for, it's a permutation
        if len(map) == 0:
            return True
        return False

    #pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 5) == [(1, 4), (2, 3)]
    #pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 1) == []
    #pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 7) == [(2, 5), (3, 4)]


    def pairsThatEqualSum(self, arr:list, target_sum:int) -> list:

        map = {}
        res = []

        # saves index of each letter, assuming no duplicates
        for i in range(len(arr)):
            map[arr[i]] = i

        # checks if there is a pair that goes with each num in arr
        for i in range(len(arr)):
            if target_sum - arr[i] in map:
                res.append((arr[i],target_sum - arr[i]))
                # deletes the pair found to avoid duplicating results
                del map[arr[i]]
                del map[target_sum-arr[i]]
        return res


instance = a1part2()
instance.main()
