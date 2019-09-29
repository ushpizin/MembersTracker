# MembersTracker
![](https://img.shields.io/badge/quality-works,_not_proud-orange)

Telegram API doesn't provide API for watching for changes in the list of members of a private channel.
This project solves that by sampling the list of members periodically.

Each new member that joins/lefts the channel will send a notification via Telegram bot.

## Quick Start
1. Register a [Telegram app](https://my.telegram.org/), and write the `API_ID` and `API_HASH` in `credentials.py`.
2. Create a [Telegram bot](https://telegram.me/botfather), and write the `BOT_TOKEN` in `credentials.py`.
3. Set your phone number (`CLIENT_PHONE`) in `credentials.py`.
4. Set the invite code for the channel (`CHANNEL_INVITE_CODE`) in `credentials.py`. The invite code is the code-part of the invite link (`https://t.me/joinchat/<invite-code>`).
5. Run: `python -m memberstracker`.
