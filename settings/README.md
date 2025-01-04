# Bot settings instructions

* settings/bot-settings.toml allows users to specifiy the buy order parameters for and number of coinbase trading pairs.
* <b>Personalize the settings in this file, the example settings do not guarentee positive results.</b>
* Use an online TOML validator to avoid trivial errors.

```
[BTC_USDC]
GLOBAL_PRODUCT_ID = "BTC-USDC"
GLOBAL_NEG_THRESHOLD = -4
GLOBAL_BUY_INCREMENT = "10"

[SOL_USDC]
GLOBAL_PRODUCT_ID = "SOL-USDC"
GLOBAL_NEG_THRESHOLD = -4
GLOBAL_BUY_INCREMENT = "10"
```


* ```[BTC-USDC]``` Is the dictionary key looped over by the bot, this shoud match the trading pair specified below.
* ```GLOBAL_PRODUCT_ID = "BTC-USDC"``` - the coinbase trading pair assessed by bot.
* ```GLOBAL_NEG_THRESHOLD = -4``` - represents the 24h running average percent price change of the specified trading pair. If the percent pricechange is below this threshold, the bot will place a buy order every hour. The bot will cease purchasing when the 24h running average percent price change rises above the threshold value.
* ```GLOBAL_BUY_INCREMENT = "10"``` - the amount in USDC that the bot will buy every hour.
* To add a trading pair, simply replicate the section for a preexisting trading pair and update the dictionary key, GLOBAL_PRODUCT_ID GLOBAL_NEG_THRESHOLD, and GLOBAL_BUY_INCREMENT.