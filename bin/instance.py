import sys
sys.path.append('.')

from stream.instance import Instance


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Instance process.')
    parser.add_argument('module', help='Instance module.')
    parser.add_argument('klass', help='Instance class.')
    parser.add_argument('--manager', help='Stream manager address.',
                        default='ipc:///tmp/0')
    parser.add_argument('--identity', default=None,
                        help='Instance unique id (default: random id)')

    args = parser.parse_args()
    Instance(args.module, args.klass, args.manager, args.identity).run()
