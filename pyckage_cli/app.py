import argparse
from pyckage.fuga import Fuga
from pyckage.hoge import Hoge
from pyckage.submodule.piyo import Piyo

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name',
        default='hoge', type=str,
    )
    args = parser.parse_args()
    if args.name == 'hoge':
        ret = Hoge()()
    elif args.name == 'fuga':
        ret = Fuga()()
    elif args.name == 'piyo':
        ret = Piyo()()
    print('What is called was:', ret)

if __name__ == '__main__':
    main()