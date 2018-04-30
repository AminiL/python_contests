import sys
import traceback


def force_load(file_name):
    f = open(file_name + ".py")
    s = f.read()
    l = s.split('\n')
    while True:
        line_number = -1
        tip = "no"
        try:
            exec(s)
        except SyntaxError as err:
            line_number = err.lineno
            tip = "syntax"
            #print(err.args)
        except Exception as err:
            tb = sys.exc_info()[-1]
            line_number = traceback.extract_tb(tb)[-1][1]
            tip = "except"
        if tip == "no":
            break
        else:
            l.pop(line_number - 1)
            s = '\n'.join(l)

    #print(s)
    ldict = {}
    exec(s, globals(), ldict)
    return ldict

