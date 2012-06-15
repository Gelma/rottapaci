"Stupid package to log"

import datetime, multiprocessing

lock_logit = multiprocessing.Lock() # fix namespace

def log(*args):
    """I receive strings/iterable objects, convert them to text and put somewhere."""

    output_to = "stdout" # ('file','stdout','syslog')

    log_line = datetime.datetime.now().strftime('%H:%M:%S') + ': '

    try:
        log_line += ' '.join(args)
    except: # so, something isn't txt
        for item in args:
            log_line += ' %s' % item

    with lock_logit:
        if output_to == "stdout":
            print log_line
            return

        if output_to == "file":
            log_file.write(linea_log + '\n')
            log_file.flush()
