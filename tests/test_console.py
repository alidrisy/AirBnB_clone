#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import FileIO
import sys


class TestHBNBCommand(unittest.TestCase):

    def test_help(self):
        with open('test.txt', "w") as fp:
            with patch('sys.stdout', new=fp) as f:
                HBNBCommand().onecmd("help show")

        help_str = "Prints the string representation of an instance based\
 on the class name and id.\nUsage: show <class name> <id>\n\n"
        with open('test.txt', "r") as fp:
            s = fp.read()
            self.assertEqual(s, help_str)

    def test_all(self):
        with open('test.txt', "w") as fp:
            with patch('sys.stdout', new=fp) as f:
                HBNBCommand().onecmd("help all")

        help_str = "Prints all string representation of all instances based or not on the class name.\nUsage: all <class name> or all\n\n"
        with open('test.txt', "r") as fp:
            s = fp.read()
            self.assertEqual(s, help_str)
