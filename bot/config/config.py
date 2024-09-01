from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 0
    API_HASH: str = ''

    MIN_AVAILABLE_ENERGY: int = 100
    SLEEP_BY_MIN_ENERGY: list[int] = [1800, 2400]

    AUTO_UPGRADE: bool = True
    MAX_LEVEL: int = 20
    MAX_PRICE: int = 50000000

    BALANCE_TO_SAVE: int = 1000000
    UPGRADES_COUNT: int = 10

    MAX_COMBO_PRICE: int = 10000000

    PREFER_COMBO_OVER_AUTO_UPGRADE: bool = True

    APPLY_COMBO: bool = True
    APPLY_PROMO_CODES: bool = True
    APPLY_DAILY_CIPHER: bool = True
    APPLY_DAILY_REWARD: bool = True
    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_MINI_GAME: bool = True

    SLEEP_MINI_GAME_TILES: list[int] = [600, 900]
    SCORE_MINI_GAME_TILES: list[int] = [300, 500]
    GAMES_COUNT: list[int] = [1, 10]

    AUTO_COMPLETE_TASKS: bool = True

    USE_TAPS: bool = True
    RANDOM_TAPS_COUNT: list[int] = [50, 200]
    SLEEP_BETWEEN_TAP: list[int] = [10, 25]

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 60]

    USE_RANDOM_USERAGENT: bool = True

    ACTION: int = 0


settings = Settings()
