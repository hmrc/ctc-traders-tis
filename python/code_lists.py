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
import csv
from typing import Optional

# Codelist to URLs
code_lists: Optional[dict[str, str]] = None
code_list_links: Optional[str] = None


class CodeList:
    def __init__(self, dictionary: dict):
        self.code_list = dictionary["Code List"]
        self.title = dictionary["Title"]


def load_code_list() -> dict[str, CodeList]:
    global code_lists
    if code_lists is None:
        result: dict[str, CodeList] = {}
        with open(file="code_lists.csv", mode="r") as code_list_file:
            reader = csv.DictReader(code_list_file, delimiter=",")
            for row in reader:
                code_list = CodeList(row)
                result[code_list.code_list] = code_list

        code_lists = result

    return code_lists


def generate_table_with_code_list_links() -> str:
    global code_list_links
    if code_list_links is None:
        phase6 = "NCTS-P6"
        base = "https://ec.europa.eu/taxation_customs/dds2/rd/compressed_file/data_download"

        markdown = "| Code list | Title | Link |\n"
        markdown += "|-----------|-------|------|\n"

        with open("code_lists.csv", 'r') as code_list_file:
            reader = csv.DictReader(code_list_file)
            rows = list(reader)
            rows = sorted(rows, key=lambda r: r["Code List"])

            for row in rows:
                code = row["Code List"].strip()
                title = row["Title"].strip()
                url = f"{base}/RD_{phase6}_{title}.zip"
                markdown += f"| {code} | {title} | <a href=\"{url}\">Download</a> |\n"

        code_list_links = markdown

    return code_list_links


def replace_code_list(cl: str) -> str:
    """
    If the codelist exists in the dict, wraps the codelist in an HTML link. Else, returns the codelist
    :param cl: The codelist
    :return: The codelist, with or without a hyperlink wrapping
    """
    return cl


def replace_code_list_full_string(string: str) -> str:
    """
    Takes a string and adds links to any known codelists

    :param string: The string
    :return: The linkified string
    """
    replaced = string
    for key, item in load_code_list().items():
        replaced = replaced.replace(key, replace_code_list(key))
    return replaced
