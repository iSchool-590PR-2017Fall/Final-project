2017Fall 590PR Final Project 
==========

A brief introduction on our project about **M**onte **C**arlo **S**imulation. 

> ***We are still learning, but for sure will try our best.***
> @ [*Yingjun Guan*](https://ischool.illinois.edu/people/phd-students/yingjun-guan)
> @ [*Lan Li*](https://www.linkedin.com/in/lan-li-42682214a/)


## Title: 
  Monte Carlo Simulation for Tic-tac-toe Game
  
  ![Tic-tac-toe](https://lh3.googleusercontent.com/EgfiSB2bdf7kuRfNQbe8Jaj_bhfrlfeRt2nzphA6jcbCQdy5iEku2uZyK-5_VWtWUCxi=w300)

## Team Member(s):
  Yingjun Guan, Lan Li

## Project
### Background:
[Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) is a world famous game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

[Monte Carlo Simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method) is a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. 

*Our project* focuses on applying the Monte Carlo Simulation into training the machine to how to play tic-tac-toe _wisely_.

### Hypothesis:
+ [ ] **Absolute randomness** - For any specific situation, the machine will try any blank spot, with an absolute randomness. In our case, the decision is on the basis of the simulation, which is on and only on the basis of randomness.
+ [ ] **random variable series** - Each step will be a different situation which will call a MCS for the decision, and the whole game is based on the collabraton of all MCS.
+ [ ] **No human experiences involved** - The program contains the idea of Exhaustive Attack method and the spirit of traversal, on the other hand, no human experience of the game is needed.
+ [ ] **Back propagation** - Further algorithms helped to better abstract the decision from the simulation.

### Purpose:
 - We are ambitious enough to generate a human-computer interactive GUI medium for playing the game. 
 - The player can choose to play on the offensive position or the defensive position.
 - The program can use the MCS to make the (best) decision.
 
### Algorithm:
 - The whole program applies the idea of recursion. The following figure can also helps to clarify the algorithm.
 ![try1](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Tic-tac-toe-game-tree.svg/2000px-Tic-tac-toe-game-tree.svg.png)
 

## Sources Used:
  #
  Software:
Python 3.6 (PythonCharm), PyQT for UI
  #
  Algorithm:
Backpropagation

![try2](https://never-stop-building-blog-production.s3.amazonaws.com/pictures/minimax/full-minimax-move-tree.png)
 
https://neverstopbuilding-dropblog.herokuapp.com/minimax
