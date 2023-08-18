import argparse
from typing import List

def scrape_board(api:str, url:List[str], collage:bool):

    # get scraper type

    # scrape

    # process
    pass




def main():
    # top level parser
    parser = argparse.ArgumentParser(description='Processes pinterest images')
    parser.add_argument('url', type=str, action='append', help='Pinterest Board URL')  # can scrape multiple boards
    parser.add_argument('api', type=str, help='Pinterest API Key')
    parser.add_argument('loc', metavar='saveLocation', help='Location to save parsed results')
    subparsers = parser.add_subparsers(title='mode', dest='mode', required=True)

    # subparsers
    subparsers.add_parser('save', help='Save pins as images in a folder')

    collage_subparser = subparsers.add_parser('collage', help='Create collage of pins')
    collage_subparser.add_argument('minHeight', metavar='MinimumImageHeight',
                                   type=int, help='Minimum width of an image in pixels')
    collage_subparser.add_argument('collageWidth', metavar='CollageWidth',
                                   type=int, help='Width of the collage in pixels')
    collage_subparser.add_argument('collageHeight', metavar='CollageHeight',
                                   type=int, help='Height of collage in pixels')


    args = parser.parse_args()

if __name__ == "__main__":
    main()