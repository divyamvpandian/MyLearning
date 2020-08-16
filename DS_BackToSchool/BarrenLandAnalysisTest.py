from DS_BackToSchool.BarrenLand import BarrenLand

import unittest

class Testing(unittest.TestCase):
    def test_calculatefertileareas(self):
        land = BarrenLand(10,10)
        land.fillBarrenLand(0,4,5,7)
        area = land.getallfertilelandsarea()
        self.assertEqual(len(area),1)
        self.assertEqual(area[0],76)

    def test_fillbarrenlandnegcoordinatesoutofbounds(self):
        land = BarrenLand(10,10)
        with self.assertRaises(Exception) as context:
            land.fillBarrenLand(0,5,11,7)
        self.assertTrue('Coordinates not within bounds' in str(context.exception))

    def test_fillbarrenlandnegcoordinates(self):
        land = BarrenLand(5,5)
        with self.assertRaises(Exception) as context:
            land.fillBarrenLand(-1,5,11,-7)
        self.assertTrue('Coordinates not within bounds' in str(context.exception))

    def test_barrenland(self):
        land = BarrenLand(10,5)
        self.assertEqual(land.size,50)

    def test_barrenlandnegative(self):
        with self.assertRaises(Exception) as context:
            land = BarrenLand(-4,5)
        self.assertTrue('length and width has to be non negative number' in str(context.exception))

    def test_calculatefertileareaslarge(self):
        land = BarrenLand(100,100)
        land.fillBarrenLand(0,40,99,70)
        area = land.getallfertilelandsarea()
        self.assertEqual(len(area),2)
        self.assertEqual(area[1],2900)

if __name__ == '__main__':
    unittest.main()


