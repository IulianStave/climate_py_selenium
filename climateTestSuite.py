import unittest
from src.common import common
from src.SearchTestCase import SearchTest
from src.HomePageTestCase import HomePageTest
from src.DataStoreTestCase import DataStoreTest


TESTS = [
    HomePageTest,
    SearchTest,
    DataStoreTest,
]

parser = common.build_cmd_arguments()
args = parser.parse_args()
driver = common.get_browser(args.browser, args.headless, args.browserpath)
resolution = (args.screenwidth, args.screenheight)
driver.set_window_size(*resolution)


test_suite = unittest.TestSuite()
for test in TESTS:
    # get the available tests
    for name in test.my_tests():
        test_case = test(name, driver)
        test_suite.addTest(test_case)

unittest.TextTestRunner(verbosity=args.verbose).run(test_suite)
driver.quit()
