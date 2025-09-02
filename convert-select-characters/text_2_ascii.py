import unidecode
import sys


def toascii(text: str):
    ascii_lines: str = ""
    for a_line in text:
        ascii_line = unidecode.unidecode(a_line)
        ascii_lines = ascii_lines + ascii_line
    return ascii_lines


if __name__ == "__main__":
    lines: str = ""
    try:
        line: str = sys.stdin.readline()
        while line:
            # append line to lines
            lines = lines + line
            # re-fill 'line'
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    lines = toascii(lines)
    print(f"cleaned input =\r\n{lines}")

