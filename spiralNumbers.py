"""The source of solution: https://github.com/Lintik/CodeFights-Arcade/blob/master/Intro/Land%20of%20Logic/spiralNumbers/code.py3"""
# When you deal with matrices always always always, write matrix indices and visualize them infront of your eyes.
def spiralNumbers(n):
    """Returns a spiral matrix with an incremented number by one."""

    # Create a matrix of size n*n
    ans =[[0]*n for i in range(n)]

    # Incremented counter.
    p = 1

    # Helper variable.
    r = 0

    # How did he came up with this decrementing sequence for this loop.
    for i in range(n,0,-2):

        # Move right.
        for a in range(0,i):
            ans[r][a+r]=p
            p+=1

        # Move down.
        for b in range(r+1,i+r):
            ans[b][i-1+r]=p
            p+=1

        # Move left.
        for c in range(i-2+r,r-1,-1):
            ans[i-1+r][c]=p
            p+=1

        # Move up
        for d in range(i-2+r,r,-1):
            ans[d][r]=p
            p+=1

        r+=1

    return ans

# Solution by lucky-seven...WTF?
def spiralNumbers(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m