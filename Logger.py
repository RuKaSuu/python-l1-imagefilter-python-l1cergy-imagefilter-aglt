from datetime import datetime


def set_logs(action, message=None):
    """
    display all the actions of a function
    :param action: the function used
    :param message: the message who appeared
    :return: a message in a phonebook.log
    """

    if message is None:
        logMessage ="[" + str(datetime.now()) + "]" + action
    else:
        logMessage ="[" + str(datetime.now()) + "]" + action + " : " + message

    with open('logs/main.log', 'a') as log_file:
        log_file.write(logMessage + '\n')

    print(logMessage)





