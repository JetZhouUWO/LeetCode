这个要多看看
​
![](https://leetcode.com/problems/diagonal-traverse/Figures/498/img1.png)
The first row and the last column in this problem would serve as the starting point for the corresponding diagonal. Given an element inside a diagonal, say [i, j][i,j], we can either go up the diagonal by going one row up and one column ahead i.e. [i - 1, j + 1][i−1,j+1] or, we can go down the diagonal by going one row down and one column to the left i.e. [i + 1, j - 1][i+1,j−1]. Note that this applies to diagonals that go from right to left only. The math would change for the ones that go from left to right.

逻辑:
1. 看要多少个sub arr (N+M-1)个
2. 每个sub arr的head在哪(第0行和第M-1列)
3. 每一个arr都是[r+1, c-1] 往下往左走
4. 走到 r = N了或者c =-1了, 就要停止, r<N, c>-1
5. 看要不要reverse这个array
6. 最后的结果就是每个sub arr 按顺序(进行reverse处理后)合在一起
