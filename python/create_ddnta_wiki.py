import csv
import os.path
import sys


class MdTable:
    def __init__(self, header_row, rows):
        if not header_row:
            raise ValueError(f"Header row cannot be empty")

        self._header_row = header_row

        if not len(rows):
            raise ValueError(f"Rows cannot be empty")

        self._rows = rows
        self._no_of_cols = len(header_row)

        self._max_col_lengths = [len(header_row_col) for header_row_col in
                                 header_row]

        for row in rows:
            if len(row) != self._no_of_cols:
                raise ValueError(
                    f"Row {row} has wrong number of cells. Expected: {self._no_of_cols}")

            for i in range(self._no_of_cols):
                self._max_col_lengths[i] = max(len(row[i]),
                                               self._max_col_lengths[i])

        self._formatted_table = None

    def _create_formatted_row(self, row):
        formatted_row = '|'

        for i, cell in enumerate(row):
            formatted_row += f" {cell}{' ' * (self._max_col_lengths[i] - len(cell))} |"

        return formatted_row

    def _create_separator_row(self):
        separator_row = '|'

        for max_col_length in self._max_col_lengths:
            separator_row += '-' * (max_col_length + 2) + '|'

        return separator_row

    def generate_formatted_table(self):
        if self._formatted_table is not None:
            return self._formatted_table

        formatted_header_row = self._create_formatted_row(self._header_row)
        separator_row = self._create_separator_row()

        formatted_table_rows = [formatted_header_row, separator_row]

        for row in self._rows:
            formatted_row = self._create_formatted_row(row)

            formatted_table_rows.append(formatted_row)

        self._formatted_table = '\n'.join(formatted_table_rows)

        return self._formatted_table


def _extract_delta_paths(ddnta_delta: str):
    removed_paths = []
    changed_paths = []
    added_paths = []

    ddnta_delta_items = [item for item in ddnta_delta.splitlines()
                         if item.startswith('-')]

    for delta_item in ddnta_delta_items:
        path, description = delta_item.rsplit('>', 1)

        path = path.strip('- ')
        description = description.strip()
        description_insensitive = description.lower()

        target_path = None
        if 'remove' in description_insensitive or 'delete' in description_insensitive:
            target_path = removed_paths
        elif 'change' in description_insensitive:
            target_path = changed_paths
        elif 'add' in description_insensitive:
            target_path = added_paths

        if target_path is not None:
            target_path.append((path, description))

    sorted_removed_paths = sorted(removed_paths, key=lambda x: x[0])

    sorted_changed_paths = sorted(changed_paths, key=lambda x: x[0])

    sorted_added_paths = sorted(added_paths, key=lambda x: x[0])

    sorted_paths = {}

    def maybe_add_to_dict(d, k, v):
        if v:
            d[k] = v

    maybe_add_to_dict(sorted_paths, 'removed', sorted_removed_paths)
    maybe_add_to_dict(sorted_paths, 'changed', sorted_changed_paths)
    maybe_add_to_dict(sorted_paths, 'added', sorted_added_paths)

    return sorted_paths


def _generate_md_from_ddnta(ddnta_rows):
    md = ['## Message Changes\n', '---\n']

    for ddnta_row in ddnta_rows:
        ddnta_delta = ddnta_row['delta (p5 vs p6)']
        ddnta_code = ddnta_row['code']
        ddnta_message = ddnta_row['message']

        table_heading = f"### {ddnta_code.strip('\'')} - {ddnta_message}\n"

        paths_by_status = _extract_delta_paths(ddnta_delta)

        if paths_by_status:
            message_section = [table_heading]
            for status, paths_with_descriptions in paths_by_status.items():
                md_table = create_md_messages_table(status,
                                                    paths_with_descriptions)

                message_section.append(f"{md_table}\n")

            message_section.append('---\n')

            md.append('\n'.join(message_section))

    return '\n'.join(md)


def create_md_messages_table(status, paths_with_descriptions):
    table_header_row = ['Key', 'Description']

    messages_md_table = MdTable(table_header_row, paths_with_descriptions)

    md_messages_table = messages_md_table.generate_formatted_table()

    return '\n'.join(
        [f"**{status.capitalize()}**\n", md_messages_table])


def _read_ddnta_csv(path_to_csv, ddnta_fields):
    ddnta_rows: list[dict[str, str]] = []

    try:
        with open(path_to_csv, newline='') as rf:
            reader = csv.DictReader(rf)

            for row_no, row in enumerate(reader):
                dict_row = {field_name.lower(): field
                            for field_name, field in row.items()
                            if field_name.lower() in ddnta_fields and field}

                if len(dict_row) < len(ddnta_fields):
                    print(
                        f"Essential fields missing from current row {row_no + 1}: "
                        f"{ddnta_fields.difference(dict_row.keys())}")

                    sys.exit(1)
                else:
                    ddnta_rows.append(dict_row)

    except FileNotFoundError:
        print("DDNTA analysis document not found")

        sys.exit(1)

    return ddnta_rows


def _write_ddnta_md_file(path_to_md_file, md_file):
    try:
        with open(path_to_md_file, mode='w') as wf:
            wf.write(md_file)
    except Exception as e:
        print(f"Error while writing DDNTA Md file: {e}")

        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python create_ddnta_wiki.py <path_to_ddnta_analysis_doc> <md_output_path>")

        sys.exit(1)

    path_to_ddnta_csv = os.path.abspath(os.path.expanduser(sys.argv[1]))

    md_output_path = os.path.abspath(os.path.expanduser(sys.argv[2]))

    if not os.path.isdir(md_output_path):
        print("Md file output path needs to be a directory")

        sys.exit(1)

    if not os.path.isfile(path_to_ddnta_csv):
        print("DDNTA analysis document path is not a file")

        sys.exit(1)

    if not path_to_ddnta_csv.endswith('.csv'):
        print("DDNTA analysis document provided is not a .csv file")

        sys.exit(1)

    ddnta_essential_fields = {'code', 'message', 'delta (p5 vs p6)'}

    ddnta_rows = _read_ddnta_csv(path_to_ddnta_csv, ddnta_essential_fields)

    md = _generate_md_from_ddnta(ddnta_rows)

    path_to_md_file = os.path.join(md_output_path, 'ddnta_changelog.md')

    _write_ddnta_md_file(path_to_md_file, md)


if __name__ == '__main__':
    main()
