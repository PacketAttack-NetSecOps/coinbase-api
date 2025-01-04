# Crypto-Stacked-Bot

### Crypto Currency Stacker Bot Using Coinbase Advanced Trade API, Python, and Docker.


### Table of Contents
1. [Overview](#Overview)
1. [Prerequisites](##Prerequisites)
2. [Getting_Started](##Getting_Started)
3. [Links](##Links)


## Overview

### Coinbase Advanced Trade API
* Any Coinbase user can create an API key allowing programatic trading pair information retrieval and buy/sell orders through the coinbase-advancedtrade Python library.
* By providing this python application with your API Key, webhook URLs, desired trading pairs and buy order conditions, we can establish around-the-clock monitoring of the 24-hour running average price change percentage of each trading pair, and automatically initiate buy orders of a given $ amount as long as the price change percentage remains below our given threshold. This process


#### Example logic:
``` 
8:00 AM: has the USDC value Bitcoin dropped by 4% or more over the last 24 hrs?
<YES> 
Buy Bitcoin equal to 25 USDC.

9:00 AM: has the USDC value Bitcoin dropped by 4% or more over the last 24 hrs?
<YES> 
Buy Bitcoin equal to 25 USDC.

9:00 AM: has the USDC value Bitcoin dropped by 4% or more over the last 24 hrs?
<NO>
Do nothing.
```

### Discord Webhooks
* This project uses discord webhooks to keep you up-to-date with the health status of your bot and notify you of buy orders place or errors. See /config/README.md for more info.
* You can use any messenger service that provides HTTP POST access through a single URL.

## Prerequisites


* A Coinbase account (free)
* A Discord acocunt and server (free)
* Some Linux host running docker that will be up 24/7. (extremely low requirements, maybe an old laptop?)


## Getting_Started

### Pull down the files and build your docker image:

```                                                             
git clone https://github.com/PacketAttack-NetSecOps/coinbase-api
cd coinbase-api
git checkout dockerization                                      
docker build -t crypto-stacked-bot:1.0                          
```                                                             

### Ensure the image tag in docker-compose.yaml matches the tag you chose when building the image.

```                                                             
services:                                                       
  cb-stacked-bot:                                               
    image: crypto-stacked-bot:1.0                               
```                                                             

### Set up your /config and /settings directories using README.md in each directory.

```
docker-compose up -d
```

### Check your discord channels.
* If you recieve price reports for each of your provided trading pairs, you're good to go!
* Any errors from starting docker-composer or running the bot will output to your terminal and post to the URL you specified for bot-errors in /config/webhooks.toml. 


## Links
[Coinbase Advanced API](https://www.coinbase.com/developer-platform/products/advanced-trade-api)  
[rhettre coinbase-advancedtrade-python](https://github.com/rhettre/coinbase-advancedtrade-python)
