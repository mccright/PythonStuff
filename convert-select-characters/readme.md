
### Replace These Unicode symbols with more common and easy-to-deal-with punctuation marks  

Using Unicode variants of common characters may make text more visually pleasing or culturally *accurate*, but for some characters it also makes management and search tasks more challenging due to the characters looking similar to their common counterparts, but failing common search behaviors.  

When copying/harvesting data or source code there is a risk that some characters are not what you expect.  When you save or reuse these inputs in your own work, converting some common Unicode characters to their ASCII counterparts can reduce coding, debugging, testing and risk managment investments.  It can also reduce the potential confusion/frustration of those who use your outputs.  

A parallel issue is associated with hostile use of ```alternate``` characters in look-alike domain names.  See: https://github.com/glaubermagal/evilurl by Glauber Magalhães.  

ToDo: Write a couple scripts to identify and convert the Unicode characters in the table below along with some ASCII look-alikes.  Script inputs: One or more files.  A stream passed along in a pipeline. Script outputs: One or more files or a stream (standard out).  
Example script using replacement (*a tough challenge, better to use a safelist*): [prep_text.py](prep_text.py)  
Example script using replacement with a broader net (*still a bad idea and risk-rich, but sometimes you don't yet know what you are dealing with, but also need to do some safe-enough exploring*): [replace_lookalike_characters.py](replace_lookalike_characters.py)  
Example script using unidecode module (*simple, generally safer, but limited*): [text_2_ascii.py](text_2_ascii.py)  

Replace These Unicode Characters With ASCII Equivalents:  

| Name                                    | From | To    |
| --------------------------------------- | ---- | ----- |
| `NO-BREAK SPACE`                        | `◌`  | ` `   |
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

Thank you https://notabug.org/SETI2261/wiki/src/master/docs/reference/bibles/the-salty-bible.md  

