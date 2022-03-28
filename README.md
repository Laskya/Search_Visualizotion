# Search_Visualizotion
Did you ever wonder what would A* and other path finding algortihms look on a square grid?<br>
If yes that's good<br>
If no that's still good<br>

For now there's no async I/O so clicking buttons will have some visible delay
> I'll fix that sometime

## Tutorial
Clicking <kbd>R</kbd> restarts the algorithm only when paused<br>
Clicking <kbd>R</kbd> when algorithm is reseted clears the grid<br>
Clicking <kbd>SPACE</kbd> pauses the algorithm<br>
<kbd>Left Click</kbd> adds (start, end 🟥, wall ⬛) in this order if you delete start it will firstly create a start node<br>
<kbd>Right Click</kbd> deletes stuff ⬜<br>
**Drawing is enabled only when the algorithm has ended<br>
When there is no solution algorithm restarts**

## Legend
- ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) EMPTY NODE
- ![#accf42](https://via.placeholder.com/15/accf42/000000?text=+) START NODE
- ![#ac3712](https://via.placeholder.com/15/ac3712/000000?text=+) END NODE
- ![#000000](https://via.placeholder.com/15/000000/000000?text=+) WALL NODE
- ![#003366](https://via.placeholder.com/15/003366/000000?text=+) CURRENTLY CHECKED NODE
- ![#4cc9f0](https://via.placeholder.com/15/4cc9f0/000000?text=+) NEIGHBOR NODE BEING ADDED TO OPEN SET
- ![#685fab](https://via.placeholder.com/15/685fab/000000?text=+) NODE IN OPEN SET
- ![#808080](https://via.placeholder.com/15/808080/000000?text=+) CHECKED NODE
- ![#ffff00](https://via.placeholder.com/15/ffff00/000000?text=+) PATH NODE

## Visualization
![Example of A star algorithm visualization](a_star.gif)
