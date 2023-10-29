#!/usr/bin/env python3
""" Unittests and integration tests """
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, res, mock_test):
        """test for correct org returned"""
        test_cls = GithubOrgClient(res)
        test_cls.org()
        mock_test.assert_called_once_with(test_cls.ORG_URL.format(org=res))
