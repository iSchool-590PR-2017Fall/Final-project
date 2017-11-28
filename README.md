2017Fall 590PR Final Project 
==========

A brief introduction on our project about **M**onte **C**arlo **S**imulation. 

![dwyl-logo-wide](https://cloud.githubusercontent.com/assets/194400/8141150/f4b4c854-115a-11e5-8c13-dc96a5f1e928.png)

> ***We are still learning, but for sure will try our best.***.
> ~ [*Arthur Ashe*](http://en.wikipedia.org/wiki/Arthur_Ashe)


# Title: 
  Monte Carlo Simulation for Tic-tac-toe Game
## Team Member(s):
  Yingjun Guan, Lan Li

# Monte Carlo Simulation Scenario & Purpose:
  #
  Scenario:
  One fool ( Monte Carlo) plays tic-tac-toe with the player(human being). Tic-tac-toe is 3*3 grid where the winning rule is to mark three    in one horizontal , vertical or diagonal row.
  #
  Purpose:
  After many random travsing simulations and backpropagation, we can come to best policy for every round movement.
         

### Hypothesis before running the simulation:
  As there is no policy or strategy for Monte Carlo, it will randomly choose all possible positions. Human have policy to win, in this way, it will fail for many times.

### Simulation's variables of uncertainty
  There is no tactics for every round. In this way, all of the blank positions are available to choose. For every MC(Monte Carlo) layer (round), we set multiple moving probabilities as random variables.Expand next move from all of the possible positions, using Monte Carlo to simulate all rounds. For each result(win or lose or fair),  we use backpropagation to score every MC layer steps. And after many times simulations, we can get best policy for this game.
  #
  Round 1, there are 9 random variables(available positions);
  #
  Round 2, there are 7 random variables(available positions);
  #
  Round 3( expect result round), there are 5 random variables(available positions);
  #
  Round 4( expect result round), there are 3 random variables(availbale positions);
  #
  Round 5( expect result round), there is 1 position.
  #
  This is the whole possible procedure for Tic-tac-toe game, where it's a good representation of reality.

"""
check here
"""
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). 
For each such variable, how did you decide the range and which probability distribution to use?  
Do you think it's a good representation of reality?

## Instructions on how to use the program:
  This is a human-computer interaction game. The player will play with computer.For each round, player will react and make a decision for next step. 

## Sources Used:
  #
  Software:
Python 3.6 (PythonCharm), PyQT for UI
  #
  Algorithm:
Backpropagation
