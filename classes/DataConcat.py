import os

class DataConcat:
    """
    Reads and saves the data from the IR camera
    """

    def __init__(self, start_time, end_time):

        self.data_path = '/Users/paoloruegg/Dropbox/Apps/hackPi/'
        self.start_time = int(start_time.replace('_', ''))
        self.end_time = int(end_time.replace('_', ''))

        available_slices = os.listdir('/Users/paoloruegg/Dropbox/Apps/hackPi/')

        selected_files = []
        for slice in available_slices:

            time = slice[5:13]
            try:
                time = int(time)

                if self.start_time <= time and time <= self.end_time:
                    selected_files.append(slice)

            # Some hidden files...
            except:
                pass


        with open('../data/data.txt', 'w') as outfile:
            for fname in sorted(selected_files):
                with open('/Users/paoloruegg/Dropbox/Apps/hackPi/' + fname) as infile:
                    for line in infile:
                        outfile.write(line)

if __name__ == '__main__':

    DataConcat('181127_11','181202_08')


