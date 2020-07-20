from Normalize import normalize
from co_occur import make_pairs, make_pairs_by_type

def go():
    #num_papers = normalize('input','output')
    make_pairs_by_type('output')
    print('complete')


if __name__ == '__main__':
    go()
