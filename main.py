import argparse
from typing import List

def scrape_image_urls(api:str, url:List[str]):

    # scrape

    # process
    pass

def create_collage():
    pass


def save_images():
    pass

def save_to_location():
    pass


def parse_arguments():
    # top level parser
    parser = argparse.ArgumentParser(description='Processes pinterest images')
    parser.add_argument('url', type=str, action='append', help='Pinterest Board URL')  # can scrape multiple boards
    parser.add_argument('api', type=str, help='Pinterest API Key')
    parser.add_argument('loc', metavar='saveLocation', help='Location to save parsed results')
    subparsers = parser.add_subparsers(title='mode', dest='mode', required=True)

    # subparsers
    subparsers.add_parser('save', help='Save pins as images in a folder')

    collage_subparser = subparsers.add_parser('collage', help='Create collage of pins')
    collage_subparser.add_argument('minHeight', type=int, help='Minimum width of an image in pixels')
    collage_subparser.add_argument('collageWidth', type=int, help='Width of the collage in pixels')
    collage_subparser.add_argument('collageHeight', type=int, help='Height of collage in pixels')

    return parser.parse_args()

def main():
    # parse aguments
    args = parse_arguments()

    # scrape images
    imageURLs = scrape_image_urls()

    # transform images
    if args.collage:
        result = create_collage()
    elif args.save:
        result = save_images()
    else:
        pass

    save_to_location(result)



    # save result


if __name__ == "__main__":
    main()