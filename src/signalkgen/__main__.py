#!/usr/bin/env python3
"""
gen signal k json for testing the navactor graph features
"""
import argparse
from signalkgen.gen_fdm import gen_fdm
from signalkgen.gen_ddm import gen_ddm

def main():
    """
    entry point
    """
    parser = argparse.ArgumentParser(description='Generate and move boats in Signal K format')
    parser.add_argument('--num-boats', type=int, default=5, help='Number of boats to generate')
    parser.add_argument('--latitude', type=float, default=37.7749,
                        help='Base latitude for generating boats')
    parser.add_argument('--longitude', type=float, default=-122.4194,
                        help='Base longitude for generating boats')
    parser.add_argument('--nautical-miles', type=float, default=10,
                        help='Range in nautical miles for generating boats')
    parser.add_argument('--iterations', type=int, default=3,
                        help='Number of iterations to report on boat navigation')
    parser.add_argument('--interval-dur', type=int, default=1,
                        help='Minutes between iterations and reports')
    parser.add_argument('--hours-ago', type=int, default=12,
                        help='Initial timestamp for each generated observations is HOURS_AGO hours')
    parser.add_argument('--delta-data-model', action='store_true', help='Generate delta data model')
    args = parser.parse_args()

    if args.delta_data_model:
        gen_ddm(args)
    else:
        gen_fdm(args)

if __name__ == "__main__":
    main()
