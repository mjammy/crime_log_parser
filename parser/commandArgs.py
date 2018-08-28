import argparse

def getDir():

    # Create argument parser to program
    parser = argparse.ArgumentParser(
        prog = 'downloader.py',
        description='Save Lehigh Crime Log scrape to a directory of your choice.'
        )

    # Add directory argument of type str
    parser.add_argument('-d','--directory', metavar='', type=str, help='a (fully specified path to a) directory to be the destination. Ex: "~/Documents/Lehigh/"')

    # Save args
    args = parser.parse_args()
    return args.directory