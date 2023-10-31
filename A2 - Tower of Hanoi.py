#Use recursion to move all the disks to another tower (3 towers):
#- One disk can be moved at any given time
#- Only the "top" disk can be removed
#- No large disk can sit over a small disk

moves = 0
def TowerOfHanoi(disks, StartRod, EndRod, UnusedRod): 
  global moves
  if disks == 0: 
    return
  TowerOfHanoi(disks-1, StartRod, UnusedRod, EndRod) 
  print("Move disk", disks, "from rod", StartRod, "to rod", EndRod) 
  moves = moves + 1
  TowerOfHanoi(disks-1, UnusedRod, EndRod, StartRod)

TowerOfHanoi(3, 'A', 'C', 'B') 
print('\nTotal moves required:', moves)
