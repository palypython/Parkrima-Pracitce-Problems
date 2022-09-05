from termcolor import colored
from importlib import import_module
import inquirer
from os import listdir
from os.path import isdir, join

problems1 = [
    list(map(lambda x: f + "." + x[:-3], listdir(join("problems", f))))
    for f in listdir("problems") if isdir(join("problems", f))
]
problems = [item for sublist in problems1 for item in sublist]


def has_test(file):
    try:
        i = import_module(f'problems.{file}')
        i.tests
        return True
    except:
        return False


problems = sorted(list(filter(has_test, problems)))
questions = [
    inquirer.List("problem", message="Choose a problem", choices=problems),
]
answers = inquirer.prompt(questions)
current_problem = answers["problem"]


class Tester:

    def __init__(self):
        self.msgs = []
        self.tests = 0
        self.passed_tests = 0

    def set_env(self, env):
        self.env = env

    def ae(self, code, val, msg):
        res = eval(code, self.env)
        self.tests += 1
        if res == val:
            self.msgs.append(f"{self.tests}. ✅ " +
                             colored(f"\"{msg}\" passed", "green"))
            self.passed_tests += 1
        else:
            self.msgs.append(f"{self.tests}. ❌ " +
                             colored(f"\"{msg}\" failed", "red"))
            self.msgs.append(
                f"\texpected {colored(code+' == '+repr(val), 'green')}\n\tbut got {colored(code+' == '+repr(res), 'red')}"
            )

    def show(self):
        print(f"tests passed: ({self.passed_tests}/{self.tests})")
        for msg in self.msgs:
            print(msg)


imported_file = import_module(f'problems.{current_problem}')
test_cases = imported_file.tests
print(f"testing {current_problem}")
tester = Tester()
res = test_cases(tester)
tester.show()
