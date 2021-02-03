import unittest
class TestStringMethods(unittest.TestCase):
    #setup 和 teardown 在所每条测试用例前后分别调用一次
    def setUp(self) -> None:
        print("set up")

    def tearDown(self) -> None:
        print("tear down")
    #setupclass和teardownclass是在整个类的前后分别调用
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def test_upper(self):
        print("test_upper 01")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper 02")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        print("test_solit 03")
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()