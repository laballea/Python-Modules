import sys


class CsvReader():
    def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
        try:
            self.file_obj = open(filename, "r")
            self.sep = sep
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
            self.header = header

        except FileNotFoundError as inst:
            print(inst)
            sys.exit()

    def __enter__(self):
        recordsCount = len(str(self.file_obj.readline()).split(self.sep))
        for line in self.file_obj.readlines():
            splitedLine = str(line[:-1]).split(self.sep)
            if (any(not el for el in splitedLine)):
                return None
            if (recordsCount != len(splitedLine)):
                return None
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.file_obj.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        result = []
        self.file_obj.seek(0)
        for idx, line in enumerate(self.file_obj.readlines()):
            if (self.skip_bottom <= idx >= self.skip_top and line[:-1]):
                result.append(str(line[:-1]).split(self.sep))
        return result

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if (not self.header):
            return None
        else:
            self.file_obj.seek(0)
            return str(self.file_obj.readline()[:-1]).split(self.sep)
        # ... Your code here ...


with CsvReader("good.csv") as file:
    if file is None:
        print("File is corrupted !")
    else:
        data = file.getdata()
        print(data)
        header = file.getheader()
        print(header)

