# Robot Problem
This program simulates a robot moving on a 5x4 grid. The grid has 4 rows (numbered 0–3) and 5 columns (numbered 0–4). The robot starts at position **(0,0)** facing **South (S)**.

## "MSMMEMM"
1. **Initial State:** (0,0,S)
2. **M:** Move south from (0,0)  (1,0)
3. **S:** Already facing South; no change - (1,0,S)
4. **M:** Move south from (1,0) - (2,0)
5. **M:** Move south from (2,0) - (3,0)
6. **E:** Change direction to East - (3,0,E)
7. **M:** Move east from (3,0) - (3,1)
8. **M:** Move east from (3,1) - (3,2)

Final output: (3, 2, E)
