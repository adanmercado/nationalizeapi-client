from unittest.mock import MagicMock, patch
from unittest import TestCase

from src.backend import search_name

class TestSearchName(TestCase):
    @patch('requests.get')
    def test_search_name(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''
        {
            "name": "Bart",
            "country": [
                {
                    "country_id": "BE",
                    "probability": 0.4028161178215354
                },
                {
                    "country_id": "NL",
                    "probability": 0.39523038591318027
                },
                {
                    "country_id": "IE",
                    "probability": 0.03918141070021203
                }
            ]
        }
        '''
        mock_requests.return_value = mock_response
        countries = search_name('Bart')

        expected_countries = [
            { 'country_id': 'BE', "probability": 0.4028161178215354 },
            { 'country_id': 'NL', "probability": 0.39523038591318027 },
            { 'country_id': 'IE', "probability": 0.03918141070021203 }
        ]
        self.assertEqual(countries, expected_countries)