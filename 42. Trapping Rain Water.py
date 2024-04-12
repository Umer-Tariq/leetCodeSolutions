class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
          return 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        count = 0

        while l < r:
          if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            count += leftMax - height[l]
          else:
             r -= 1
             rightMax = max(rightMax, height[r])
             count += rightMax - height[r]

        return count
