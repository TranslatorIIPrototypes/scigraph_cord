from Normalize import normalize
from co_occur import make_pairs, make_pairs_by_type

def go():
    num_papers = normalize('input','output')
    #print(num_papers)
    #make_pairs('output',num_papers)
    make_pairs_by_type('output')
    print('complete')


if __name__ == '__main__':
    go()