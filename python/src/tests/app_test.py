# coding=utf-8
import unittest

from app.app import is_tdd_course


class TestApp(unittest.TestCase):

    def test_is_tdd_course(self):
        self.assertTrue(is_tdd_course())