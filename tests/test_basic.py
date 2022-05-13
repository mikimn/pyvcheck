from pyvcheck import version


def test_basic_1():
    @version("3.5")
    def _main():
        x = 3
        return x + 1

    assert _main() == 4
