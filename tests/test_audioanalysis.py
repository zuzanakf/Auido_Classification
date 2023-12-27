import unittest
import os
import shutil
from scripts.audio_analysis import short_term_feature_extraction  # Adjust the import path according to your project structure

class TestAudioAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary directory for output files
        cls.temp_dir = "temp_test_dir"
        os.makedirs(cls.temp_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        # Clean up: Remove the temporary directory after tests
        shutil.rmtree(cls.temp_dir)

    def test_short_term_feature_extraction(self):
        # Use a sample audio file for testing
        test_audio_file = "tests\\test_data\\sample.wav"  # Replace with the path to a real or mock audio file
        output_dir = self.temp_dir

        # Run the function
        short_term_feature_extraction(test_audio_file, output_dir)

        # Check if the output file is created
        expected_output_file = os.path.join(output_dir, 'short_term_features', os.path.basename(test_audio_file) + '_features.png')
        self.assertTrue(os.path.exists(expected_output_file), "Output file not created")

# Add more test cases for other functions

if __name__ == '__main__':
    unittest.main()
