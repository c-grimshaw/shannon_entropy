#!/usr/bin/env python3

from collections import Counter
from dataclasses import dataclass
from typing import IO

import argparse
import math
import sys


@dataclass
class Arguments:
    """Represents the command-line arguments for the program.

    Attributes:
        n (int): The size of the n-gram window.
        user_input (IO): The input file or stream to read from.
        verbose (bool): Flag indicating whether to preserve the original input column.
    """

    n: int
    user_input: IO
    verbose: bool


def read_arguments() -> Arguments:
    """Reads command-line arguments and returns an argument object.

    Parses the command-line arguments provided by the user and constructs
    an Arguments object containing the parsed values. The function uses
    the argparse module to define and handle the command-line interface.

    Returns:
        An Arguments object populated with the parsed values.
    """
    parser = argparse.ArgumentParser(
        prog="shannon-entropy calculator",
        description="Calculates the Shannon-Entropy of inputs from stdin",
    )

    parser.add_argument(
        "-n",
        "--ngrams",
        dest="n",
        type=int,
        choices=range(1, 5),
        help="size of n-gram window",
    )
    parser.add_argument(
        "-r",
        "--read-file",
        dest="user_input",
        type=argparse.FileType("r"),
        default=(None if sys.stdin.isatty() else sys.stdin),
        help="input file to read from",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="preserve original input column",
    )

    args = parser.parse_args()
    return Arguments(**vars(args))


def shannon_entropy(word: str, n: int) -> float:
    """Calculates the Shannon entropy of the input using n-gram tokens.

    This function computes the Shannon entropy of a given word using n-gram tokens.
    Shannon entropy is a measure of the average amount of information contained
    in each token of the word. It provides an indication of the uncertainty or
    randomness in the distribution of n-grams within the word.

    Args:
        word (str): The input word to calculate entropy for.
        n (int): The size of the n-gram window.

    Returns:
        float: The calculated Shannon entropy.

    Examples:
        >>> shannon_entropy("hello, world!", 2)
        3.6682958340544896
        >>> shannon_entropy("google.ca", 1)
        3.2810361125534233
    """
    ngrams = Counter(word[i : i + n] for i in range(0, len(word) - n + 1))

    total_population = sum(ngrams.values())
    entropy = 0.0
    for value in ngrams.values():
        probability = value / total_population
        entropy += probability * math.log2(1 / probability)

    return entropy


def main():
    """Entry point of the program.

    Reads command-line arguments, processes input lines, and calculates Shannon entropy.
    This function serves as the main entry point for the program execution.
    """
    args = read_arguments()
    for line in args.user_input.readlines():
        line, n = line.strip(), args.n

        entropy = shannon_entropy(line, n)
        if args.verbose:
            print(f"{line}\t{entropy}")
        else:
            print(entropy)


if __name__ == "__main__":
    main()
