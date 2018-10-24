def _indent(parameter):
    parameter = parameter.strip()
    if parameter.find('target_link_libraries') >= 0:
        return parameter
    if parameter == 'PUBLIC' or parameter == 'PRIVATE' or parameter == 'INTERFACE':
        return '  ' + parameter
    return '    ' + parameter

def _split_target_link_libraries(line):
    if line.endswith(')'):
        line = line[0:len(line) - 1]
    tokens = line.split()
    tokens = [_indent(t) for t in tokens]
    tokens.append(')')
    return tokens

def _split_long_line(line):
    if 'target_link_libraries' in line:
        return _split_target_link_libraries(line)
    return line

def run(file_text):
    lines = file_text.splitlines()
    processed_lines = list()
    for line in lines:
        if len(line) <= 80:
            processed_lines.append(line)
        else:
            processed_lines += _split_long_line(line)
    processed_text = '\n'.join(processed_lines)
    return processed_text
