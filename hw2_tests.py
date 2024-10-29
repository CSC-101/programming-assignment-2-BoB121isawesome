import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle(self):
        point1= data.Point(1, 1)
        point2= data.Point(3, 2)
        expected= data.Rectangle(data.Point(1,2), data.Point(3,1))
        self.assertEqual(expected, hw2.create_rectangle(point1, point2))

    def test_create_rectangle_2(self):
        point1= data.Point(-1, -6)
        point2= data.Point(5, -6)
        expected= data.Rectangle(data.Point(-1,-6), data.Point(5,-6))
        self.assertEqual(expected, hw2.create_rectangle(point1, point2))

    # Part 2
    def test_shorter_duration_than(self):
        dur1 = data.Duration(3,52)
        dur2 = data.Duration(4,21)
        self.assertEqual(True, hw2.shorter_duration_than(dur1,dur2))

    def test_shorter_duration_than_2(self):
        dur1 = data.Duration(3,52)
        dur2 = data.Duration(3,52)
        self.assertEqual(False, hw2.shorter_duration_than(dur1,dur2))

    # Part 3
    def test_songs_shorter_than(self):
        dur = data.Duration(3,52)
        song1 = data.Song('Kanye','Runaway',data.Duration(3,51))
        song2 = data.Song('Travis Scott','FEIN',data.Duration(4,51))
        song3 = data.Song('SZA','Kill Bill',data.Duration(3,31))
        song4 = data.Song('NewJeans','OMG',data.Duration(4,50))
        song_list=[song1,song2,song3,song4]
        expected=[song1,song3]
        self.assertEqual(expected, hw2.songs_shorter_than(song_list,dur))

    def test_songs_shorter_than_2(self):
        dur = data.Duration(4,39)
        song1 = data.Song('Joji','Die For You',data.Duration(3,51))
        song2 = data.Song('NewJeans', 'Ditto', data.Duration(3, 31))
        song3 = data.Song('Travis Scott','FEIN',data.Duration(4,51))
        song4 = data.Song('Childish Gambino','Les',data.Duration(5,17))
        song_list=[song1,song2,song3,song4]
        expected=[song1,song2]
        self.assertEqual(expected, hw2.songs_shorter_than(song_list,dur))

    # Part 4
    def test_running_time(self):
        song1 = data.Song('Kanye','Runaway',data.Duration(3,51))
        song2 = data.Song('Travis Scott','FEIN',data.Duration(4,51))
        song3 = data.Song('SZA','Kill Bill',data.Duration(3,31))
        song4 = data.Song('NewJeans','OMG',data.Duration(4,50))
        song_list=[song1,song2,song3,song4]
        nums_list=[0,1,2,3,2,3]
        expected=data.Duration(25,24)
        self.assertEqual(expected, hw2.running_time(song_list,nums_list))

    def test_running_time_2(self):
        song1 = data.Song('Kanye','Runaway',data.Duration(3,49))
        song2 = data.Song('Travis Scott','FEIN',data.Duration(4,51))
        song3 = data.Song('SZA','Kill Bill',data.Duration(5,21))
        song4 = data.Song('NewJeans','OMG',data.Duration(4,50))
        song_list=[song1,song2,song3,song4]
        nums_list=[0,1,2,3,2,3]
        expected=data.Duration(29,2)
        self.assertEqual(expected, hw2.running_time(song_list,nums_list))

    # Part 5
    def test_validate_route(self):
        city_links = [['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]
        route=['san luis obispo', 'santa margarita', 'atascadero']
        self.assertEqual(True, hw2.validate_route(city_links,route))

    def test_validate_route_2(self):
        city_links = [['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            #['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]
        route=['san luis obispo', 'santa margarita', 'atascadero']
        self.assertEqual(False, hw2.validate_route(city_links,route))

    # Part 6
    def test_longest_repetition(self):
        num_list=[1, 1, 2, 2, 1, 1, 1, 3]
        expected=4
        self.assertEqual(expected, hw2.longest_repetition(num_list))

    def test_longest_repetition_2(self):
        num_list=[1, 1, 1, 2, 2, 1, 1, 1, 3,3,3,3]
        expected=8
        self.assertEqual(expected, hw2.longest_repetition(num_list))

if __name__ == '__main__':
    unittest.main()
