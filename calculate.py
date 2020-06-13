from Normalize import normalize
from co_occur import make_pairs

def go():
    num_papers = normalize('input','output')
    print(num_papers)
    make_pairs('output',num_papers)
    print('complete')


if __name__ == '__main__':
    go()