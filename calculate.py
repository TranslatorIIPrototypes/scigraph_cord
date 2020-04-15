from Normalize import normalize
from co_occur import make_pairs

def go():
    #num_papers = normalize('input','output')
    num_papers=44682
    print(num_papers)
    make_pairs('output',num_papers)


if __name__ == '__main__':
    go()