class CsvReader:
    """ A Class that will open, read and parse a CSV file.
        It contains some built-in methods
        @__init__
            - filename: the name of the file to open
            - sep: the separator between values
            - header: a boolean indicating if the file contains a header
            - skip_top: the number of lines to skip at the top of the file
            - skip_bottom: the number of lines to skip at the bottom of the file
            - data: a list of lists containing the data of the file
        @__enter__
        @__exit__
            - Close the file
    """
    def check_file(self):

        for value in self.data:
            if len(value) != len(self.header):
                raise ValueError("The number of columns in the header and the data do not match")
    
    def __init__(self, filename=None, sep=’,’, header=False, skip_top=0, skip_bottom=0):
        check_file(self)
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        try:
            with open(self.filename, 'r') as file:
                self.data = [line.strip().split(self.sep) for line in file]
        except Exception as e:
            print('Error: unable to open file ' + self.filename + ' ' + str(e)) 
        if self.header:
            getheader(self)
        if self.skip_top:
            self.data = self.data[self.skip_top:]
        if self.skip_bottom:
            self.data = self.data[:-self.skip_bottom]
    
    def __enter__(...):
    # ... Your code here ...
    def __exit__(...):
    # ... Your code here ...
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        data = [
            []
        ]
    # ... Your code here ...
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
    if self.header:
        return self.data[0]
    return None
    # ... Your code here ...