import datetime
from dateutil.parser import parser
from dateutil.tz import *
timezone = {'PDT': gettz('America/Los_Angeles')}

def parser(time):
    return parse(time, tzinfos=timezone, fuzzy=True)
