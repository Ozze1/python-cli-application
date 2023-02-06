import io
import unittest
import sys
from guestbook import main
import os
import json

class TestGuestbook(unittest.TestCase):

    def setUp(self):
        if os.path.exists('../cli application/guestbook.txt'):
            os.remove('../cli application/guestbook.txt')

    def test_new_command(self):
        sys.argv = ['main', 'new', 'Test message 1']
        main()
        with open('../cli application/guestbook.txt', "r") as file:
            content = file.read().strip()
        self.assertEqual(content, "Test message 1")

    def test_list_command(self):
        sys.argv = ['main', 'new', 'Test message 1']
        main()
        sys.argv = ['main', 'new', 'Test message 2']
        main()
        sys.argv = ['main', 'list']
        output = io.StringIO()
        sys.stdout = output
        main()
        self.assertEqual(output.getvalue().strip(), "Test message 1\nTest message 2")

    def test_edit_command(self):
        sys.argv = ['main', 'new', 'Test message 1']
        main()
        sys.argv = ['main', 'edit', '1', 'Test message 2']
        main()
        with open('../cli application/guestbook.txt', "r") as file:
            content = file.read().strip()
        self.assertEqual(content, "Test message 2")

    def test_delete_command(self):
        sys.argv = ['main', 'new', 'Test message 1']
        main()
        sys.argv = ['main', 'delete', '1']
        main()
        with open('../cli application/guestbook.txt', "r") as file:
            content = file.read().strip()
        self.assertEqual(content, "")

    def test_export_command(self):
        sys.argv = ['main', 'new', 'Test message 1']
        main()
        sys.argv = ['main', 'new', 'Test message 2']
        main()
        sys.argv = ['main', 'export']
        output = io.StringIO()
        sys.stdout = output
        main()
        content = json.loads(output.getvalue().strip())
        print(json.loads(output.getvalue().strip()))
        self.assertEqual(content, ["Test message 1", "Test message 2"])


if __name__ == '__main__':
    unittest.main()
