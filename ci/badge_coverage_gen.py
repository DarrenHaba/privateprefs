import re
import argparse
import pkg_resources

from xml.dom import minidom

path_to_coverage_xml = pkg_resources.resource_filename(__name__, '../coverage.xml')
path_to_readme = pkg_resources.resource_filename(__name__, '../README.md')

path_to_coverage = path_to_coverage_xml
path_to_readme = path_to_readme


def get_coverage_percentage():
    xml_doc = minidom.parse(path_to_coverage)
    elements = xml_doc.getElementsByTagName('package')
    coverage_decimal = elements[0].attributes['line-rate'].value
    coverage_percentage = int(float(coverage_decimal) * 100)
    return coverage_percentage


def get_readme_str():
    with open(path_to_readme, "r") as file:
        readme_str = file.read()
        return readme_str


def get_code_snipit(percent, link: str = "https://coveralls.io/github/badges/shields", symbol: str = "%25"):
    return f'<!-- coverage badge snipit -->\n' \
           f'<a href="{link}">\n' \
           f'<img src="https://img.shields.io/badge/coverage-{percent}{symbol}-green"\n' \
           f'alt="coverage"></a>\n' \
           f'<!-- coverage badge snipit -->'


def generate_badge(
        pattern="<!-- coverage badge snipit -->((.|\n)*)[a-z]*<!-- coverage badge snipit -->",
        percent=get_coverage_percentage()
):
    new_readme = re.sub(pattern,
                        get_code_snipit(percent, link="https://github.com/DarrenHaba/privateprefs/actions"),
                        get_readme_str())

    with open(path_to_readme, "w") as file:
        file.write(new_readme)


parser = argparse.ArgumentParser()

if __name__ == "__main__":
    generate_badge()

