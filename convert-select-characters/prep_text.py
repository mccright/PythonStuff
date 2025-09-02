import sys

"""
This function began with the pypdf documentation:  
https://pypdf.readthedocs.io/en/stable/user/post-processing-in-text-extraction.html#ligature-replacement
This type of character replacing is highly context specific.
This code is not meant to be immediately reusable for other contexts, 
only to support my use case and to act as a model to be morphed for 
other contexts.
Here are the names of some of the targeted characters:
| Name                                    | From | To    |
| --------------------------------------- | ---- | ----- |
| `NON-BREAKING SPACE`                    | `◌`  | ` `   |
| `LEFT SINGLE QUOTATION MARK`            | `‘`  | `'`   |
| `RIGHT SINGLE QUOTATION MARK`           | `’`  | `'`   |
| `SINGLE LOW-9 QUOTATION MARK`           | `‚`  | `,`   |
| `SINGLE HIGH-REVERSED-9 QUOTATION MARK` | `‛`  | `'`   |
| `LEFT DOUBLE QUOTATION MARK`            | `“`  | `"`   |
| `RIGHT DOUBLE QUOTATION MARK`           | `”`  | `"`   |
| `DOUBLE LOW-9 QUOTATION MARK`           | `„`  | `"`   |
| `DOUBLE HIGH-REVERSED-9 QUOTATION MARK` | `‟`  | `"`   |
| `HYPHEN`                                | `‐`  | `-`   |
| `NON-BREAKING HYPHEN`                   | `‑`  | `-`   |
| `EN DASH`                               | `–`  | `-`   |
| `EM DASH`                               | `—`  | `-`   |
| `FIGURE DASH`                           | `‒`  | `-`   |
| `HORIZONTAL BAR`                        | `―`  | `-`   |
| `ONE DOT LEADER`                        | `․`  | `.`   |
| `TWO DOT LEADER`                        | `‥`  | `..`  |
| `HORIZONTAL ELLIPSIS`                   | `…`  | `...` |
| `DOUBLE EXCLAMATION MARK`               | `‼`  | `!!`  |
| `DOUBLE QUESTION MARK`                  | `⁇`  | `??`  |
| `FRACTION SLASH`                        | `⁄`  | `/`   |
| `DIVISION SLASH`                        | `∕`  | `/`   |
| `WAVE DASH`                             | `〜` | `~`   |
| `FULLWIDTH TILDE`                       | `～` | `~`   |
| `FULLWIDTH LEFT PARENTHESIS`            | `（` | ` (`  |
| `FULLWIDTH RIGHT PARENTHESIS`           | `）` | `) `  |
| `FULLWIDTH LEFT SQUARE BRACKET`         | `［` | ` [`  |
| `FULLWIDTH RIGHT SQUARE BRACKET`        | `］` | `] `  |
| `FULLWIDTH LESS-THAN SIGN`              | `＜` | `<`   |
| `FULLWIDTH GREATER-THAN SIGN`           | `＞` | `>`   |
"""
def replace_problematic_characters(text: str) -> str:
    prob_chars = {
        "◌": " ",
        "‘": "'",
        "’": "'",
        "‚": ",",
        "‛": "'",
        "“": "\"",
        "”": "\"",
        "„": "\"",
        "‟": "\"",
        "‐": "-",
        "­": "-",
        "‑": "-",
        "–": "-",
        "—": "-",
        "‒": "-",
        "―": "-",
        "․": ".",
        "‥": "..",
        "…": "...",
        "‼": "!!",
        "⁇": "??",
        "⁄": "/",
        "∕": "/",
        "〜": "~",
        "～": "~",
        "（": " (",
        "）": ") ",
        "［": " [",
        "］": "] ",
        "＜": "<",
        "＞": ">",
        "Ö": "O",
        "Ü": "U",
        "À": "A", 
        "Á": "A", 
        "Â": "A", 
        "Ã": "A", 
        "Ä": "A", 
        "Å": "A", 
        "à": "a",
        "á": "a",
        "â": "a",
        "ã": "a",
        "ä": "a",
        "å": "a",
        "È": "E",
        "É": "E",
        "Ê": "E",
        "Ë": "E",
        "è": "e",
        "é": "e",
        "ê": "e",
        "ë": "e",
        "Ì": "I",
        "Í": "I",
        "Î": "I",
        "Ï": "I",
        "ì": "i",
        "í": "i",
        "î": "i",
        "ï": "i",
        "Ꜳ": "AA",
        "Æ": "AE",
        "ꜳ": "aa",
        "»": ">>",
        "«": "<<",
        "✓": "(check)",
        "ﬀ": "ff",
        "ø": "o",
        "Ø": "O",
        "Ò": "O",
        "Ó": "O",
        "Ô": "O",
        "Õ": "O",
        "Ö": "O",
        "ò": "o",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ö": "o",
        "Ù": "U",
        "Ú": "U",
        "Û": "U",
        "Ü": "U",
        "ù": "u",
        "ú": "u",
        "û": "u",
        "ü": "u",
        "Ý": "Y",
        "Ÿ": "Y",
        "ý": "y",
        "ÿ": "y",
        "Š": "S",
        "š": "s",
        "ð": "(eth)",
        "Ç": "C",
        "ç": "c",
        "ñ": "n",
        "Ñ": "N",
        "Ž": "Z",
        "ž": "z",
        "þ": "p",
        "Þ": "p",
        "ﬁ": "fi",
        "ﬂ": "fl",
        "ﬃ": "ffi",
        "ﬄ": "ffl",
        "ﬅ": "ft",
        "Œ": "OE",
        "œ": "oe",
        "ﬆ": "st",
        "ß": "ss",
        "⻖": "(Unicode U+2ED6, looks like B)",
        "阝": "(Unicode U+961D, looks like B)",
        "ഭ": "(Malayalam script Consonant bha Unicode U+0D2D, looks like C)",        
    }
    for search, replace in prob_chars.items():
        text = text.replace(search, replace)
    return text


# Read lines in a way that is ready for pipelines
# Though unsophisticated, this seems like a common
# and useful idiom.
# Under many circumstances input/output sanity checking
# or other *safety* measures will be needed in that while loop.
# as my exception handling isn't automation-friendly.
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
    lines = replace_problematic_characters(lines)
    print(f"cleaned input =\r\n{lines}")

