import os
import sys
import unittest

sys.path.insert(0, '../cmake-tidy')
import ct_core

class FindConfigurationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # test_project/
        #     .cmake-tidy
        #     same.cmake
        #     modules/
        #         foo.cmake
        # bad.cmake
        os.makedirs('test_project/modules')
        f = open('test_project/.cmake-tidy', 'w')
        f.close()
        f = open('test_project/same.cmake', 'w')
        f.close()
        f = open('test_project/modules/good.cmake', 'w')
        f.close()
        f = open('bad.cmake', 'w')
        f.close()

    @classmethod
    def tearDownClass(cls):
        os.remove('test_project/.cmake-tidy')
        os.remove('test_project/same.cmake')
        os.remove('test_project/modules/good.cmake')
        os.remove('bad.cmake')
        os.removedirs('test_project/modules')

    def test_find_in_parent(self):
        cwd = os.getcwd()
        f = ct_core.find_cmake_tidy_configuration(cwd + '/test_project/modules/good.cmake')
        self.assertEqual(f, cwd + '/test_project/.cmake-tidy')

    def test_find_in_same(self):
        cwd = os.getcwd()
        f = ct_core.find_cmake_tidy_configuration(cwd + '/test_project/same.cmake')
        self.assertEqual(f, cwd + '/test_project/.cmake-tidy')

    def test_raise(self):
        cwd = os.getcwd()
        self.assertRaises(
            ValueError,
            ct_core.find_cmake_tidy_configuration,
            cwd + '/test_project/modules/good.cmake')

if __name__ == '__main__':
    unittest.main()
