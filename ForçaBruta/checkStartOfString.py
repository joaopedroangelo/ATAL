string = "Hello, world!"
prefix = "Hello"

def checkStartOfString(string, prefix):
    """
    Check if the given string starts with the specified prefix.

    Parameters:
    string (str): The string to check.
    prefix (str): The prefix to look for.

    Returns:
    bool: True if the string starts with the prefix, False otherwise.
    """
    result = False
    for i in range(0, len(prefix)):
        if i >= len(string) or string[i] != prefix[i]:
            result = False
            break
        result = True
    return result

print(checkStartOfString(string, prefix))
