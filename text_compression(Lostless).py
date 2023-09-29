uncompressed_text = "" # varible storing uncompressed text
compressed_text = "" # varible storing compressed without string library
substrings_and_frequencies = {} # varible storing list of substrings and frequencies in uncompressed text
# varible storing string library
# varible storing serialized string library
compressed_data = "" # varible storing compressed_data
source_filename = "" # varible storing source filename
destination_filename = "" # varible storing destination filename
# varible storing setting for verbose mode
# varible storing compression mode (compress | decompress)
# varible storing source_type mode (user_input | file)
file_content ="" # varible storing loaded file content
max_substring_size = 8 # max size for substrings to search for

# Ask user if they wish to compress or decompress
# Ask user if they wish to input text or load a file
# ask user if they want verbose mode and set setting

# if source_type is user_input
    # if compression_mode is compress
        # gets user input and stores it in uncompressed_text
    # if compression_mode is decompress
        # gets user input and stores it in compressed_data
# if source_type is file
    # ask user for source file name and store in source_filename
    # ask user for destination file name and store in destination_filename
    # check if file exists at source_filename
        # load file using source_filename and store content in file_contents
        # if compression_mode is compress
            # set uncompressed_text to file_contents
        # if compression_mode is decompress
            # set compressed_data to file_contents
    # if file dose not exist
        # print error message
        # exit program

# if compression mode is compress
    # get all substrings
    # loop over all substring lenghts starting at max_substring_size
        # loop over uncompressed_text starting from beginning to end - substring size
            # stores current substring at given postion
            # if substring is already in list
                # increament frequency by 1
            # if not present
                # add to list with value of 1
    
    # if verbose mode is true
        # print all substrings with frequencies
    

