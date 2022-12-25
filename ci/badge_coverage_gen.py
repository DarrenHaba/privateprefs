import pkg_resources
import re

from xml.dom import minidom

path_to_coverage_xml = pkg_resources.resource_filename(__name__, '../coverage.xml')
path_to_readme = pkg_resources.resource_filename(__name__, '../README.md')

url_link = "https://github.com/DarrenHaba/privateprefs/actions"


def get_coverage_percentage() -> int:
    xml_doc = minidom.parse(path_to_coverage_xml)
    elements = xml_doc.getElementsByTagName('coverage')
    coverage_decimal = elements[0].attributes['line-rate'].value
    coverage_percentage = int(float(coverage_decimal) * 100)
    return coverage_percentage


def get_readme_str() -> str:
    with open(path_to_readme, "r") as file:
        readme_str = file.read()
        return readme_str


def set_readme_str(readme_str):
    with open(path_to_readme, "w") as file:
        file.write(readme_str)


def get_badge_link(percent, link, title="Coverage", color=None, symbol: str = "%25"):
    green = "31c653"
    yellow = "yellow"
    red = "red"

    if color is None:
        if 85 < percent <= 100:
            color = green
        elif 60 < percent <= 85:
            color = yellow
        else:
            color = red
    return f"[![Pytest - Coverage](https://img.shields.io/badge/{title}-{percent}{symbol}-{color})]({link})"


def generate_badge():
    pct = get_coverage_percentage()
    regex_pattern = r"\[\!\[Pytest - Coverage\].*"
    new_readme_str = re.sub(regex_pattern, get_badge_link(pct, url_link), get_readme_str())
    set_readme_str(new_readme_str)


if __name__ == "__main__":
    generate_badge()
