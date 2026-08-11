class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        def reverse(left, right):

            # Base case
            if left >= right:
                return

            # Swap first and last
            s[left], s[right] = s[right], s[left]

            # Move toward the middle
            reverse(left + 1, right - 1)

        reverse(0, len(s) - 1)