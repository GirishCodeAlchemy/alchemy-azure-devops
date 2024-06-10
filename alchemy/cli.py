"""Alchemy CLI Package."""

import sys
from datetime import datetime

import argparser

import alchemy


def main(args=None):
    """CLI entry Point."""
    parser = argparser.ArgumentParser()
    subparsers.add_parser("version")
    subparsers = parser.add_subparsers(title="Subcommands", dest="command")

    export_data_parser = subparsers.add_parser("export_data")
    export_data_parser.add_argument(
        "-m",
        "--mode",
        dest="mode",
        help="Select output format",
        required=True,
    )

    export_data_parser.add_argument(
        "-x",
        "--meta_data_xls",
        dest="meta_data_xls",
        help="meta data xlsx file",
        required=True,
    )

    export_data_parser.add_argument(
        "-o",
        "--output_path",
        dest="output",
        help="output path",
        required=True,
    )

    filter_data_parser = subparsers.add_parser("filter_data")
    filter_data_parser.add_argument(
        "-m",
        "--mode",
        dest="mode",
        help="Select output format",
        required=True,
    )

    filter_data_parser.add_argument(
        "-x",
        "--meta_data_xls",
        dest="meta_data_xls",
        help="meta data xlsx file",
        required=True,
    )
    args = parser.parse_args(args if args is not None else sys.argv[1:])
    if args.command == "export_data":
        print("Invoke export code", args.output)
    elif args.command == "filter":
        print("Invoke filter")
    elif args.command == "version":
        print(alchemy.__version__)
    else:
        print(f"Unknown command: {args.command}.")


if __name__ == "__main__":
    main()
