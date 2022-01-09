"""
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""
import unicodedata
import string

valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
"""
str: A string containing all of the valid filename characters.
"""
char_limit = 255
"""
int: The maximumn number of characters allowed for a filename in Windows (255).
"""


def _replace_spaces_with_underscores(filename, replace=' '):
    """
    Replace all of the spaces (` `) in a filename with underscores (`_`).

    Parameters
    ----------
    filename : str
        A string that needs the spaces (` `) converted into underscores (`_`).
    replace : str
        The string character to replace in the filename with `_`. By default, this will be spaces.

    Returns
    -------
    str
        By default, a copy of `filename` without any spaces. It will only have underscores.
        Setting the `replace` parameter will change what character is removed.
    """
    for r in replace:
        filename = filename.replace(r, '_')
    return filename


def _preserve_valid_ascii_character(filename):
    """
    Return a filename string that contains only valid ASCII characters.

    Parameters
    ----------
    filename : str
        A string that needs only valid ASCII characters.

    Returns
    -------
    str
        A copy of `filename` with only valid ASCII characters.
    """
    return unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()


def _preserve_whitelisted_characters(cleaned_filename, whitelist=valid_filename_chars):
    """
    Scrape through a string and remove all characters that are not valid for a filename.

    Print a message warning if a string is longer than 256 characters. If a string is longer than 256 characters,
    return the first 256 characters from the original string.

    Parameters
    ----------
    cleaned_filename : str
        A string that I want to turn into a filename.
    whitelist : str
        A string of valid characters I can use in a filename.

    Returns
    -------
    str
        A string that can safely serve as a Windows system filename.
    """
    cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename) > char_limit:
        print(f"Warning, filename truncated because it was over {char_limit} characters.")
        print("Filename may no longer be unique.")
    return cleaned_filename[:char_limit]


def clean_filename(filename, whitelist=valid_filename_chars, replace=' '):
    """
    Return a copy of a string that can safely be used as a filename.

    Parameters
    ----------
    filename : str
        The original string I want to use as the base for the filename.
    whitelist : str
        A string of valid characters I can use in a filename.
    replace : str
        The string character to replace in the filename with `_`. By default, this will be spaces.

    Returns
    -------
    str
        A string that can safely serve as a Windows system filename
    """
    dirty_filename = _replace_spaces_with_underscores(filename, replace)
    cleaner_filename = _preserve_valid_ascii_character(dirty_filename)
    return _preserve_whitelisted_characters(cleaner_filename, whitelist)
