import sys
import traceback
import re
from contextlib import contextmanager


@contextmanager
def supresser(*args):
    try:
        yield
    except args:
        pass

@contextmanager
def retyper(type_from, type_to):
    try:
        yield
    except type_from as err:
        tb = sys.exc_info()[-1]
        raise type_to(*err.args).with_traceback(tb)

@contextmanager
def dumper(stream):
    try:
        yield
    except:
        err = sys.exc_info()
        s = str(err[0])
        out = re.sub("class|<|>|\s|'", '', s)
        stream.write(out + ': ' + str(err[1]) + '\n')
        stream.write(traceback.format_exc())
        
