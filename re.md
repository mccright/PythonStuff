## Python `re` Module: Cheatsheet & Examples
(*copied from https://github.com/blutterfly/python/blob/main/docs/examples/re.md on 2025-10-21 - thank you "`Butterfly`"*)

The `re` module in Python provides support for regular expressions (regex), allowing you to search, match, and manipulate text efficiently.

---

## **1. Basic Functions in `re` Module**

| Function | Description |
|----------|-------------|
| `re.match(pattern, string)` | Matches pattern at the **beginning** of the string |
| `re.search(pattern, string)` | Searches **anywhere** in the string |
| `re.findall(pattern, string)` | Returns all **non-overlapping** matches as a list |
| `re.finditer(pattern, string)` | Returns an iterator yielding `MatchObject` instances |
| `re.split(pattern, string)` | Splits the string by occurrences of the pattern |
| `re.sub(pattern, repl, string)` | Replaces occurrences of pattern with `repl` |
| `re.subn(pattern, repl, string)` | Like `re.sub()`, but returns a tuple with count of substitutions |
| `re.compile(pattern)` | Compiles a regex pattern for reuse |

---

## **2. Meta Characters & Their Meaning**

| Meta Character | Meaning | Example |
|---------------|---------|---------|
| `.` | Any character except newline | `r"a.b"` matches `"acb"`, `"axb"` |
| `^` | Start of string | `r"^hello"` matches `"hello world"` |
| `$` | End of string | `r"world$"` matches `"hello world"` |
| `*` | 0 or more repetitions | `r"ab*"` matches `"a"`, `"ab"`, `"abb"` |
| `+` | 1 or more repetitions | `r"ab+"` matches `"ab"`, `"abb"`, but not `"a"` |
| `?` | 0 or 1 occurrence | `r"colou?r"` matches `"color"` and `"colour"` |
| `{n}` | Exactly n times | `r"\d{3}"` matches `"123"` but not `"12"` |
| `{n,}` | n or more times | `r"\d{2,}"` matches `"12"`, `"123"`, `"1234"` |
| `{n,m}` | Between n and m times | `r"\d{2,4}"` matches `"12"`, `"123"`, `"1234"` but not `"1"` |
| `\` | Escape special characters | `r"\."` matches a literal `"."` |
| `[]` | Character set | `r"[aeiou]"` matches any vowel |
| `[^]` | Negated character set | `r"[^aeiou]"` matches any **non-vowel** |
| `\|` | OR (alternation) | `r"yes\|no"` matches `"yes"` or `"no"` |
| `()` | Grouping | `r"(abc)+"` matches `"abc"`, `"abcabc"` |

---

## **3. Special Sequences**

| Pattern | Meaning | Example |
|---------|---------|---------|
| `\d` | Digit (`0-9`) | `r"\d+"` matches `"123"` |
| `\D` | Non-digit | `r"\D+"` matches `"abc"` |
| `\w` | Word character (`a-z, A-Z, 0-9, _`) | `r"\w+"` matches `"hello_123"` |
| `\W` | Non-word character | `r"\W+"` matches `"#@"` |
| `\s` | Whitespace (`space, tab, newline`) | `r"\s+"` matches `" "` |
| `\S` | Non-whitespace | `r"\S+"` matches `"Hello"` |
| `\b` | Word boundary | `r"\bcat\b"` matches `"cat"`, but not `"scatter"` |
| `\B` | Not a word boundary | `r"\Bcat\B"` matches `"scatter"` |

---

## **4. Using `re.match()`**

- **Matches only at the beginning of the string**

```python
import re
result = re.match(r"\d+", "123abc")
print(result.group())  # Output: 123
```

```python
result = re.match(r"\d+", "abc123")
print(result)  # Output: None
```

---

## **5. Using `re.search()`**

- **Finds first occurrence anywhere in the string**

```python
import re
result = re.search(r"\d+", "abc123def456")
print(result.group())  # Output: 123
```

---

## **6. Using `re.findall()`**

- **Finds all occurrences of the pattern**

```python
import re
result = re.findall(r"\d+", "abc123def456")
print(result)  # Output: ['123', '456']
```

---

## **7. Using `re.finditer()`**

- **Returns an iterator of match objects**

```python
import re
for match in re.finditer(r"\d+", "abc123def456"):
    print(match.group())  # Output: 123, 456
```

---

## **8. Using `re.split()`**

```python
import re
result = re.split(r"\s+", "Hello   World  Python")
print(result)  # Output: ['Hello', 'World', 'Python']
```

---

## **9. Using `re.sub()`**

```python
import re
result = re.sub(r"\d+", "X", "abc123def456")
print(result)  # Output: abcXdefX
```

---

## **10. Using `re.compile()`**

- **Pre-compiling regex patterns for better performance**

```python
import re
pattern = re.compile(r"\d+")
result = pattern.findall("abc123def456")
print(result)  # Output: ['123', '456']
```

---

## **11. Greedy vs. Non-Greedy Matching**

| Type | Pattern | Example | Matches |
|------|---------|---------|---------|
| **Greedy** | `r"<.*>"` | `<b>hello</b>` | `<b>hello</b>` |
| **Non-Greedy** | `r"<.*?>"` | `<b>hello</b>` | `<b>` |

```python
import re
text = "<b>hello</b>"
print(re.findall(r"<.*>", text))  # Output: ['<b>hello</b>']
print(re.findall(r"<.*?>", text)) # Output: ['<b>', '</b>']
```

---

## **12. Named Groups in `re`**

```python
import re
result = re.search(r"(?P<first>\w+) (?P<last>\w+)", "John Doe")
print(result.group("first"))  # Output: John
print(result.group("last"))   # Output: Doe
```

---

## **13. Lookaheads & Lookbehinds**

| Type | Pattern | Example | Matches |
|------|---------|---------|---------|
| **Positive Lookahead** | `r"foo(?=bar)"` | `"foobar foo123"` | `"foo"` |
| **Negative Lookahead** | `r"foo(?!bar)"` | `"foobar foo123"` | `"foo"` |
| **Positive Lookbehind** | `r"(?<=\$)\d+"` | `"$100 €200"` | `"100"` |
| **Negative Lookbehind** | `r"(?<!\$)\d+"` | `"$100 €200"` | `"200"` |

```python
import re
print(re.findall(r"foo(?=bar)", "foobar foo123"))  # Output: ['foo']
print(re.findall(r"(?<=\$)\d+", "$100 €200"))  # Output: ['100']
```

---

## **14. Case-Insensitive Matching**

```python
import re
result = re.search(r"hello", "HELLO", re.IGNORECASE)
print(result.group())  # Output: HELLO
```

---

## **15. Multi-line & Dotall Mode**

```python
import re
text = "First line\nSecond line"
print(re.findall(r"^Second", text, re.MULTILINE))  # Output: ['Second']
print(re.findall(r"First.*Second", text, re.DOTALL))  # Output: ['First line\nSecond']
```

---

This cheatsheet should cover most of what you need to work with regular expressions in Python efficiently! 🚀 Let me know if you need more advanced examples.

