
class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        required = [0] * 26

        # Step 1: Combine requirements from words2
        for word in words2:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                required[i] = max(required[i], count[i])

        # Step 2: Check candidates from words1
        answer = []

        for word in words1:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            for i in range(26):
                if count[i] < required[i]:
                    break
            else:
                answer.append(word)

        return answer
