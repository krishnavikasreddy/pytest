
"""
We download and setup the data that are needed for our requirements
"""
from __future__ import print_function

import os
import sys
import urllib
import tarfile


class SetupData(object):
    """
    SetupData downloads the data and makes it ready for use
    """
    def __init__(self, url, data_root):
        self.url = url
        self.data_root = data_root
        self.last_download_progress = 0

    def __download_progress_hook(self, count, block_size, total_size):
        """
        A hook to report the total progress of the download. This is mostly
        for slow internet connections.Reports every 5% change in download
        """
        percent = int(count * block_size * 100 / total_size)

        if self.last_download_progress != percent:
            if percent % 5 == 0:
                sys.stdout.write("%s%%" % percent)
                sys.stdout.flush()
            else:
                sys.stdout.write(".")
                sys.stdout.flush()
        self.last_download_progress = percent

    def download_file(self, filename, force=False):
        """
        Download the file if the file is not present
        """
        dest_filename = os.path.join(self.data_root, filename)
        if force or not os.path.exists(dest_filename):
            print("Attemptig to download %s", filename)
            filename, _ = urllib.urlretrieve(self.url + filename,
                                             dest_filename,
                                             reporthook=self.
                                             __download_progress_hook)
            print("Download complete")
            print("%s of bytes of data downloaded"
                  % os.stat(dest_filename).st_size)

    def unpack_tar_files(self, filename):
        """
        To unpack all the files into the folder
        """
        print("Extracting files")
        path = os.path.join(self.data_root, filename)
        print(os.path.exists(path))
        print(os.path.splitext(path))
        # tarFileRef = tarfile.open(path, "r")
        # tarFileRef.extractall()
        # tarFileRef.close()


if __name__ == "__main__":
    SETUPDATA = SetupData("http://commondatastorage.googleapis.\
    com/books1000/", ".")
    # SETUPDATA.download_file("notMNIST_large.tar.gz",
    # True)
    SETUPDATA.unpack_tar_files("notMNIST_large.tar.gz")
