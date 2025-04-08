from slack import execute_slack_socket_mode
from publish import publish
from consume import consume
import logging
logging.basicConfig(level=logging.DEBUG)


# consume needs to be run in the main thread
consume()

# publish.py could be called anywhere
publish()

# slack needs to be run in the main thread
execute_slack_socket_mode()
