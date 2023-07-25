#!/usr/bin/python3

def valid_utf8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: A list of integers representing bytes of data (8 least significant bits).
    :type data: list[int]
    :return: True if data is a valid UTF-8 encoding, else return False.
    :rtype: bool

    A character in UTF-8 can be 1 to 4 bytes long. The data set can contain multiple characters.
    Each integer in the data list represents 1 byte of data, so we only consider the 8 least significant bits of each integer.
    """

    # Helper function to check if a byte starts with "10"
    def is_valid_following_byte(byte):
        """
        Check if the given byte starts with "10".

        :param byte: The byte to check.
        :type byte: int
        :return: True if the byte starts with "10", else return False.
        :rtype: bool
        """
        return (byte & 0b11000000) == 0b10000000

    num_bytes_to_follow = 0

    for byte in data:
        # Check the number of bytes to follow for the current character
        if num_bytes_to_follow == 0:
            if byte & 0b10000000 == 0:
                # One-byte character
                num_bytes_to_follow = 0
            elif byte & 0b11100000 == 0b11000000:
                # Two-byte character
                num_bytes_to_follow = 1
            elif byte & 0b11110000 == 0b11100000:
                # Three-byte character
                num_bytes_to_follow = 2
            elif byte & 0b11111000 == 0b11110000:
                # Four-byte character
                num_bytes_to_follow = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check if the following bytes start with "10"
            if not is_valid_following_byte(byte):
                return False

            num_bytes_to_follow -= 1

    # If there are remaining bytes to follow, it means the data is invalid
    return num_bytes_to_follow == 0
