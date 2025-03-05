import unittest
from click.testing import CliRunner
from algomancer import cli
import os


class TestAlgomancerCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_hello(self):
        result = self.runner.invoke(cli, ['hello'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('path:', result.output)

    def test_init(self):
        with self.runner.isolated_filesystem():
            result = self.runner.invoke(cli, ['init'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Directories created successfully!', result.output)
            self.assertTrue(os.path.exists('solved'))
            self.assertTrue(os.path.exists('attempting'))
            self.assertTrue(os.path.exists('data_structures'))

    def test_add_problem_easy(self):
        with self.runner.isolated_filesystem():
            self.runner.invoke(cli, ['init'])
            result = self.runner.invoke(cli, ['add_problem', 'test_problem', '-e'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Problem test_problem added successfully!', result.output)
            self.assertTrue(os.path.exists('attempting/easy/test_problem.py'))

    def test_add_problem_medium(self):
        with self.runner.isolated_filesystem():
            self.runner.invoke(cli, ['init'])
            result = self.runner.invoke(cli, ['add_problem', 'test_problem', '-m'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Problem test_problem added successfully!', result.output)
            self.assertTrue(os.path.exists('attempting/medium/test_problem.py'))

    def test_add_problem_hard(self):
        with self.runner.isolated_filesystem():
            self.runner.invoke(cli, ['init'])
            result = self.runner.invoke(cli, ['add_problem', 'test_problem', '-h'])
            self.assertEqual(result.exit_code, 0)
            self.assertIn('Problem test_problem added successfully!', result.output)
            self.assertTrue(os.path.exists('attempting/hard/test_problem.py'))

    def test_add_problem_no_difficulty(self):
        with self.runner.isolated_filesystem():
            self.runner.invoke(cli, ['init'])
            result = self.runner.invoke(cli, ['add_problem', 'test_problem'])
            self.assertNotEqual(result.exit_code, 0)
            self.assertIn('Error: You must specify a difficulty using -e, -m, or -h.', result.output)


if __name__ == '__main__':
    unittest.main()