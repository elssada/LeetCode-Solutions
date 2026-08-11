class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        #count the frequency of each word in both lists
        count1= Counter(words1)
        count2= Counter(words2)
        #initialize a variable to keep track of the matches
        ans=0
        #initerate through the words that appear only once in words1
        for word, count in count1.items():
            if count ==1 and count2[word]== 1:
                ans+=1
        return ans