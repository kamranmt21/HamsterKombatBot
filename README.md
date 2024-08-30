[<img src="https://img.shields.io/badge/Telegram-%40Me-orange">](https://t.me/sho6ot)
[<img src="https://img.shields.io/badge/python-3.10%20%7C%203.11-blue">](https://www.python.org/downloads/)

![img1](.github/images/demo.png)

> 🇪🇳 README in english available [here](README-EN.md)

## ⚙ [Настройки](https://github.com/shamhi/HamsterKombatBot/blob/main/.env-example)
| Настройка                          | Описание                                                                                                                                                                        |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**              | Данные платформы, с которой запускать сессию Telegram _(сток - Android)_                                                                                                        |
| **MIN_AVAILABLE_ENERGY**           | Минимальное количество доступной энергии, при достижении которой будет задержка _(напр. 100)_                                                                                   |
| **SLEEP_BY_MIN_ENERGY**            | Задержка при достижении минимальной энергии в секундах _(напр. [1800,2400])_                                                                                                    |
| **AUTO_UPGRADE**                   | Улучшать ли пассивный заработок _(True / False)_                                                                                                                                |
| **MAX_LEVEL**                      | Максимальный уровень прокачки апгрейда _(напр. 20)_                                                                                                                             |
| **MAX_PRICE**                      | Максимальная цена прокачки апгрейда _(напр. 50000000)_                                                                                                                          |
| **BALANCE_TO_SAVE**                | Лимит баланса, который бот "не тронет" _(напр. 1000000)_                                                                                                                        |
| **UPGRADES_COUNT**                 | Количество карточек, который бот прокачает за 1 круг _(напр. 10)_                                                                                                               |
| **MAX_COMBO_PRICE**                | Максимальная цена покупки для покупки комбо при доступном балансе _(напр. 10000000)_                                                                                            |
| **PREFER_COMBO_OVER_AUTO_UPGRADE** | Prefer upgrading combo cards over auto-upgrade.<\br>This option will set AUTO_UPGRADE to False if you don't have enough coins for upgrading combo cards in order to save coins. |
| **APPLY_COMBO**                    | Использовать ли покупку и активацию комбо карт _(True / False)_                                                                                                                 |
| **APPLY_PROMO_CODES**              | Применять ли активацию промокодов _(True / False)_                                                                                                                              |
| **APPLY_DAILY_CIPHER**             | Применять ли ввод ежедневного шифра _(True / False)_                                                                                                                            |
| **APPLY_DAILY_REWARD**             | Применять ли сбор ежедневной награды _(True / False)_                                                                                                                           |
| **APPLY_DAILY_ENERGY**             | Применять ли активацию ежедневного буста энергии _(True / False)_                                                                                                               |
| **APPLY_DAILY_MINI_GAME**          | Применять ли активацию мини игры _(True / False)_                                                                                                                               |
| **USE_RANDOM_MINI_GAME_KEY**       | Использовать ли рандомный ключ для шифра мини игры _(True / False)_                                                                                                             |
| **AUTO_COMPLETE_TASKS**            | Выполнять ли задания _(True / False)_                                                                                                                                           |
| **USE_TAPS**                       | Использовать ли тапы _(True / False)_                                                                                                                                           |
| **RANDOM_TAPS_COUNT**              | Рандомное количество тапов _(напр. [50,200])_                                                                                                                                   |
| **SLEEP_BETWEEN_TAP**              | Рандомная задержка между тапами в секундах _(напр. [10,25])_                                                                                                                    |
| **USE_RANDOM_DELAY_IN_RUN**        | Использовать ли рандомную задержку при запуске _(True / False)_                                                                                                                 |
| **RANDOM_DELAY_IN_RUN**            | Рандомная задержка при запуске _(напр. [0,60])_                                                                                                                                 |
| **USE_RANDOM_USERAGENT**           | Использовать ли рандомный User Agent при каждом новом запуске _(True / False)_                                                                                                  |

## 📕 Профили
Для каждой сессии можно создать профиль с уникальными данными:
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
> ❕ **Примечание**:  `session1` и `session2` - это примеры названий сессий.

## ⚡ Быстрый старт
1. Чтобы установить библиотеки в Windows, запустите INSTALL.bat.
2. Для запуска бота используйте `START.bat` (или в консоли: `python main.py`).

## 📌 Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [Python](https://www.python.org/downloads/) версии 3.10 или 3.11.

## 📃 Получение API ключей
1. Перейдите на сайт [my.telegram.org](https://my.telegram.org) и войдите в систему, используя свой номер телефона.
2. Выберите **"API development tools"** и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## 🧱 Установка
Вы можете скачать [**Репозиторий**](https://github.com/shamhi/HamsterKombatBot) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/shamhi/HamsterKombatBot.git 
cd HamsterKombatBot

# Linux
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
playwright install
cp .env-example .env
nano .env  # Укажите ваши API_ID и API_HASH
python3 main.py

# Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
copy .env-example .env
# Откройте файл .env и укажите ваши API_ID и API_HASH
python main.py
```
> Установка в качестве Linux службы для фоновой работы бота [тут](docs/LINUX-SERVIS-INSTALL.md).

⏳ Также для быстрого запуска вы можете использовать аргументы, например:
```shell
python3 main.py --action (1/2)
# Или
python3 main.py -a (1/2)

# 1 - Создает сессию
# 2 - Запускает кликер
```
