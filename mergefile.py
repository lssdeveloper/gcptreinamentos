from fsplit.filesplit import Filesplit

fs = Filesplit()


def merge_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))


path = "C:/Users/Leandro/PycharmProjects/gcptreinamentos/output"

fs.merge(input_dir=path, callback=merge_cb)
