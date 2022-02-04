import argparse
from ast import parse
import addAccount
import getAccount

parser = argparse.ArgumentParser(description="ManagerPassword",prog="macc")

parser.add_argument('--add','-a', help="This argument is for add account to storage",action='store_true')
parser.add_argument('--get','-g', help="This argument is for get all account on storage",action='store_true')


if __name__ == "__main__":
    args = parser.parse_args()

    if args.add:
        addAccount()
    elif args.get:
        getAccount()
