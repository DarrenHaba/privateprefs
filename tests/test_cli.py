import argparse
import privateprefs.internal.cli as cli


# def test_save():
#     cli._save("Fee", "fi")
#
#
# def test_load():
#     assert False


def test_save(capsys):
    with capsys.disabled():
        cli.main(["save", "foo", "bar"])
    cli.main(["load", "foo"])
    captured = capsys.readouterr()
    assert captured.out.__contains__("bar")


def test_load(capsys):
    with capsys.disabled():
        cli.main(["save", "foo", "bar"])
    cli.main(["load", "foo"])
    captured = capsys.readouterr()
    assert captured.out.__contains__("bar")


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True)
    args = parser.parse_args(argv)
    print(f'Hello {args.name}')


# if __name__ == '__main__':
#     sys.exit(main())


def test_main_even_simpler(capsys):
    main(["--name", "Jürgen"])
    captured = capsys.readouterr()
    print(5555555)
    print(captured)
    assert captured.out == "Hello Jürgen\n"
