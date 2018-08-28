import argparse
import os

class Options:
    directory: str = None

    def __init__(self, directory: str):
        self.directory = directory
    
    def __str__(self):
        return f'Directory: {self.directory}'

    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def from_cli():
        # Create argument parser to program
        parser = argparse.ArgumentParser(
            prog = 'downloader.py',
            description='Save Lehigh Crime Log scrape to a directory of your choice.'
        )

        # Add directory argument of type str
        parser.add_argument(
            '-d', '--directory', metavar='', type=str, default=os.getcwd(),
            help='A (fully specified path to a) directory to be the destination. Ex: "Users/Musa/Documents". Defaults to current working directory.'
        )

        args = parser.parse_args()
        return Options(args.directory)

if __name__ == '__main__':
    print(Options.from_cli())