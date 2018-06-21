originalBet = 0.0082
originalOdds = 1.719

hedgeOdds = 3.65

totalOriginalInvestment = round(originalBet + (originalBet * (originalOdds - 1.0)), 5)
hedgeBet = round(totalOriginalInvestment/(hedgeOdds), 5)
newProfit = round(hedgeBet * (hedgeOdds - 1.0), 5)
prof = (hedgeBet+newProfit) - (originalBet+hedgeBet)
effective_odds = round(prof/(originalBet+hedgeBet), 4)

print ("Original Bet: " + str(originalBet) + " to win " + str((originalBet * (originalOdds - 1.0))) + " = " +  str(totalOriginalInvestment))
print ("Hedge Bet: " + str(hedgeBet) + " to win " + str(newProfit) + " = " +  str(hedgeBet + newProfit))
print ("Profit: " + str(prof))
print ("Effective Odds: " + str(1 + effective_odds))