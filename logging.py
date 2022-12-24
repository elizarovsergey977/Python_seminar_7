from datetime import datetime as dt


def logger(arifmetics):
    path = 'log.scv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign} => {arifmetics}\n')
    f.close()
