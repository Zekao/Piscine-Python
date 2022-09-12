class CsvReader:
    """ A Class that will open, read and parse a CSV file.
        It contains some built-in methods
        @__init__
        @__enter__
        @__exit__
    """
    def __init__(self, filename=None, sep=’,’, header=False, skip_top=0, skip_bottom=0):
    # ... Your code here ...
    def __enter__(...):
    # ... Your code here ...
    def __exit__(...):
    # ... Your code here ...
    def getdata(self):
    """ Retrieves the data/records from skip_top to skip bottom.
    Return:
    nested list (list(list, list, ...)) representing the data.
    """
    # ... Your code here ...
    def getheader(self):
    """ Retrieves the header from csv file.
    Returns:
    list: representing the data (when self.header is True).
    None: (when self.header is False).
    """
    # ... Your code here ...