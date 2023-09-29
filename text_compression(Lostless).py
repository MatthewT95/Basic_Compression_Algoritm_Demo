import os

uncompressed_text = "" # varible storing uncompressed text
compressed_text = "" # varible storing compressed without string library
compressed_data = "" # varible storing compressed_data
source_filename = "" # varible storing source filename
verbose_mode = False # varible storing setting for verbose mode
compression_mode = "" # varible storing compression mode (compress | decompress)
source_type = "" # varible storing source_type mode (user_input | file)
file_content ="" # varible storing loaded file content
partial_max_size = 8 # max size for substrings to search for
lookback_window_max = 200 # look back window size, must be less then 255
valid_input = False # varible stores weither input was valid
user_input = ""
file_reader = ""

# Ask user if they wish to compress or decompress
valid_input = False
while not valid_input:
    user_input = input("Do you wish to compress(c) or decompress(d)")
    if user_input == "c" or user_input == "C":
        compression_mode = "compress"
        valid_input = True
    elif user_input == "d" or user_input == "D":
        compression_mode = "decompress"
        valid_input = True
    else:
        print("Invalid entry. Enter c to compress, d to decompress.")
#print("compression_mode:" + compression_mode)
# Ask user if they wish to input text or load a file
valid_input = False
while not valid_input:
    user_input = input("Do you wish to use user_input(u) or file(f)")
    if user_input == "u" or user_input == "U":
        source_type = "user_input"
        valid_input = True
    elif user_input == "f" or user_input == "F":
        source_type = "file"
        valid_input = True
    else:
        print("Invalid entry. Enter u for user input, f for file.")
#print("source_type:" + source_type)

# ask user if they want verbose mode and set setting
valid_input = False
while not valid_input:
    user_input = input("Do you wish to have verbose mode on y/n.")
    if user_input == "y" or user_input == "Y":
        verbose_mode = True
        valid_input = True
    elif user_input == "n" or user_input == "N":
        verbose_mode = False
        valid_input = True
    else:
        print("Invalid entry. Enter y for on, n for off.")
#print("verbose_mode:" + str(verbose_mode))

# if source_type is user_input
if source_type == "user_input":
    # if compression_mode is compress
    if compression_mode == "compress":
        # gets user input and stores it in uncompressed_text
        uncompressed_text = input("Enter text to compress: ")
        #print("compress: " + uncompressed_text)
    # if compression_mode is decompress
    else:
        # gets user input and stores it in compressed_text
        compressed_text = input("Enter text to decompress: ")
        #print("decompress: " + compressed_text)
# if source_type is file
else:
    # ask user for source file name and store in source_filename
    source_filename = input("Please enter source filename: ")
    # check if file exists at source_filename
    if os.path.isfile(source_filename):
        #print("file exists.")
        # load file using source_filename and store content in file_contents
        file_reader = open(source_filename, "r")
        file_content = file_reader.read()
        # if compression_mode is compress
        if compression_mode == "compress":
            # set uncompressed_text to file_contents
            uncompressed_text = file_content
            #print("compress: " + uncompressed_text)
        # if compression_mode is decompress
        else:
            # set compressed_data to file_contents
            compressed_text = file_content
            #print("decompress: " + compressed_text)
    # if file dose not exist
    else:
        # print error message
        print("Source file dose not exist.")
        # exit program
        exit()

# if compression mode is compress
if compression_mode == "compress":
    postion = 0 # current postion in uncompressed text
    lookback_window = "" # current look back window
    compression_buffer = "" # compression_buffer
    lookback_pointer = 0 # number of steps back to partial begining
    partial_size = 0 # size of the partial string found
    # while loop until end of uncompressed text
        # update loop back window
        # loop over all substrings at postion with length starting at partial_max_size
            # search for string in look back window
            # if partial found
                # calculate look_back_pointer
                # update partial_size
                # append byte repressing lookbackpointer to compression_buffer
                # append btye repressing partial_size to compression_buffer
            # incremeant postion by partial_size
        # if partial not found
            # append byte representing zero pointer
            # append charter at postion to compression_buffer
            # incremeant postion by 1 to compression_buffer
    
    # set compressed_text to compressed_buffer

