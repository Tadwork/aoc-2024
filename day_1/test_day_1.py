import unittest
from unittest.mock import mock_open, patch
from day_1 import read_input_into_lists
from day_1 import compute_min_distance_between_lists
from day_1 import calc_total_similarity_score

class TestReadInputIntoSortedLists(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='3 4\n1 2\n5 6\n')
    @patch('os.path.dirname', return_value='/dev/aoc-2024/1')
    def test_read_input_into_sorted_lists(self, mock_dirname, mock_open):
        expected_list_1 = [3, 1, 5]
        expected_list_2 = [4, 2, 6]
        list_1, list_2 = read_input_into_lists()
        self.assertEqual(list_1, expected_list_1)
        self.assertEqual(list_2, expected_list_2)

    @patch('builtins.open', new_callable=mock_open, read_data='10 20\n30 40\n')
    @patch('os.path.dirname', return_value='/aoc-2024/1')
    def test_read_input_with_different_values(self, mock_dirname, mock_open):
        expected_list_1 = [10, 30]
        expected_list_2 = [20, 40]
        list_1, list_2 = read_input_into_lists()
        self.assertEqual(list_1, expected_list_1)
        self.assertEqual(list_2, expected_list_2)

    @patch('builtins.open', new_callable=mock_open, read_data='')
    @patch('os.path.dirname', return_value='/aoc-2024/1')
    def test_read_input_with_empty_file(self, mock_dirname, mock_open):
        expected_list_1 = []
        expected_list_2 = []
        list_1, list_2 = read_input_into_lists()
        self.assertEqual(list_1, expected_list_1)
        self.assertEqual(list_2, expected_list_2)
        
class TestComputeMinDistanceBetweenLists(unittest.TestCase):
    def test_compute_min_distance_between_lists(self):
        list_1 = [3,4,2,1,3,3]
        list_2 = [4,3,5,3,9,3]
        expected_distance = 11
        distance = compute_min_distance_between_lists(list_1, list_2)
        self.assertEqual(distance, expected_distance)

class TestComputeSimilarityScore(unittest.TestCase):
    def test_calc_total_similarity_score(self):
        list_1 = [3,4,2,1,3,3]
        list_2 = [4,3,5,3,9,3]
        expected_distance = 31
        distance = calc_total_similarity_score(list_1, list_2)
        self.assertEqual(distance, expected_distance)

if __name__ == '__main__':
    unittest.main()