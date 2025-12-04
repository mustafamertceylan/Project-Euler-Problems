mygrid=[[0]*20 for i in range(20)]
"""for i in range(20):
    for j in range(20):
        print(mygrid[i][j],end="---")
    print("")"""


def RouteCounter(rightCount, downCount, path=""):
    if rightCount == 0 and downCount == 0:
        return [path] 
    all_paths = [] 
    if rightCount > 0:
        paths_from_right = RouteCounter(rightCount - 1, downCount, path + "R")
        all_paths.extend(paths_from_right) 
    if downCount > 0:
        paths_from_down = RouteCounter(rightCount, downCount - 1, path + "D")
        all_paths.extend(paths_from_down) 
    return all_paths
routeList = RouteCounter(20, 20, "")

print(routeList)


def pathCounter(columnNumbers=20,lineNumbers=20):
    sum1=columnNumbers+lineNumbers
    sum2=1
    sum3=1
    numberOfPath=1
    for i in range(1,sum1+1):
        numberOfPath*=i
        if i<=columnNumbers:
            sum2*=i
        if i<=lineNumbers:
            sum3*=i
    numberOfPath/=(sum3*sum2)
    return numberOfPath

print(pathCounter())

    
