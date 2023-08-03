from babel.messages.frontend import extract_messages

options = {
    'output_file': 'messages.pot',
    'input_paths': ['.'],
    'mapping_file': None,
    'keywords': None,
    'comment_tags': None,
    'strip_comments': False,
    'sort_output': False,
    'add_comments': False,
}

extract_messages(options)
