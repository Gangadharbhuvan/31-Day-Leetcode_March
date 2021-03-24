'''
    Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9


'''

class Solution:
    def advantageCount(self, A, B):
        n = len(A)
        B = sorted([(num, i) for i, num in enumerate(B)])[::-1]
        A = sorted(A)[::-1]
        ans = [-1]*n
        
        beg, end = 0, n - 1
        
        for num, ind in B:
            if A[beg] > num:
                ans[ind] = A[beg]
                beg += 1
            else:
                ans[ind] = A[end]
                end -= 1
                
        return ans