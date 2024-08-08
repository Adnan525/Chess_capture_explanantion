## Chess Piece Capture Data Generation
Inpit :  
```
e3 c5 d3 d6 c3 g6 Nf3 Bg7 Bd2 Nc6 Na3 Qa5 Qb3 Be6 Qb5 Qxb5 Nxb5 Kd7 Ng5 a6 Na3 Bd5 e4 Be6 Nxe6 Kxe6 Nc4 Nf6 Be2 Kd7 Nb6+ Kc7 Nxa8+ Rxa8 Bg5 e6 Bxf6 Bxf6 O-O d5 exd5 exd5 Bf3 Kd6 Rae1 c4 d4 Ne7 Bg4 h5 Bh3 a5 b3 cxb3 axb3 a4 bxa4 Rxa4 Rb1 Rc4 Rb6+ Rc6 Rxb7 Rxc3 Rb6+ Rc6 Rxc6+ Nxc6 Rd1 Nxd4 Kf1 Nb5 Bc8 d4 Ba6 Nc3 Rc1 Ne4 Bd3 Nd2+ Ke2 Nb3 Rb1 Nc5 Rb6+ Ke5 Rb5 Be7 g3 Kd6 Rb6+ Kc7 Rb5 Kc6 Kf3 Bf6 h4 Kd6 Kf4 Be5+ Kg5 Bg7 Rb6+ Kc7 Rb5 Nxd3 f3 Ne5 Rc5+ Kd6 Rc2 Nxf3+ Kf4 Ne1 Rd2 Be5+ Ke4 Kc5 Kxe5 Nf3+ Kf6 Nxd2 Kxf7 Nf1 Kxg6 Nxg3 Kg5 d3 Kf4 d2 Kxg3 d1=Q Kf4 Qg1 Kf5 Kd4 Kf4 Qg4#
```  
Output :  
```

White: e3, Black: c5
(no capture at White: e3 since White: e3 does not contain 'x')
(no capture at  Black: c5 since  Black: c5 does not contain 'x')

White: d3, Black: d6
(no capture at White: d3 since White: d3 does not contain 'x')
(no capture at  Black: d6 since  Black: d6 does not contain 'x')

White: c3, Black: g6
(no capture at White: c3 since White: c3 does not contain 'x')
(no capture at  Black: g6 since  Black: g6 does not contain 'x')

White: Nf3, Black: Bg7
(no capture at White: Nf3 since White: Nf3 does not contain 'x')
(no capture at  Black: Bg7 since  Black: Bg7 does not contain 'x')

White: Bd2, Black: Nc6
(no capture at White: Bd2 since White: Bd2 does not contain 'x')
(no capture at  Black: Nc6 since  Black: Nc6 does not contain 'x')

White: Na3, Black: Qa5
(no capture at White: Na3 since White: Na3 does not contain 'x')
(no capture at  Black: Qa5 since  Black: Qa5 does not contain 'x')

White: Qb3, Black: Be6
(no capture at White: Qb3 since White: Qb3 does not contain 'x')
(no capture at  Black: Be6 since  Black: Be6 does not contain 'x')

White: Qb5, Black: Qxb5
letter 'x' present in Qxb5
Black Queen captured White Queen at position b5

White: Nxb5, Black: Kd7
letter 'x' present in Nxb5
White Knight captured Black Queen at position b5

White: Ng5, Black: a6
(no capture at White: Ng5 since White: Ng5 does not contain 'x')
(no capture at  Black: a6 since  Black: a6 does not contain 'x')

White: Na3, Black: Bd5
(no capture at White: Na3 since White: Na3 does not contain 'x')
(no capture at  Black: Bd5 since  Black: Bd5 does not contain 'x')

White: e4, Black: Be6
(no capture at White: e4 since White: e4 does not contain 'x')
(no capture at  Black: Be6 since  Black: Be6 does not contain 'x')

White: Nxe6, Black: Kxe6
letter 'x' present in Nxe6
White Knight captured Black Bishop at position e6
letter 'x' present in Kxe6
Black King captured White Knight at position e6

White: Nc4, Black: Nf6
(no capture at White: Nc4 since White: Nc4 does not contain 'x')
(no capture at  Black: Nf6 since  Black: Nf6 does not contain 'x')

White: Be2, Black: Kd7
(no capture at White: Be2 since White: Be2 does not contain 'x')
(no capture at  Black: Kd7 since  Black: Kd7 does not contain 'x')

White: Nb6+, Black: Kc7
(no capture at White: Nb6+ since White: Nb6+ does not contain 'x')
(no capture at  Black: Kc7 since  Black: Kc7 does not contain 'x')

White: Nxa8+, Black: Rxa8
letter 'x' present in Nxa8+
White Knight captured Black Rook at position a8
letter 'x' present in Rxa8
Black Rook captured White Knight at position a8

White: Bg5, Black: e6
(no capture at White: Bg5 since White: Bg5 does not contain 'x')
(no capture at  Black: e6 since  Black: e6 does not contain 'x')

White: Bxf6, Black: Bxf6
letter 'x' present in Bxf6
White Bishop captured Black Knight at position f6
letter 'x' present in Bxf6
Black Bishop captured White Bishop at position f6

White: O-O, Black: d5
(no capture at White: O-O since White: O-O does not contain 'x')
(no capture at  Black: d5 since  Black: d5 does not contain 'x')

White: exd5, Black: exd5
letter 'x' present in exd5
White Pawn captured Black Pawn at position d5
letter 'x' present in exd5
Black Pawn captured White Pawn at position d5

White: Bf3, Black: Kd6
(no capture at White: Bf3 since White: Bf3 does not contain 'x')
(no capture at  Black: Kd6 since  Black: Kd6 does not contain 'x')

White: Rae1, Black: c4
(no capture at White: Rae1 since White: Rae1 does not contain 'x')
(no capture at  Black: c4 since  Black: c4 does not contain 'x')

White: d4, Black: Ne7
(no capture at White: d4 since White: d4 does not contain 'x')
(no capture at  Black: Ne7 since  Black: Ne7 does not contain 'x')

White: Bg4, Black: h5
(no capture at White: Bg4 since White: Bg4 does not contain 'x')
(no capture at  Black: h5 since  Black: h5 does not contain 'x')

White: Bh3, Black: a5
(no capture at White: Bh3 since White: Bh3 does not contain 'x')
(no capture at  Black: a5 since  Black: a5 does not contain 'x')

White: b3, Black: cxb3
letter 'x' present in cxb3
Black Pawn captured White Pawn at position b3

White: axb3, Black: a4
letter 'x' present in axb3
White Pawn captured Black Pawn at position b3

White: bxa4, Black: Rxa4
letter 'x' present in bxa4
White Pawn captured Black Pawn at position a4
letter 'x' present in Rxa4
Black Rook captured White Pawn at position a4

White: Rb1, Black: Rc4
(no capture at White: Rb1 since White: Rb1 does not contain 'x')
(no capture at  Black: Rc4 since  Black: Rc4 does not contain 'x')

White: Rb6+, Black: Rc6
(no capture at White: Rb6+ since White: Rb6+ does not contain 'x')
(no capture at  Black: Rc6 since  Black: Rc6 does not contain 'x')

White: Rxb7, Black: Rxc3
letter 'x' present in Rxb7
White Rook captured Black Pawn at position b7
letter 'x' present in Rxc3
Black Rook captured White Pawn at position c3

White: Rb6+, Black: Rc6
(no capture at White: Rb6+ since White: Rb6+ does not contain 'x')
(no capture at  Black: Rc6 since  Black: Rc6 does not contain 'x')

White: Rxc6+, Black: Nxc6
letter 'x' present in Rxc6+
White Rook captured Black Rook at position c6
letter 'x' present in Nxc6
Black Knight captured White Rook at position c6

White: Rd1, Black: Nxd4
letter 'x' present in Nxd4
Black Knight captured White Pawn at position d4

White: Kf1, Black: Nb5
(no capture at White: Kf1 since White: Kf1 does not contain 'x')
(no capture at  Black: Nb5 since  Black: Nb5 does not contain 'x')

White: Bc8, Black: d4
(no capture at White: Bc8 since White: Bc8 does not contain 'x')
(no capture at  Black: d4 since  Black: d4 does not contain 'x')

White: Ba6, Black: Nc3
(no capture at White: Ba6 since White: Ba6 does not contain 'x')
(no capture at  Black: Nc3 since  Black: Nc3 does not contain 'x')

White: Rc1, Black: Ne4
(no capture at White: Rc1 since White: Rc1 does not contain 'x')
(no capture at  Black: Ne4 since  Black: Ne4 does not contain 'x')

White: Bd3, Black: Nd2+
(no capture at White: Bd3 since White: Bd3 does not contain 'x')
(no capture at  Black: Nd2+ since  Black: Nd2+ does not contain 'x')

White: Ke2, Black: Nb3
(no capture at White: Ke2 since White: Ke2 does not contain 'x')
(no capture at  Black: Nb3 since  Black: Nb3 does not contain 'x')

White: Rb1, Black: Nc5
(no capture at White: Rb1 since White: Rb1 does not contain 'x')
(no capture at  Black: Nc5 since  Black: Nc5 does not contain 'x')

White: Rb6+, Black: Ke5
(no capture at White: Rb6+ since White: Rb6+ does not contain 'x')
(no capture at  Black: Ke5 since  Black: Ke5 does not contain 'x')

White: Rb5, Black: Be7
(no capture at White: Rb5 since White: Rb5 does not contain 'x')
(no capture at  Black: Be7 since  Black: Be7 does not contain 'x')

White: g3, Black: Kd6
(no capture at White: g3 since White: g3 does not contain 'x')
(no capture at  Black: Kd6 since  Black: Kd6 does not contain 'x')

White: Rb6+, Black: Kc7
(no capture at White: Rb6+ since White: Rb6+ does not contain 'x')
(no capture at  Black: Kc7 since  Black: Kc7 does not contain 'x')

White: Rb5, Black: Kc6
(no capture at White: Rb5 since White: Rb5 does not contain 'x')
(no capture at  Black: Kc6 since  Black: Kc6 does not contain 'x')

White: Kf3, Black: Bf6
(no capture at White: Kf3 since White: Kf3 does not contain 'x')
(no capture at  Black: Bf6 since  Black: Bf6 does not contain 'x')

White: h4, Black: Kd6
(no capture at White: h4 since White: h4 does not contain 'x')
(no capture at  Black: Kd6 since  Black: Kd6 does not contain 'x')

White: Kf4, Black: Be5+
(no capture at White: Kf4 since White: Kf4 does not contain 'x')
(no capture at  Black: Be5+ since  Black: Be5+ does not contain 'x')

White: Kg5, Black: Bg7
(no capture at White: Kg5 since White: Kg5 does not contain 'x')
(no capture at  Black: Bg7 since  Black: Bg7 does not contain 'x')

White: Rb6+, Black: Kc7
(no capture at White: Rb6+ since White: Rb6+ does not contain 'x')
(no capture at  Black: Kc7 since  Black: Kc7 does not contain 'x')

White: Rb5, Black: Nxd3
letter 'x' present in Nxd3
Black Knight captured White Bishop at position d3

White: f3, Black: Ne5
(no capture at White: f3 since White: f3 does not contain 'x')
(no capture at  Black: Ne5 since  Black: Ne5 does not contain 'x')

White: Rc5+, Black: Kd6
(no capture at White: Rc5+ since White: Rc5+ does not contain 'x')
(no capture at  Black: Kd6 since  Black: Kd6 does not contain 'x')

White: Rc2, Black: Nxf3+
letter 'x' present in Nxf3+
Black Knight captured White Pawn at position f3

White: Kf4, Black: Ne1
(no capture at White: Kf4 since White: Kf4 does not contain 'x')
(no capture at  Black: Ne1 since  Black: Ne1 does not contain 'x')

White: Rd2, Black: Be5+
(no capture at White: Rd2 since White: Rd2 does not contain 'x')
(no capture at  Black: Be5+ since  Black: Be5+ does not contain 'x')

White: Ke4, Black: Kc5
(no capture at White: Ke4 since White: Ke4 does not contain 'x')
(no capture at  Black: Kc5 since  Black: Kc5 does not contain 'x')

White: Kxe5, Black: Nf3+
letter 'x' present in Kxe5
White King captured Black Bishop at position e5

White: Kf6, Black: Nxd2
letter 'x' present in Nxd2
Black Knight captured White Rook at position d2

White: Kxf7, Black: Nf1
letter 'x' present in Kxf7
White King captured Black Pawn at position f7

White: Kxg6, Black: Nxg3
letter 'x' present in Kxg6
White King captured Black Pawn at position g6
letter 'x' present in Nxg3
Black Knight captured White Pawn at position g3

White: Kg5, Black: d3
(no capture at White: Kg5 since White: Kg5 does not contain 'x')
(no capture at  Black: d3 since  Black: d3 does not contain 'x')

White: Kf4, Black: d2
(no capture at White: Kf4 since White: Kf4 does not contain 'x')
(no capture at  Black: d2 since  Black: d2 does not contain 'x')

White: Kxg3, Black: d1=Q
letter 'x' present in Kxg3
White King captured Black Knight at position g3

White: Kf4, Black: Qg1
(no capture at White: Kf4 since White: Kf4 does not contain 'x')
(no capture at  Black: Qg1 since  Black: Qg1 does not contain 'x')

White: Kf5, Black: Kd4
(no capture at White: Kf5 since White: Kf5 does not contain 'x')
(no capture at  Black: Kd4 since  Black: Kd4 does not contain 'x')

White: Kf4, Black: Qg4#
(no capture at White: Kf4 since White: Kf4 does not contain 'x')
(no capture at  Black: Qg4# since  Black: Qg4# does not contain 'x')

Summary
White captured 13 pieces which are Black Queen, Black Bishop, Black Rook, Black Knight, Black Pawn, Black Pawn, Black Pawn, Black Pawn, Black Rook, Black Bishop, Black Pawn, Black Pawn, Black Knight
Black captured 14 pieces which are White Queen, White Knight, White Knight, White Bishop, White Pawn, White Pawn, White Pawn, White Pawn, White Rook, White Pawn, White Bishop, White Pawn, White Rook, White Pawn

Total Capture
Total 27 pieces were captured in the game

```

## Debug code and known issues
Debug Log:  
```
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] En Passant | Special Chess Move detected assigning Pawn
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] En Passant | Special Chess Move detected assigning Pawn
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] En Passant | Special Chess Move detected assigning Pawn
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] En Passant | Special Chess Move detected assigning Pawn
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[DEBUG] Black move not present, IndexError caught. -- Improved logic will be added
[INFO] Saving File..
```
Error handling -  
- IndexError will be present when last pair does not have a Blacck move which effectively means White has won. A better logic can be added to handle this since during development I worked with even number of moves only
- Special chess move error will occur when we have En Passant. Essentially a pawn will capture an opposition pawn without visiting that sqaure so there will not be any trace of the square on which the capture occurred, resulting the issue.  

## To do
- [ ] Improve error handling logic where required  
- [ ] Address pawn promotion  
- [ ] Address castling  

## Capture analysis (Number only)
```
How many chess pieces have been captured so far in this game - d4 d5 c4 e6 Nc3 Nf6 Bg5 Nbd7 e3 Be7 Nf3 O-O Be2 h6 Bh4 Ne4 Bxe7 Qxe7 Nxe4 dxe4 Nd2 f5 O-O c6 Qc2 Nf6 c5 Nd5 Bc4 Kh8 a3 e5 Qb3 exd4 exd4 Be6 Rae1 Rae8 Re2 Nf4 Re3 Rd8 g3 Bxc4 Qxc4 Nh3+ Kg2 Ng5 h4 Ne6 Nb3 Qd7 Rd1 Nc7 Re2 Nd5 f3 exf3+ Kxf3 f4 Re4 Qh3 Rg1 fxg3+ Ke2 Qh2+?
To analyse each move using Algebraic Notation and count the number of captured pieces, let's go through the game move by move:
1. d4
2. d5
3. c4
4. e6
5. Nc3
6. Nf6
7. Bg5
8. Nbd7
9. e3
10. Be7
11. Nf3
12. O-O
13. Be2
14. h6
15. Bh4
16. Ne4
17. Bxe7 (total capture 1)
18. Qxe7 (total capture 2)
19. Nxe4 (total capture 3)
20. dxe4 (total capture 4)
21. Nd2
22. f5
23. O-O
24. c6
25. Qc2
26. Nf6
27. c5
28. Nd5
29. Bc4
30. Kh8
31. a3
32. e5
33. Qb3
34. exd4 (total capture 5)
35. exd4 (total capture 6)
36. Be6
37. Rae1
38. Rae8
39. Re2
40. Nf4
41. Re3
42. Rd8
43. g3
44. Bxc4 (total capture 7)
45. Qxc4 (total capture 8)
46. Nh3+
47. Kg2
48. Ng5
49. h4
50. Ne6
51. Nb3
52. Qd7
53. Rd1
54. Nc7
55. Re2
56. Nd5
57. f3
58. exf3+ (total capture 9)
59. Kxf3 (total capture 10)
60. f4
61. Re4
62. Qh3
63. Rg1
64. fxg3+ (total capture 11)
65. Ke2
66. Qh2+

<ANSWER>: Capture occurred in: 17. Bxe7, 18. Qxe7, 19. Nxe4, 20. dxe4, 34. exd4, 35. exd4, 44. Bxc4, 45. Qxc4, 58. exf3+, 59. Kxf3, 64. fxg3+
```