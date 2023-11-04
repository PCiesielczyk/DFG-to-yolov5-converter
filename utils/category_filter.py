def forbidden_classes_ids(classnames_file_path: str, forbidden_classnames_file_path: str) -> list[int]:
    classnames_file = open(classnames_file_path, 'r')
    classnames_lines = classnames_file.read().splitlines()

    forbidden_classnames_file = open(forbidden_classnames_file_path, 'r')
    forbidden_classnames = forbidden_classnames_file.read().splitlines()

    output = []

    for classnames_line in classnames_lines:
        classname_line_split = classnames_line.split(' ')

        class_id = int(classname_line_split[3]) - 1
        classname = classname_line_split[5]

        if classname in forbidden_classnames:
            output.append(class_id)

    return output
