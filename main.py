import logging

from pomodoro.Timer import Timer

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='./pomodoro/logs/pomodoro.log',
        # filemode='a', # uncomment in production
        filemode='w',  # uncomment in development
    )
    timer = Timer()
