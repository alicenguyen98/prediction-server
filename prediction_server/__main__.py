from . import run
from . import config
from . import models_handler
import argparse

if __name__ == '__main__':
    # Parse config path
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=str, help="Path to config", default='./config.json')

    args = parser.parse_args()

    # Init config
    config.init(args.c)

    # Init models handler
    models_handler.init()

    # Run server
    run()
