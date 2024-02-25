class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
            m, n = len(img), len(img[0])
            result = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    total, count = 0, 0
                    for r in range(i-1, i+2):
                        for c in range(j-1, j+2):
                            if 0 <= r < m and 0 <= c < n:
                                total += img[r][c]
                                count += 1
                    result[i][j] = total // count

            return result