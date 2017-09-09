"""Main script of project.

This script launch main functionality of the project.

Its name can be more explicit than main, but is has to be project root to
access all packages.
"""


def main(foo, bar):
    """Main script."""
    raise NotImplementedError


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(
        "TODO: describe "
    )
    parser.add_argument('-F', '--foo', required=True, help='foo')
    parser.add_argument('-B', '--bar', help='bar')
    args = parser.parse_args()

    main(foo=args.foo, bar=args.bar)
