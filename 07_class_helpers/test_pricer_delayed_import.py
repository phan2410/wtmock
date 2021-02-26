from unittest import TestCase, expectedFailure
# not importing `pricer`
import mock

class TestCountryPrices(TestCase):

    def test_delayed_import(self):
        with mock.patch('pricer.COUNTRIES', ['GB']):
            from pricer import CountryPricer
            pricer = CountryPricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)
