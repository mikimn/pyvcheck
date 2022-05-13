"""Run with python 3.7.6"""
import sys
from os.path import dirname, join
sys.path.append(join(dirname(__file__), '../'))
from test_utils import generic_fail_test, generic_success_test


def test_unary_gt_version_major_fail():
    generic_fail_test(">3")


def test_unary_ge_version_major_fail():
    generic_fail_test(">=4")


def test_unary_lt_version_major_fail():
    generic_fail_test("<3")


def test_unary_le_version_major_fail():
    generic_fail_test("<=2")


def test_unary_gt_version_major_success():
    generic_success_test(">2")


def test_unary_ge_version_major_success():
    generic_success_test(">=3")


def test_unary_lt_version_major_success():
    generic_success_test("<6")


def test_unary_le_version_major_success():
    generic_success_test("<=4")