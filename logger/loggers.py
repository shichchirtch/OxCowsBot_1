import logging, sys

logging.basicConfig(level='WARNING',
                    filename='my_log_for_U_Bot.log',
                    encoding='utf-8',
                    filemode='w',
                    format='[{asctime}] #{levelname:8} {filename}:'
                           '{lineno} - {name} - {message}',
                    style='{'
                    )

class My_DATA_LogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'WARNING'

logger = logging.getLogger('FILE_LOGGER')
logger.setLevel("WARNING")
file_handler = logging.FileHandler('log_for_Ox_Bot', mode='w', encoding='utf-8')
file_handler.addFilter(My_DATA_LogFilter())
logger.addHandler(file_handler)



std_out_logger = logging.getLogger('STD_out') # for bot actions
std_out_logger.setLevel("INFO")
std_out_handler = logging.StreamHandler(sys.stdout)
std_out_logger.addHandler(std_out_handler)



std_err_logger = logging.getLogger('ERR_out')  # for user actions
std_err_logger.setLevel("INFO")
std_err_handler = logging.StreamHandler(sys.stderr)
std_err_logger.addHandler(std_err_handler)