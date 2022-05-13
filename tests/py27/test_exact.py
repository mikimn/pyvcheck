"""Run with python 2.7.17"""
import sys
from os.path import dirname, join
sys.path.append(join(dirname(__file__), '../'))
from test_utils import generic_fail_test, generic_success_test


def test_exact_version_major_fail():
    generic_fail_test("3")


def test_exact_version_minor_fail():
    generic_fail_test("2.0")


def test_exact_version_patch_fail():
    generic_fail_test("2.7.0")


def test_exact_version_major_success():
    generic_success_test("2")


def test_exact_version_minor_success():
    generic_success_test("2.7")


def test_exact_version_patch_success():
    generic_success_test("   2.7.17")
