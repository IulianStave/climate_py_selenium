import unittest
import sys
from src.common import common
from src.DataStoreTestCase import DataStoreTest


TESTS = [
    DataStoreTest,
]

parser = common.build_cmd_arguments()
args = parser.parse_args()
driver = common.get_browser(args.browser, args.headless, args.browserpath)
resolution = (args.screenwidth, args.screenheight)
driver.set_window_size(*resolution)
print('Passed URL = ', args.url)

test_suite = unittest.TestSuite()
for test in TESTS:
    # get the available tests
    for name in test.my_tests():
        test_case = test(name, driver, args.url)
        test_suite.addTest(test_case)

# unittest.TextTestRunner(verbosity=args.verbose).run(test_suite)
runner = unittest.TextTestRunner(verbosity=args.verbose)
# runner.run(test_suite)
code = not runner.run(test_suite).wasSuccessful()
driver.quit()
sys.exit(code)
