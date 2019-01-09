import os

class DataConcat:
    """
    Reads and saves the data from the IR camera
    """

    def __init__(self, start_time, end_time, datatype):

        if datatype == 'W' or datatype == 'S':
            print("Starting data concatenation between ", start_time, " and ", end_time)
        else:
            raise TypeError("Please select either 'S' for sensor data or 'W' for weather API data. Exiting...")

        available_files = os.listdir('/Users/paoloruegg/Dropbox/Apps/hackPi/')

        selected_files = []

        for filename in available_files:

            if datatype == 'S':
                time = filename[5:13]
                try:
                    time = int(time)

                    if start_time <= time <= end_time:
                        if filename[0] == 'w':
                            pass
                        else:
                            selected_files.append(filename)

                # Some hidden files...
                except:
                    pass

            elif datatype == 'W':
                time = filename[6:14]

                try:
                    time = int(time)

                    if start_time <= time <= end_time:
                        if filename[0] == 'w':
                            selected_files.append(filename)
                        else:
                            pass

                # Some hidden files...
                except:
                    pass

        with open('/Users/paoloruegg/Dropbox/Apps/hackPi_concatenated/' + datatype + 'data.txt', 'w') as outfile:
            for fname in sorted(selected_files):
                with open('/Users/paoloruegg/Dropbox/Apps/hackPi/' + fname) as infile:
                    for line in infile:
                        outfile.write(line)

        print("Data concatenation completed")

if __name__ == '__main__':

    START_DATE = 18113000
    END_DATE = 18123000

    DataConcat(START_DATE, END_DATE, 'W')
    DataConcat(START_DATE, END_DATE, 'S')

