import logging
from concurrent.futures import ThreadPoolExecutor

import pygame

assets = {}
loadingFinished = False
logger = logging.getLogger(__name__)


class worker:
    def __init__(self, loadFunc, path, key, args=None):
        self.loadFunc = loadFunc
        self.path = path
        self.key = key
        self.args = args
        self.run()

    def run(self):
        logger.debug(f"Started:  {self.key}")
        if self.args is not None:
            assets[self.key] = self.loadFunc(self.path, *self.args)
        else:
            assets[self.key] = self.loadFunc(self.path)
        logger.debug(f"Finished: {self.key}")


def load():
    threads = []
    threads.extend(
        [
            worker(pygame.image.load, "assets/bullet.png", "bullet"),
            worker(pygame.image.load, "assets/Ship-Blue-005.png", "player"),
        ]
    )
    with ThreadPoolExecutor(max_workers=4) as executor:
        [executor.submit(t) for t in threads]
    loadingFinished = True
