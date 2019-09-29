import os
import time
import logging

from .tracker import Tracker
from .app_interaction import AppInteraction


STATE_CACHE_PATH = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'state_cache.bin')


def main():
    app = AppInteraction()
    tracker = Tracker(STATE_CACHE_PATH)

    logger = logging.getLogger('members_tracker')
    logger.setLevel(logging.INFO)
    logger.addHandler(app.get_notification_handler())
    c_handler = logging.StreamHandler()
    c_handler.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s'))
    logger.addHandler(c_handler)

    logger.info('Ready')

    while True:
        added, removed = tracker.update(app.get_members())
        for user in added:
            logger.info('Joined: {}'.format(user))
        for user in removed:
            logger.info('Left: {}'.format(user))

        time.sleep(5)

if __name__ == '__main__':
    main()

