import argparse, os

def main(args):
    f  = open(args.outFile, "w")
    for filename in os.listdir(args.data_dir):
        read_in = open(args.data_dir + filename, 'r')
        f.write("----------------------------------------------------\n")
        f.write(filename + "\n")
        f.write("----------------------------------------------------\n")
        f.write(read_in.read())
        f.write("\n")
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Combine all files into one')
    parser.add_argument('-d', dest="data_dir",required=True,
                        help='Directory of all files you want to combine')
    parser.add_argument('-o', dest="outFile",required=True,
            help='Output Filename')
    args = parser.parse_args()
    main(args)
