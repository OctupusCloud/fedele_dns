from django.urls import reverse
from django.test import SimpleTestCase

from fedele_dns import __version__
from fedele_dns.tests.custom import APITestCase


class NetBoxDNSVersionTestCase(SimpleTestCase):
    def test_version(self):
        assert __version__ == "0.21.17"


class AppTest(APITestCase):
    def test_root(self):
        url = reverse("plugins-api:fedele_dns-api:api-root")
        response = self.client.get(f"{url}?format=api", **self.header)

        self.assertEqual(response.status_code, 200)
