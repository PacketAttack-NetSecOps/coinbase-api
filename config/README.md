# config File Guide

#### The config files follow a specific format to be compatible with src, but are personalized with your sensative information that is passed safely from your host machine to docker via the secrets top-level element in docker-compose.

## cdp_api_key.json

#### You can either transfer the file to the host machine and replace the example file in /config, or you can copy and paste your name and privateKey values into the example file if that's easier.

[Coinbase Advanced Trade API key creation](https://help.coinbase.com/en/exchange/managing-my-account/how-to-create-an-api-key)

## webhooks.toml

#### Create your three channels in discord and provide the full urls in the /config/webhooks.toml.
[Discord Webhooks](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)

* Contains three seperate, private webhook URLs:
* price-bot: posts hourly updates on the trading pairs you specifiy in /settings/bot-settings.toml
    * You can mute this channel, but keep an eye on it to monitor the health of the bot.
* buy-bot: keep notifications on for this channel, this channel notifies you if the bot places and buys on your behalf.
* bot-errors: keep notifications for this one as wlel, this will tell you if any errors occur, and is very useful for initial troubleshootings.
