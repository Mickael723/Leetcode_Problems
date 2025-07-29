class Solution:
    def permute(self, nums):

        permutation_list = []
        def heap_algo(k: int, curr_permutation):
            if k == 1:
                permutation_list.append(curr_permutation[:])
            
            for i in range(k):
                heap_algo(k - 1, curr_permutation)
                if k % 2 == 0:
                    curr_permutation[i], curr_permutation[k-1] = curr_permutation[k-1], curr_permutation[i]
                else:
                    curr_permutation[0], curr_permutation[k-1] = curr_permutation[k-1], curr_permutation[0]
                    
                    

        heap_algo(len(nums), nums)
        print(permutation_list)

if __name__=="__main__":
    s = Solution()
    s.permute([1,2,3])
                    
