# time complexity: O(n)
# space complexity:O(1)

def isRobotBounded(self, instructions: str) -> bool:


    n =len(instructions)

    x =0
    y = 0

    dirs = [[0,1],[1,0], [0,-1],[-1,0]]

    i = 0

    for k in range(0,4):
        for j in range(n):
            if instructions[j] == 'R':
                i = (i+1)%4 #move forward by 1 reset at end
            elif instructions[j] == 'L':
                i = (i+3)%4 #move back by 1 reset at 0
            else:
                x+=dirs[i][0]
                y+=dirs[i][1]
        #  i not facing north or it's reached origin
        if i!=0 or (x ==0 and y == 0):
            return True

    return False

    