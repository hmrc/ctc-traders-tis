"""
 Copyright 2023 HM Revenue & Customs

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import os
import re
from inspect import cleandoc
from os import path
from typing import Optional

from code_lists import replace_code_list, replace_code_list_full_string
from data_types import MessageCategory, MessageField, Rule

partials_save_location = path.join("..", "source", "documentation", "partials")

special_formats = {
    "Message sender": """an..35""",
    "Message recipient": """an..35"""
}

head_tag = """<table cellspacing="0" style="table-layout: fixed; width: 100%;">
<colgroup>
    <col style="width: 40%;">
    <col style="width: 10%;">
    <col style="width: 20%;">
    <col style="width: 15%;">
    <col style="width: 15%;">
</colgroup>"""
header_row = """
<tr>
<th>
   Field Name
  </th>
<th>
   Priority
  </th>
<th>
   Format / Max Repeat
  </th>
<th>
   Code Lists
  </th>
<th>
   Rules
  </th>
</tr>
"""

tail = """</table>"""


def linkify_rule(rule: str) -> str:
    return f"""<a href="../phase-6-rules/{rule}.html">{rule}</a>"""


def create_rules(rules: list[str]):
    if len(rules) > 0:
        return "<br />".join(map(linkify_rule, rules))
    else:
        return "&nbsp;"


def render_optional_code_list(value: Optional[str]) -> str:
    """
    Creates links for code lists that have associated URIs

    :param value: The codelist, if there is one
    :return: A non-breaking space if no code list, or the codelist, potentially with a link
    """
    if value is None:
        return "&nbsp;"
    else:
        return replace_code_list(value)


level_counter = 0

parent_stack = []

message_type_prefix = ""


def get_next_level():
    global level_counter
    level_counter += 1
    return f"{message_type_prefix}_{level_counter - 1}"


def reset_level_counter(message_type: str = ""):
    global level_counter
    global parent_stack
    global message_type_prefix
    level_counter = 0
    parent_stack = []
    message_type_prefix = message_type


# ---- Rendering for Message Types

def render_category_row(category: MessageCategory, indent_offset: int = 0) -> str:
    """
    Creates a table row for a category and associated rows for the fields

    :param category: The category
    :param indent_offset: Number of indentation levels to subtract (for flattening)
    :return: The HTML
    """
    global parent_stack

    current_level = get_next_level()

    cat = category.category.replace("---", "")
    hyphens = category.category.count("---")

    # Apply indent offset to reduce indentation
    adjusted_hyphens = max(0, hyphens - indent_offset)
    indent = "&nbsp;" * (4 * adjusted_hyphens) if adjusted_hyphens > 0 else ""

    # Adjust parent stack tracking for the offset
    effective_hyphens = hyphens - indent_offset
    while len(parent_stack) > effective_hyphens:
        parent_stack.pop()

    parent_level = parent_stack[-1] if parent_stack else None

    parent_stack.append(current_level)

    if parent_level is not None:
        parent_attr = f'data-parent="{parent_level}"'
    else:
        parent_attr = ''

    c = cleandoc(f"""
    <tr class="parent-row" data-level="{current_level}" {parent_attr}>
        <td>{indent}<span class="toggle-icon">▾</span> <strong>{cat}</strong></td>
        <td>{category.required}</td>
        <td>{category.multiplicity}</td>
        <td>&nbsp;</td>
        <td>{create_rules(category.rules)}</td>
    </tr>""")

    # Render the fields and return the category and fields together
    return c + render_children_fields(category.children, adjusted_hyphens + 1, current_level)


def render_children_fields(fields: list[MessageField], hyphens: int, parent_level: str) -> str:
    """
    Renders fields

    :param fields: The fields to render
    :param hyphens: The number of indentation levels
    :param parent_level: The parent level ID for these fields
    :return: The HTML
    """
    r = []
    indent = "&nbsp;" * (4 * hyphens) if hyphens > 0 else ""

    for f in fields:
        # The code list and rules will have hyperlinks added to them
        # The format field might have a special format -- this is the case for the message sender and message recipient
        # fields
        r.append(cleandoc(f"""
        <tr data-parent="{parent_level}">
            <td>{indent}{f.field}</td>
            <td>{f.required}</td>
            <td>{special_formats.get(f.field, f.format)}</td>
            <td>{render_optional_code_list(f.code_list)}</td>
            <td>{create_rules(f.rules)}</td>
        </tr>"""))

    return "".join(r)


def render_root_fields(fields: list[MessageField]) -> str:
    """
    Renders fields at the root level (no parent)

    :param fields: The fields to render
    :return: The HTML
    """
    r = []

    for f in fields:
        r.append(cleandoc(f"""
        <tr>
            <td>{f.field}</td>
            <td>{f.required}</td>
            <td>{special_formats.get(f.field, f.format)}</td>
            <td>{render_optional_code_list(f.code_list)}</td>
            <td>{create_rules(f.rules)}</td>
        </tr>"""))

    return "".join(r)


def render_type(categories: list[MessageCategory], message_type: str = "") -> str:
    """
    Renders a message type in its entirety.

    If the first category is "MESSAGE", its fields are rendered at root level
    and subsequent categories are rendered with reduced indentation.

    :param categories: The categories for the message type
    :param message_type: The message type identifier (e.g., "IE004") for scoping
    :return: The HTML
    """
    reset_level_counter(message_type)

    if not categories:
        return head_tag + header_row + tail

    rows = ""
    first_category = categories[0]

    # Check if the first category is MESSAGE (no hyphens = root level MESSAGE)
    if first_category.category.replace("---", "").strip().upper() == "MESSAGE" and "---" not in first_category.category:
        # Render MESSAGE's fields at root level (no parent row for MESSAGE itself)
        rows += render_root_fields(first_category.children)

        # Render remaining categories with indent offset of 1 to shift them left
        for category in categories[1:]:
            rows += render_category_row(category, indent_offset=1)
    else:
        # No MESSAGE wrapper, render normally
        rows = "".join(map(lambda x: render_category_row(x), categories))

    return head_tag + header_row + rows + tail


def write_message_type_file(message_type: str, categories: list[MessageCategory]):
    """
    Writes the message type categories to a file named "messagetypes/_IExxx.md"
    :param message_type: The message type
    :param categories: The categories to render
    :return: None
    """
    file_name = f"_{message_type}_table.md"
    if not path.exists(partials_save_location):
        os.makedirs(partials_save_location)
    print(f"Writing file {file_name}")
    with open(file=path.join(partials_save_location, file_name), mode="w") as md_file:
        md_file.write(render_type(categories, message_type))


def process_rule_string(string: str, rule_code: str) -> str:
    formatted = indent_rule(string, rule_code)
    formatted = replace_code_list_full_string(formatted)
    formatted = formatted.replace("*", "<span>&#42;</span>")
    return formatted


specific_line_break_rules: list[str] = []


def indent_rule(rule_text: str, rule_code: str = '', allow_if_in_else: bool = False) -> str:
    """
    Indents a rule text.
    There are no scope terminators/delimiters, so dangling else problems are solved by pairing the ELSE with
    the nearest unmatched IF. This means that indentation is biased and might not reflect the intended logic.
    Also, an IF clause immediately after another IF clause will be indented within the previous IF clause. In case
    of, for example, C0001, this is correct indentation, but in case of R0506, the IF clauses should be at the same
    level (this is partially circumvented by a lookahead "strategy"). Generally, it's not possible to remedy this unless
    explicit scope delimiters are introduced. For R0506, the original PDF document uses newlines between IF clauses as
    delimiters, but they're being discarded as part of the parsing of the document into rules. This is not consistent
    throughout the document, as for R0507 the IF clauses are not delimited by newlines, despite the fact that the
    intention is for those clauses to be separate and not nested, like R0506.

    :param rule_text: The rule description
    :param rule_code: The rule code
    :param allow_if_in_else: Whether to allow else blocks to contain nested conditionals
    :return: The indented rule description with escaped HTML entities
    """
    # nbsp's are found in some of the rules' descriptions, so we replace them with ordinary whitespaces
    rule_text = rule_text.replace('\xa0', ' ')
    rule_text = rule_text.replace('\r\n', '\n')
    rule_text = rule_text.replace('\r', '\n')
    rule_text = rule_text.replace('<', '&lt;').replace('>', '&gt;')
    rule_text = re.sub(r' = "([^"]*)"', r'&nbsp;=&nbsp;"\1"', rule_text)

    rule_split_lines: list[str] = rule_text.split('\n')

    # some rule lines start with an 'IF ex: C0467 line 1
    # some rule lines start with ELSE IF where there are more than 1 spaces between ELSE and IF: ex C0003 line 5
    rule_sanitize_replacements = [(re.compile(r"^'IF"), 'IF'), (re.compile(r"^ELSE\s+IF"), 'ELSE IF')]

    rule_sanitized_lines: list[str] = []

    for rule_line in rule_split_lines:
        rule_line = rule_line.strip()

        for pattern, repl in rule_sanitize_replacements:
            rule_line = re.sub(pattern, repl, rule_line)

        rule_sanitized_lines.append(rule_line)

    rule_merged_lines: list[str] = []

    rule_if_pattern = re.compile(r"^(?:THEN\s)?IF")

    i = 0
    # merge empty ELSE and THEN lines with the next IF line, if the IF line occurs immediately after
    while i < len(rule_sanitized_lines) - 1:
        if rule_sanitized_lines[i] in ['ELSE', 'THEN'] and re.match(rule_if_pattern, rule_sanitized_lines[i + 1]):
            rule_merged_lines.append(f"{rule_sanitized_lines[i]} {rule_sanitized_lines[i + 1]}")

            i += 1
        else:
            rule_merged_lines.append(rule_sanitized_lines[i])

        i += 1

    if i == len(rule_sanitized_lines) - 1:
        rule_merged_lines.append(rule_sanitized_lines[i])

    indented_rule_lines = []

    ifs = []

    base_indent = 4

    print(f"Indenting rule {rule_code}...")

    for line_number, rule_line in enumerate(rule_merged_lines):
        if re.match(rule_if_pattern, rule_line):
            # when else conditional nesting is not allowed, step out of the else
            if not allow_if_in_else and ifs and ifs[-1]:
                ifs.pop()

            # lookahead strategy;
            # if the current IF is inside the previous IF, if the next clause is IF then there's a
            # high chance, based on looking through the original PDF document, that the current IF
            # should not be nested inside the previous IF
            if rule_line.startswith('IF') and ifs and not ifs[-1]:
                is_next_if = False

                i = line_number + 1
                while i < len(rule_merged_lines):
                    if rule_merged_lines[i].startswith('ELSE'):
                        break
                    elif re.match(rule_if_pattern, rule_merged_lines[i]):
                        is_next_if = True
                        break

                    i += 1

                if is_next_if or i == len(rule_merged_lines):
                    ifs.pop()

            depth = len(ifs)

            indented_rule_lines.append(f"{depth * base_indent * '&nbsp;'}{rule_line}")

            ifs.append(False)
        elif rule_line.startswith('ELSE'):
            # find nearest unmatched if
            while ifs and ifs[-1]:
                ifs.pop()

            if not ifs:
                error_message_iter = map(lambda rl: f"{rl[0] + 1}. {rl[1]}", enumerate(rule_merged_lines))
                raise RuntimeError(
                    f"Malformed rule: found unmatchable ELSE on line: {line_number + 1} in rule {rule_code}\n" +
                    "\n".join(error_message_iter)
                )

            depth = len(ifs)

            if not rule_line.startswith('ELSE IF'):
                indented_rule_lines.append(f"{(depth - 1) * base_indent * '&nbsp;'}ELSE")

                else_suite = rule_line[5:]

                if else_suite:
                    indented_rule_lines.append(f"{depth * base_indent * '&nbsp;'}{else_suite}")

                ifs[-1] = True
            else:
                indented_rule_lines.append(f"{(depth - 1) * base_indent * '&nbsp;'}{rule_line}")
        else:
            depth = len(ifs)

            indented_rule_lines.append(f"{depth * base_indent * '&nbsp;'}{rule_line}")

    return '<br>\n'.join(indented_rule_lines)


def should_replace_line_breaks(rule_code: str) -> bool:
    if rule_code.upper().startswith("C"):
        return True
    else:
        return specific_line_break_rules.__contains__(rule_code.upper())


def render_rule(rule: Rule) -> str:
    """
    Renders a single rule in markdown
    :param rule: The rule to render
    :return: The markdown
    """
    func = process_rule_string(rule.functional_description, rule.rule_code)
    tech = process_rule_string(rule.technical_description, rule.rule_code)
    return cleandoc(f"""
    **Functional Description**

    {func}

    **Technical Description**

    {tech}
    """).replace("    ", "")  # cleandoc/dedent doesn't want to work, so just do it manually


def render_rules(rules: list[Rule]) -> str:
    """
    Renders rules in markdown and joins them together
    :param rules: The rules to render
    :return: The rendered rules
    """
    return "\n\n".join(map(lambda x: render_rule(x), rules))


def _write_md_rules_files(category: str, rules: list[Rule]):
    """
    Writes the rules for a given category to Markdown files named "rules/category/_[a-z]\\d{4}.md"
    :param category: The rule category, a single letter
    :param rules: The rules to render
    :return: None
    """
    rules_md_dir = path.join(partials_save_location, 'rules', category.lower())

    for rule in rules:
        partial_file_name = f"_{rule.rule_code}.md"
        print(f"Writing file {partial_file_name}")
        if not path.exists(rules_md_dir):
            os.makedirs(rules_md_dir)
        with open(file=path.join(rules_md_dir, partial_file_name), mode="w") as md_file:
            md_file.write(render_rule(rule))


rule_num = 0

ruby_templates_save_location = path.join('..', 'source', 'documentation', 'phase-6-rules')


def _write_erb_rules_files(category: str, rules: list[Rule]) -> None:
    global rule_num

    rules_md_dir = path.join(partials_save_location, 'rules', category.lower())

    for rule in rules:
        ruby_template_file_name = f"{rule.rule_code}.html.md.erb"
        partial_file_name = f"_{rule.rule_code}.md"

        partial_file_location = path.join(rules_md_dir, partial_file_name)

        if not path.exists(partial_file_location):
            raise FileNotFoundError(partial_file_location)

        if not path.exists(ruby_templates_save_location):
            os.makedirs(ruby_templates_save_location)

        with open(file=path.join(ruby_templates_save_location, ruby_template_file_name), mode="w") as erb_file:
            content = cleandoc(f"""
            ---
            title: {rule.rule_code}
            weight: {rule_num + 1}
            ---
            
            # {rule.rule_code}
            
            <%= partial 'documentation/partials/rules/{category.lower()}/{rule.rule_code}' %>
            """)

            erb_file.write(content)

            rule_num += 1


def create_md_table(table_header_row: list[str], rows: list[list[str]]) -> str:
    def create_formatted_row(row_with_max_lengths: list[tuple[str, int]]) -> str:
        def transform_func(col_and_max_length: tuple[str, int]) -> str:
            return f" {col_and_max_length[0]}{' ' * (max(col_and_max_length[1] - len(col_and_max_length[0]), 0))} "

        return f"|{'|'.join(map(transform_func, row_with_max_lengths))}|"

    def create_separator_row(max_lengths: list[int]) -> str:
        return f"|{'|'.join([f"{'-' * (max_length + 2)}" for max_length in max_lengths])}|"

    row_max_lengths = [len(col) for col in table_header_row]

    for row in rows:
        if len(row) != len(table_header_row):
            raise ValueError(f"Row {row} has wrong number of elements. Expected: {len(table_header_row)}")

        for i, col in enumerate(row):
            row_max_lengths[i] = max(row_max_lengths[i], len(col))

    table_header_row = create_formatted_row(list(zip(table_header_row, row_max_lengths)))
    table_header_separator_row = create_separator_row(row_max_lengths)

    table_rows = [table_header_row, table_header_separator_row]

    for row in rows:
        formatted_row = create_formatted_row(list(zip(row, row_max_lengths)))

        table_rows.append(formatted_row)

    return "\n".join(table_rows)


def write_rules_index() -> None:
    if not path.exists(ruby_templates_save_location):
        raise FileNotFoundError({ruby_templates_save_location})

    os.remove(path.join(ruby_templates_save_location, 'index.html.md.erb'))

    rule_codes = list(map(lambda fn: fn.rstrip('.html.md.erb'), os.listdir(ruby_templates_save_location)))

    rule_codes = sorted(rule_codes)

    rule_header_row = ['Rule code', 'Category']

    rule_rows = []

    for rule_code in rule_codes:
        category = rule_code[0]
        rule_code_link = f"[{rule_code}](/documentation/phase-6-rules/{rule_code}.html)"
        rule_row = [rule_code_link, category]

        rule_rows.append(rule_row)

    rule_table = create_md_table(rule_header_row, rule_rows)

    index_tile = 'Phase 6 Rules'
    weight = 5
    index_description = ('Software developers, designers, product owners or business analysts. Learn about the '
                         'processes involved in the exchange of messages between traders and phase 6 of the NCTS '
                         'at departure and arrival of transit movements, and about the definitions, formats and '
                         'validations of those messages.')

    index = cleandoc(f"""
    ---
    title: {index_tile}
    weight: {weight}
    description: {index_description}
    ---
    
    # Rules
    
    This section contains the rules used in Phase 6 of NCTS.
    """)

    # cleandoc acting up when interpolating `rule_table` in the f-string
    index += f"\n\n{rule_table}"

    with open(file=path.join(ruby_templates_save_location, 'index.html.md.erb'), mode="w") as index_file:
        index_file.write(index)


def write_rules_files(category: str, rules: list[Rule]) -> None:
    _write_md_rules_files(category, rules)
    _write_erb_rules_files(category, rules)
