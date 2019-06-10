
import csv

# ------------------------------------------------------------------------------------------------ #
# CSV.READER(csvfile obj, dialect='excel', **fmtparams)
# Return a reader object which will iterate over lines in the given csvfile
# If csvfile is a file object, it should be opened with newline=''
# with open('TEST_CSV.csv', newline='') as f:
#     spamreader = csv.reader(f, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))


# ------------------------------------------------------------------------------------------------ #
# CSV.WRITER(csvfile obj, dialect='excel', **fmtparams)
# Return a writer object responsible for converting the user’s data into delimited strings
# on the given file-like object. csvfile can be any object with a write() method.
# with open('TEST_CSV_2.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


# with open('TEST_CSV_2.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))


# ------------------------------------------------------------------------------------------------ #
# Reading Examples
# The simplest example of reading a CSV file
# with open('TEST_CSV.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# ------------------------------------------------------------------------------------------------ #
# Reading a file with an alternate format
# with open('TEST_CSV.csv', newline='') as f:
#     reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
#     for row in reader:
#         print(row)


# By default be decoded into unicode using the system default encoding
# To decode a file using a different encoding, use the encoding argument of open
# import csv
# with open('some.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# A slightly more advanced use of the reader — catching and reporting errors
# import csv, sys
# filename = 'some.csv'
# with open(filename, newline='') as f:
#     reader = csv.reader(f)
#     try:
#         for row in reader:
#             print(row)
#     except csv.Error as e:
#         sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


# And while the module doesn’t directly support parsing strings, it can easily be done:
# import csv
# for row in csv.reader(['one,two,three']):
#     print(row)



# ------------------------------------------------------------------------------------------------ #
# Writing Examples

# The corresponding simplest possible writing example is
# with open('TEST_CSV_3.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Knock'] * 2 + ['Whos there?'])


# with open('TEST_CSV_3.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)