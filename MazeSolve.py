from pyMaze import maze,agent,COLOR,textLabel
m=maze(15,15)
m.CreateMaze(loopPercent=100,theme='light')
a=agent(m,filled=True,footprints=True,shape='arrow',color='green')
b=agent(m,5,5,filled=True,goal=None,footprints=True,color='red')
c=agent(m,4,2,shape='square',footprints=True,color='yellow')
path2=[(5,4),(5,3),(4,3),(3,3),(3,4),(4,4)]
path3='NNEWWS'
l1=textLabel(m,'Total Cells',m.rows*m.cols)
m.tracePath({a:m.path},delay=100)
m.tracePath({b:path2},delay=100)
m.tracePath({c:path3},delay=100)
print(m.maze_map)
print(m.path)
m.run()


