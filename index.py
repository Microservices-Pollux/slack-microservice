from slack import execute_slack_socket_mode
from publish import publish
from consume import consume
import logging
logging.basicConfig(level=logging.DEBUG)


publish()
consume()

execute_slack_socket_mode()
