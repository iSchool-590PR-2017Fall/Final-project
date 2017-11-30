# Title: Predicting the future value of Bitcoins using the BitVaRY® method (an implementation of the GBM Method)

## Team Member(s): Rishabh Mulani, Vasu Choudhary, Yogeshwar Kansara

## Monte Carlo Simulation Scenario & Purpose: 
We are developing a model which attempts to predict future bitcoin values based on historical opening and closing values of bitcoins. The underlying calculation for this model is based on the GBM (Geometrical Brownian Motion) model which is used to predict values of stocks trading in the stock-market. We are using similar fundamental rules to come up with a model which predicts Bitcoin values. We will run a Monte-Carlo simulation by iterating through multiple historical data values and validate them against recent historical values. Then, we will compare how accurate our predictions were. Our goal is to reach a prediction level with 80% accuracy. Our model will compare predictions to actual values for a 30 day period.


## Hypothesis before running the simulation:
HA: The BitVaRY model The BitVaRY model provides at least an 80% accurate prediction of future bitcoin values based on historical bitcoin opening and closing values
H0: The VaRY model is less than 80% accurate in its prediction of future bitcoin values based on historical bitcoin opening and closing values

## Simulation's variables of uncertainty:
Explanatory variables: Opening Price, Closing Price, Date
Response variable: Predicted bitcoin value
For the opening and closing prices, the range is defined by the historical lowest and highest values that the bitcoin held. These values are updated in real-time and the range for both these variables keeps changing as each day passes.
The probability distribution is a normal distribution which is represented by a log function of the price fluctuation over time.

## List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and which probability distribution to use?
Do you think it's a good representation of reality?

## Instructions on how to use the program:
1. Download the "Btc_hist_data.csv" file
2. Download and run the script "bitvary.py"

## Sources Used:
For historical data: https://www.kaggle.com/mczielinski/bitcoin-historical-data 
For problem idea and description & learning about Geometric Brownian Motion: https://www.investopedia.com/articles/07/montecarlo.asp 
Quora.com for articles on predicting stocks & bitcoin values: https://www.quora.com/What-are-some-predictions-for-the-price-of-Bitcoin-or-Litecoin-by-2019
