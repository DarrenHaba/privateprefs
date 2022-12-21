import pytest
import argparse, sys

@pytest.mark.parametrize("option", ("-h", "--help"))
def test_help(capsys, option):
    try:
        main([option])
    except SystemExit:
        pass
    output = capsys.readouterr().out
    assert "Stream one or more files with a delay" in output




parser = argparse.ArgumentParser(
    description="Stream one or more files with a delay between each line"
)
parser.add_argument("files", type=argparse.FileType("r"), nargs="*", default=["-"])
parser.add_argument("-d", "--delay-in-ms", type=int, default=100)


def main(args=None):
    parsed_args = parser.parse_args(args)
    delay_in_s = float(parsed_args.delay_in_ms) / 1000