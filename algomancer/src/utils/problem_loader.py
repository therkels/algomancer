import importlib


def get_solution(difficulty, problem):
    module = importlib.import_module(f'solutions.{difficulty}.{problem}.main')
    return module.Solution()


def get_tests(difficulty, problem):
    module = importlib.import_module(f'solutions.{difficulty}.{problem}.test')
    return module.TestCases()