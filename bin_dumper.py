def dump_bin_file(file_path, output_format='hex', readable=False):
    """
    Dumps the contents of a .bin file in a specified format.

    :param file_path: Path to the .bin file.
    :param output_format: Format for output ('hex' or 'binary'). Default is 'hex'.
    :param readable: If True, also outputs the content as readable ASCII characters.
    """
    try:
        with open(file_path, 'rb') as bin_file:
            content = bin_file.read()

            if output_format == 'hex':
                # Print the content in hexadecimal format
                hex_output = ' '.join(f'{byte:02X}' for byte in content)
                print("Hex Dump:")
                print(hex_output)
                
                if readable:
                    # Convert hex to ASCII, filtering out non-printable characters
                    ascii_output = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in content)
                    print("\nReadable ASCII:")
                    print(ascii_output)
            elif output_format == 'binary':
                # Print the content in binary format
                binary_output = ' '.join(f'{byte:08b}' for byte in content)
                print("Binary Dump:")
                print(binary_output)
            else:
                print("Unsupported output format. Please use 'hex' or 'binary'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Use a raw string or double backslashes for the file path
    file_path = r"path/to/file/include/filename.bin"
    dump_bin_file(file_path, output_format='hex', readable=True)
