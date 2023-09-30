import os
from time import sleep
from traceback import print_tb

uncompressed_text = "" # varible storing uncompressed text
compressed_text = "" # varible storing compressed without string library
compressed_data = "" # varible storing compressed_data
source_filename = "" # varible storing source filename
verbose_mode = False # varible storing setting for verbose mode
compression_mode = "" # varible storing compression mode (compress | decompress)
source_type = "" # varible storing source_type mode (user_input | file)
file_content ="" # varible storing loaded file content
PARTIAL_MAX_SIZE = 7 # max size for substrings to search for. Must be less then 16
BITS_FOR_SIZE_PORTION = 3
lookback_window_max = 900 # look back window size, must be less then 255
valid_input = False # varible stores weither input was valid
user_input = ""
file_reader = ""
MAX_LOOKBACK_POINTER = 1000

def string_to_numbers(input_string):
    output = ""
    for i in range(0,len(input_string)):
        output=output+str(ord(input_string[i])) + " "

    return (output)

def compressed_string_breakdown(input_string):
    output = ""
    for i in range(0,len(input_string)):
        size = ord(input_string[i]) % 2**BITS_FOR_SIZE_PORTION
        pointer = (ord(input_string[i])-size) / 2**BITS_FOR_SIZE_PORTION
        output=output+"({},{}) ".format(str(pointer),str(size))

    return (output)
def utf8len(s):
    return len(s.encode('utf-8'))

if PARTIAL_MAX_SIZE > 2**BITS_FOR_SIZE_PORTION:
    print("PARTIAL_MAX_SIZE is too large for BIT_FOR_PORTION provided")
    exit()

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
            # print("compress: " + uncompressed_text)
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
    while postion < len(uncompressed_text):
        # update loop back window
        if postion < lookback_window_max:
            lookback_window = uncompressed_text[0:postion]
        else:
            lookback_window = uncompressed_text[(postion-lookback_window_max):postion]
        # reverses window so partial postions postions are relative to current postion
        lookback_window=lookback_window[::-1]
        partial_found_in_lookback = False
        # loop over all substrings at postion with length starting at partial_max_size
        for sustring_size in range(min(PARTIAL_MAX_SIZE,len(uncompressed_text)-postion),0,-1):
            # search for string in look back window
            partial_postion_in_lookback_window = lookback_window.find(uncompressed_text[postion+sustring_size:postion:-1])
            # if partial found
            if partial_postion_in_lookback_window != -1:
                partial_found_in_lookback = True
                # calculate look_back_pointer
                lookback_pointer = partial_postion_in_lookback_window + partial_size + 1
                # update partial_size
                partial_size = sustring_size
                # combined pointer and size
                serialized_pointer_size = chr((lookback_pointer * 2**BITS_FOR_SIZE_PORTION) + partial_size)
                # # append byte repressing lookbackpointer to compression_buffer
                # compression_buffer = compression_buffer + chr(lookback_pointer)
                # # append btye repressing partial_size to compression_buffer
                # compression_buffer = compression_buffer + chr(partial_size)
                # append serialized_pointer_size to compressed_buffer
                compression_buffer=compression_buffer+serialized_pointer_size
                # incremeant postion by partial_size
                postion=postion+partial_size
        # if partial not found
        if not partial_found_in_lookback:
            # combined pointer and size
            serialized_pointer_size = chr(((MAX_LOOKBACK_POINTER+ord(uncompressed_text[postion])) * 2**BITS_FOR_SIZE_PORTION) + 0)
            # # append byte representing zero pointer
            # compression_buffer = compression_buffer + chr(255)
            # # append charter at postion to compression_buffer
            # compression_buffer = compression_buffer + uncompressed_text[postion]
            # incremeant postion by 1 to compression_buffer
            # append serialized_pointer_size to compressed_buffer
            compression_buffer=compression_buffer+serialized_pointer_size
            postion=postion+1
    # set compressed_text to compressed_buffer
    compressed_text = compression_buffer
    print(compressed_string_breakdown(compressed_text))
    print(utf8len(compressed_text),utf8len(uncompressed_text))
