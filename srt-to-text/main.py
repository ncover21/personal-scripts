import argparse, re
from ytcc.download import Download

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getVideoId(url):
    return re.split(r'\?v=', url)[1]

def main(args):
    if args.videoUrl is not None:
        video_id = getVideoId(args.videoUrl)
        print(bcolors.OKGREEN +
            "Scraping Captions from url with id: {}...".format(video_id) + bcolors.ENDC)
        download = Download()
        captions = download.get_captions(video_id)
        if captions is not None:
            print(bcolors.OKBLUE + "Done!" + bcolors.ENDC)
        else:
            print(bcolors.FAIL +
                "\tError Occured: Unable to download captions" + bcolors.ENDC)
            exit()
    if captions is not None:
        if args.outFile is not None:
            f = open(args.outFile, "w")
        else:
            f = open("youtube-{}.txt".format(video_id), "w")

        wordNum = 0
        for word in re.split('\s+', captions):
            if wordNum == args.lineLimit:
                f.write('\n')
                wordNum = 0
            f.write("{} ".format(word))
            wordNum+=1
        f.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Conversion of srt files to text')
    parser.add_argument('-v', dest="videoUrl",required=False,
                        help='Youtube video url')
    parser.add_argument('-o', dest="outFile",required=False,
                        help='Output Filename')
    parser.add_argument('-l', dest="lineLimit",required=False,
                        help='Character Line limit', default=20)
    args = parser.parse_args()
    main(args)
