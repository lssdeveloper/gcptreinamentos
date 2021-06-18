from fsplit.filesplit import Filesplit

fs = Filesplit()


def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))


# fs.split(file="/path/to/source/file", split_size=900000, output_dir="/path/to/output/dir", callback=split_cb)

path_file = "C:/Users/Leandro/PycharmProjects/gcptreinamentos/source/rais_to_bq.csv"
path_output = "C:/Users/Leandro/PycharmProjects/gcptreinamentos/output"
fs.split(file=path_file, split_size=2000000,
         output_dir=path_output, callback=split_cb)


