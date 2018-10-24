import re

# TODO handle split scopes: PUBLIC ... PRIVATE ... PUBLIC ...
def _gather_dependencies(scope, parameters):
    if scope in parameters:
        scope_index = parameters.index(scope)
        end = scope_index + 1
        while end < len(parameters) and (parameters[end] != 'PUBLIC'
                and parameters[end] != 'PRIVATE'
                and parameters[end] != 'INTERFACE'):
            end = end + 1
        dependencies = parameters[scope_index + 1:end]
        return dependencies

def _sort_dependencies(dependencies):
    if dependencies is None:
        return None
    return sorted(dependencies, key=str.lower)

def _strip_comments(parameter_text):
    comment_pattern = re.compile('#.*\n')
    return comment_pattern.sub('', parameter_text)

def run(file_text):
    start = file_text.find('target_link_libraries')
    if start < 0:
        return file_text
    start = file_text.find('(', start)
    end = file_text.find(')', start)
    parameter_text = file_text[start + 1:end]

    parameters = _strip_comments(parameter_text)
    parameters = parameters.strip()
    parameters = parameters.split()
    target = parameters[0]
    dependencies = parameters[1:]

    # gather public dependencies
    public_dependencies = _sort_dependencies(
            _gather_dependencies('PUBLIC', dependencies))
    private_dependencies = _sort_dependencies(
            _gather_dependencies('PRIVATE', dependencies))
    interface_dependencies = _sort_dependencies(
            _gather_dependencies('INTERFACE', dependencies))

    sorted_parameter_text = target
    if public_dependencies is not None:
        sorted_parameter_text = sorted_parameter_text + ' PUBLIC ' \
                + ' '.join(public_dependencies)
    if private_dependencies is not None:
        sorted_parameter_text = sorted_parameter_text + ' PRIVATE ' \
                + ' '.join(private_dependencies)
    if interface_dependencies is not None:
        sorted_parameter_text = sorted_parameter_text + ' INTERFACE ' \
                + ' '.join(interface_dependencies)
    sorted_parameter_text = sorted_parameter_text

    file_text = file_text.replace(parameter_text, sorted_parameter_text)
    return file_text
