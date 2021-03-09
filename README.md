# The knight's tour problem

Project created as an object of study for the subject of "Projeto e Análise de Algortimos" of the "Ciência da Computação" course of the "Instituto Federal Minas Gerais - IFMG Campus Formiga".

## Description

A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square exactly once. If the knight ends on a square that is one knight's move from the beginning square (so that it could tour the board again immediately, following the same path), the tour is closed; otherwise, it is open.

## Solve

Backtracking is the process offinding a path in a tree which is a solution to a problem by going as far down the tree as possible but, if a solution is not
found, returning to the parent node and then trying the next child. It is the return to the parent node which gives the method its name. Backtracking is a natural for solving the KTP since when we try to do a knight's tour, say by hand, we will frequently get to positions where we have no further moves but have not yet occupied all the squares of the board. At that point we can backtrack and try an alternative move not yet tried. Most of the paths down the tree of sequences of knight's moves will end when the knight has no further moves.
