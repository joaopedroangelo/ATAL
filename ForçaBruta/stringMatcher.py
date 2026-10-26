text = "This is a simple example to demonstrate"
pattern = "mons"

def stringMatcher(text, pattern):
    """
    A simple brute-force string matching algorithm that searches for occurrences of a pattern
    in a given text.

    Parameters:
    text (str): The text in which to search for the pattern.
    pattern (str): The pattern to search for in the text.

    Returns:
    list: A list of starting indices where the pattern is found in the text.
    """
    matches = []
    text_length = len(text)
    pattern_length = len(pattern)

    # Loop through the text to find the pattern
    for i in range(0, text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            matches.append(i)
    return matches


# Example usage
result = stringMatcher(text, pattern)
if result:
    print(f"Pattern found at indices: {result}")
else:
    print("Pattern not found in the text.")
