from slack import execute_slack_socket_mode
import logging
logging.basicConfig(level=logging.DEBUG)


# slack needs to be run in the main thread
execute_slack_socket_mode()
