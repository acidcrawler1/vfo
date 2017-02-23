# table.py
class table (object):
    def p_table(objects, cnames):
        for c in cnames:
            print('{:>5s}'.format(c), end='...')
        print()
        for o in objects:
            for c in cnames:
                print('{}'.format(getattr(o, c)), end='  ')
