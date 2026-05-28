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
import re


class MessageField:
    regex = re.compile(
        r"(?:(CL\d{3})\s+([BCEGRS]\d{4})|(CL\d{3})|([BCEGRS]\d{4}))$")

    def __init__(self):
        self.field: str = ""
        self.required: str = ""
        self.format: str = ""
        self.code_list: str = ""
        self.rules: list[str] = list()

    def parse_line(self, line: str):
        # Reference number R an8 CL172 R0901 (Everything)
        # Binding itinerary R n1 CL027 (no rule)
        # Release date R an10 G0002 (no code list)
        # Message recipient R an..35 (no rule, no codelist)

        # We'll start from the right. Do we have the optional code list and/or rule?
        match = re.search(self.regex, line.strip())

        captured = ""
        code_list = None
        rule = None

        # if we have a match then we have at least the code list or rule
        if match:
            captured = match.group(0)
            code_list = match.group(1) or match.group(3)
            rule = match.group(2) or match.group(4)

        # we now partition the rest of the line by the first space starting from the right
        # this will yield a part containing the field and required, and another one
        # containing the format. we strip where needed for consistency
        line_partition = [s.strip() for s in
                          line.removesuffix(captured).strip().rpartition(" ")]

        field, required = line_partition[0].rsplit(" ", 1)
        field = field.strip()

        field_format = line_partition[2]

        self.field = field
        self.required = required
        self.format = field_format
        self.code_list = code_list

        # we add the rule to the list if present
        if rule is not None:
            self.rules.append(rule)

    def add_rule(self, line: str):
        self.rules.append(line)

    def __str__(self):
        return f"""
         Field: {self.field}
         Required: {self.required}
         Format: {self.format}
         Code List: {self.code_list}
         Rules: {self.rules}
         """


class MessageCategory:
    hyphen_pattern = re.compile("^(-+)")

    def __init__(self, message_type: str):
        self.message_type: str = message_type
        self.category: str = ""
        self.category_name_only: str = ""
        self.multiplicity: str = ""
        self.required: str = ""
        self.rules: list[str] = list()
        self.children: list[MessageField] = list()
        self.level = 0

    def parse_line(self, line: str):
        # "------TRANSPORT CHARGES 1x D C0186"
        # "---TRANSIT OPERATION 1x R" (no rule)

        # a line will always contain the multiplicity, so we can just partition by
        # the lowercase x. this will yield a part containing the category and
        # multiplicity number, and another one containing the required and possibly
        # the rule. we strip where needed for consistency
        line_x_partition = [s.strip() for s in line.rpartition("x")]

        category, multiplicity = line_x_partition[0].rsplit(" ", 1)
        category = category.strip()

        required_and_maybe_rule = line_x_partition[2].split(" ", 1)
        required = required_and_maybe_rule[0].strip()

        rule = None
        if len(required_and_maybe_rule) > 1:
            rule = required_and_maybe_rule[1]

        self.category = re.sub(self.hyphen_pattern, lambda x: f"{x.group(0)} ",
                               category)
        self.category_name_only = category.replace("-", "")
        self.level = int(category.count("-") / 3)
        self.multiplicity = f"{multiplicity}x"
        self.required = required

        # we add the rule to the list if present
        if rule is not None:
            self.rules.append(rule)

    def add_rule(self, line: str):
        self.rules.append(line)

    def add_field(self, field: MessageField):
        self.children.append(field)

    def __str__(self):
        children: list[str] = list()
        for c in self.children:
            children.append(c.__str__())
        return f"""
                Category: {self.category}
                Multiplicity: {self.multiplicity}
                Required: {self.required}
                Rules: {self.rules}
                Children: {children}
                """

    def simple_str(self):
        children: list[str] = list()
        for c in self.children:
            children.append(c.field.__str__())
        return "\n".join([self.category, *children])


class Rule:

    def __init__(self, rule_text: list[str]):
        # first line will be [A-Z]\d{4}\s+Technical Description
        first_line = rule_text[0]
        self.rule_category = first_line[0]
        self.rule_code = first_line[0:5]

        # we split the list on "Functional Description:"
        idx = rule_text.index("Functional Description:")
        self.technical_description = "\n".join(rule_text[1:idx])
        self.functional_description = "\n".join(
            rule_text[idx + 1:len(rule_text)])
