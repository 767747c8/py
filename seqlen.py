#!/usr/bin/env python
import json
import argparse
import logging
import os

def run():

    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", help="Name of folder containing *.data.json files", required=True)
    folder = vars(parser.parse_args())["folder"]

    fset = fileset(folder)

    if not fset:
        raise Exception("No '*.data.json' files found in folder")

    print("Total: " + str(sum_files(fset)))

def fileset(folder):

    return [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(".data.json")]

def sum_files(files):

    total = 0

    for file in files:

        logging.info("Parsing file: '%s'", file)

        with open(file) as f:
            for lineno, line in enumerate(f, 1):
                try:
                    json_line = json.loads(line)
                except ValueError:
                    logging.error("Line %d is invalid json", lineno)
                
                seqlen = json_line.get('seqlen', None)

                if not seqlen:
                    logging.error('Failed to get seqlen value on line %d', lineno)
                    continue

                if not isinstance(seqlen, int):
                    logging.error('Seqlen field is not of type int on line %d', lineno)
                    continue

                total += seqlen

    return total


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)-15s %(levelname)s %(filename)s:%(lineno)d: %(message)s",
        level=logging.INFO
    )

    run()
