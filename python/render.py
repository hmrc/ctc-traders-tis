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

save_location = path.join("..", "source", "documentation", "partials")

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
    return f"""<a href="../phase-6-rules.html#{rule.lower()}">{rule}</a>"""


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
    if not path.exists(save_location):
        os.makedirs(save_location)
    print(f"Writing file {file_name}")
    with open(file=path.join(save_location, file_name), mode="w") as md_file:
        md_file.write(render_type(categories, message_type))


def process_rule_string(string: str, rule_code: str) -> str:
    formatted = indent_rule(string, rule_code)
    formatted = replace_code_list_full_string(formatted)
    formatted = formatted.replace("*", "<span>&#42;</span>")
    return formatted


specific_line_break_rules: list[str] = []


def indent_rule(rule_text: str, rule_code: str = '', allow_else_nesting: bool = False) -> str:
    """
    Indents a rule text.

    :param rule_text: The rule description
    :param rule_code: The rule code to identify it in case of errors
    :param allow_else_nesting: Whether to allow else blocks to contain nested conditionals
    :return: The indented rule description with escaped HTML entities
    """
    rule_text = rule_text.replace('\xa0', ' ')
    rule_text = rule_text.replace('\r\n', '\n')
    rule_text = rule_text.replace('\r', '\n')
    rule_text = rule_text.replace('<', '&lt;').replace('>', '&gt;')
    rule_text = re.sub(r' = "([^"]*)"', r'&nbsp;=&nbsp;"\1"', rule_text)

    rule_lines: list[str] = list(map(lambda rl: rl.strip(), rule_text.split('\n')))

    indented_rule_lines = []

    ifs = []

    base_indent = 4

    for line_number, rule_line in enumerate(rule_lines):
        # some rules have empty lines
        if not rule_line:
            indented_rule_lines.append('<br>')
        # some rule lines start with an 'IF
        # ex: C0467 line 1
        elif rule_line.startswith('IF') or rule_line.startswith('\'IF') or rule_line.startswith('THEN IF'):
            if not allow_else_nesting:
                while ifs and ifs[-1]:
                    ifs.pop()

            depth = len(ifs)

            indented_rule_lines.append(f"{depth * base_indent * '&nbsp;'}{rule_line}")

            ifs.append(False)
        elif rule_line.startswith('ELSE'):
            while ifs and ifs[-1]:
                ifs.pop()

            if not ifs:
                error_message_iter = map(lambda rl: f"{rl[0] + 1}. {rl[1]}", enumerate(rule_lines))
                raise RuntimeError(
                    f"Malformed rule: found unmatchable ELSE on line: {line_number + 1} in rule {rule_code}\n" +
                    "\n".join(error_message_iter)
                )

            depth = len(ifs)

            # some rule lines start with ELSE IF where there are more than 1 spaces between ELSE and IF
            # ex: C0003 line 5
            if not re.match(r"^ELSE\s*IF", rule_line):
                else_suite = rule_line[5:]
                indented_rule_lines.append(f"{(depth - 1) * base_indent * '&nbsp;'}ELSE")

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
    return cleandoc(
        f"""## {rule.rule_code}

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


def write_rules_file(category: str, rules: list[Rule]):
    """
    Writes the rules for a given category to a markdown file named "rules/_rules_X.md"
    :param category: The rule category, a single letter
    :param rules: The rules to render
    :return: None
    """
    file_name = f"_rules_{category}.md"
    print(f"Writing file {file_name}")
    if not path.exists(save_location):
        os.makedirs(save_location)
    with open(file=path.join(save_location, file_name), mode="w") as md_file:
        md_file.write(render_rules(rules))
