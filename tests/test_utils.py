from pyvcheck import version, VersionError


def generic_fail_test(version_str):
    @version(version_str)
    def _main():
        pass

    try:
        _main()
        assert False
    except VersionError as e:
        pass


def generic_success_test(version_str):
    @version(version_str)
    def _main():
        pass

    try:
        _main()
    except VersionError as e:
        print(e)
        assert False