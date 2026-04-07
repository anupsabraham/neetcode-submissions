class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        t = 0
        b = m - 1

        while t <= b:
            vm = (t+b)//2
            print(t, b, vm, matrix[vm])

            if matrix[vm][0] <= target <= matrix[vm][n-1]:
                l = 0
                r = n - 1
                while l <= r:
                    hm = (l+r) // 2
                    print(l, r, hm, matrix[vm][hm])
                    if matrix[vm][hm] == target:
                        return True
                    elif matrix[vm][hm] < target:
                        l = hm + 1
                    else:
                        r = hm - 1
                return False
            elif matrix[vm][0] < target:
                t = vm + 1
            elif matrix[vm][n-1] > target:
                b = vm - 1
                
            

        return False