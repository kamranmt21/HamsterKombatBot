[<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/sho6ot)
[<img src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue">](https://www.python.org/downloads/)

![img1](.github/images/demo.png)

> 🇷🇺 README на русском доступен [здесь](README.md)

## ⚙ [Settings](https://github.com/shamhi/HamsterKombatBot/blob/main/.env-example)
| Setting                            | Description                                                                                                                                                                     |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**              | Platform data from which to launch a Telegram session _(stock - Android)_                                                                                                       |
| **MIN_AVAILABLE_ENERGY**           | Minimum amount of available energy, upon reaching which there will be a delay _(eg 100)_                                                                                        |
| **SLEEP_BY_MIN_ENERGY**            | Delay when reaching minimum energy in seconds _(eg [1800,2400])_                                                                                                                |
| **AUTO_UPGRADE**                   | Whether to upgrade the passive earn _(True / False)_                                                                                                                            |
| **MAX_LEVEL**                      | Maximum upgrade level _(eg 20)_                                                                                                                                                 |
| **MAX_PRICE**                      | Maximum upgrade price _(eg 50000000)_                                                                                                                                           |
| **BALANCE_TO_SAVE**                | Balance limit that the bot "won't touch" _(eg 1000000)_                                                                                                                         |
| **UPGRADES_COUNT**                 | The count of cards that the bot will upgrade in 1 lap _(eg 10)_                                                                                                                 |
| **MAX_COMBO_PRICE**                | Maximum purchase price for buying combo cards with an available balance _(eg 10000000)_                                                                                         |
| **PREFER_COMBO_OVER_AUTO_UPGRADE** | Prefer upgrading combo cards over auto-upgrade.<\br>This option will set AUTO_UPGRADE to False if you don't have enough coins for upgrading combo cards in order to save coins. |
| **APPLY_COMBO**                    | Whether to apply the buying and claiming combo cards _(True / False)_                                                                                                           |
| **APPLY_PROMO_CODES**              | Whether to apply the activation promo codes _(True / False)_                                                                                                                    |
| **APPLY_DAILY_CIPHER**             | Whether to apply the claiming daily cipher _(True / False)_                                                                                                                     |
| **APPLY_DAILY_REWARD**             | Whether to apply the claiming daily reward _(True / False)_                                                                                                                     |
| **APPLY_DAILY_ENERGY**             | Whether to apply the activation daily energy boost _(True / False)_                                                                                                             |
| **APPLY_DAILY_MINI_GAME**          | Whether to apply the activation mini game _(True / False)_                                                                                                                      |
| **USE_RANDOM_MINI_GAME_KEY**       | Whether to use random key for mini game cipher _(True / False)_                                                                                                                 |
| **AUTO_COMPLETE_TASKS**            | Whether to complete tasks _(True / False)_                                                                                                                                      |
| **USE_TAPS**                       | Whether to use taps _(True / False)_                                                                                                                                            |
| **RANDOM_TAPS_COUNT**              | Random number of taps _(eg [50,200])_                                                                                                                                           |
| **SLEEP_BETWEEN_TAP**              | Random delay between taps in seconds _(eg [10,25])_                                                                                                                             |
| **USE_RANDOM_DELAY_IN_RUN**        | Whether to use random delay on startup _(True / False)_                                                                                                                         |
| **RANDOM_DELAY_IN_RUN**            | Random delay in run _(eg [0,60])_                                                                                                                                               |
| **USE_RANDOM_USERAGENT**           | Whether to use random User Agent every time to start _(True / False)_                                                                                                           |

## 📕 Профили
Possible to create a profile with unique data for each session:
```json
{
  "session1": {
    "proxy": "socks5://yGow3a:uBro3wL@58.195.21.83:9715",
    "headers": {"...": "..."},
    "fingerprint": {"...": "..."}
  },
  "session2": {
    "proxy": "socks5://yGow3a:uBro3wL@58.195.21.83:9715",
    "headers": {"...": "..."},
    "fingerprint": {"...": "..."}
  },
  "...": {}
}
```
> ❕ **Note**:  `session1` и `session2` - are examples of session names.

## ⚡ Quick Start
1. To install libraries on Windows click on `INSTALL.bat`.
2. To start the bot use `START.bat` (or in console: `python main.py`).

## 📌 Prerequisites
Before you begin, ensure you have the following installed:
- [Python](https://www.python.org/downloads/) version 3.10 or 3.11

## 📃 Getting API Keys
1. Go to [my.telegram.org](https://my.telegram.org) and log in using your phone number.
2. Select **"API development tools"** and fill out the form to register a new application.
3. Note down the `API_ID` and `API_HASH` in `.env` file provided after registering your application.

## 🧱 Installation
You can download [**Repository**](https://github.com/shamhi/HamsterKombatBot) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/shamhi/HamsterKombatBot.git
cd HamsterKombatBot

#Linux
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
playwright install
cp .env-example .env
nano .env # Specify your API_ID and API_HASH
python3 main.py

#Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
copy .env-example .env
# Open .env file and specify your API_ID and API_HASH
python main.py
```
> Installing as a Linux service for running the bot in the background [here](docs/LINUX-SERVIS-INSTALL_EN.md).

⏳ Also for quick launch you can use arguments, for example:
```shell
python3 main.py --action (1/2)
# Or
python3 main.py -a (1/2)

#1 - Create session
#2 - Run clicker
```
