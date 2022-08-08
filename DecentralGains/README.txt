Decentral Games is a casino operating in the Decentraland metaverse. This casino offers multiple digital table games with cryptocurrenty betting options. Rewards are given to players in the casino's currency, DG coin, at a fixed rate, with the rate updating every few weeks. Given that the rate between DG and other bettable tokens is not constant, and given that the odds of the table games are constant, it is possible for the prices of coins to flucuate enough that crypto rewards outperform losses.

WARNING: This script is not ment to endorse gambling. You may lose crypto if by relying on this script. Addtionally, this script does not factor in gas and transfer fees and is not reliable when the polygon blockchain is overloaded, as some transactions fail and must be manually returned.

This script implements the cyrptocompare API, and utilzes game probabilites to determine when the player has an advantage against the house. Kind of like easy card counting. It checks odds on Roulette and Blackjack to see if you will earn more in DG rewards than you will lose with regular play. In many cases, you will need to own expensive NFT outfits to get prefered odds in the casino, this script will tell you how many DG NFT's you would need to own to get the advantage, if any at all. Keep in mind, playing Blackjack would still require you to play a perfect standard game. If you have the advantage in Roulette, you only need to bet on Red and Black. 

Decental Games: decentral.games
Decentral Games Documentation: docs.decentral.games
Decentraland Metaverse: play.decentraland.org

To use, go to https://min-api.cryptocompare.com/ and get a free, individual key for the API.
Plug that key into where it says "API_KEY_HERE".
Ensure you have Python 3.x installed.
Open cryptoCasinoOddsCalculator.py

Be sure to update rates in the rates.txt file if necessary.
