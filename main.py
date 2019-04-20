import argparse


def main(args):
    print('To be developed ' + str(args))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('--start_page', '-p', action="store_true", default=False, help='Starts the webpage server')
    parser.add_argument('--start_crawler', '-c', action="store_true", default=False, help='Starts the webpage server')
    parser.add_argument('--start_indexer', '-i', action="store_true", default=False, help='Starts the webpage server')
    parser.add_argument('--start_ranker', '-r', action="store_true", default=False, help='Starts the webpage server')
    parser.add_argument('--start_all', '-a', action="store_true", default=False, help='Starts the webpage server')
    args = parser.parse_args()
    main(args)
