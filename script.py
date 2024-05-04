import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Nehal Parnika G",
            model="ollama:llama3",
        ),
        player_2=Player2(
            nickname="Paarthu G",
            model="anthropic:claude-3-haiku-20240307",
        ),
    )
    return game.run()


if __name__ == "__main__":
    main()
