def is_valid_html(html):
    stack = []

    for match in re.finditer(r'<(/?\w+)>', html):
        tag = match.group(1)

        if tag.startswith('/'):  # Closing tag
            if not stack or stack.pop() != tag[1:]:
                return False
        else:  # Opening tag
            stack.append(tag)

    return not stack

# Example usage:
html = "<html><body><p>Hello</p></body></html>"
assert is_valid_html(html) == True
