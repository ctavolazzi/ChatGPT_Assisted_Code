# Here's a simple test environment that can be used to test your skills with Python.
class TestEnvironment:
    def __init__(self):
        self.tests = []
        self.test_results = []
        self.passed = 0
        self.failed = 0

    def set_name(self, name):
        self.name = name
        return self

    def add_test(self, test):
        self.tests.append(test)

    def run_tests(self):
        for test in self.tests:
            try:
                result = test()
                self.test_results.append((test.__name__, result, True))
                self.passed += 1
            except AssertionError as e:
                self.test_results.append((test.__name__, str(e), False))
                self.failed += 1

    def print_results(self):
        print(f'Total tests: {len(self.tests)}')
        print(f'Passed: {self.passed}')
        print(f'Failed: {self.failed}')
        print('---------------------------------------')
        for result in self.test_results:
            print(f'{result[0]}: {"PASSED" if result[2] else "FAILED"}')
            print(f'Result: {result[1]}')
            print('---------------------------------------')

if __name__ == '__main__':
    te = TestEnvironment()

    def test_1():
        assert 1 == 1

    def test_2():
        assert 1 == 2

    te.add_test(test_1)
    te.add_test(test_2)

    te.run_tests()
    te.print_results()