from django.urls import reverse_lazy
from django.test import TestCase, Client


class BlogViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('blog')
        client = Client()
        cls.response = client.get(cls.url)



    def test_url(self):
        self.assertEqual(self.url, '/en/blog/')

    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_template(self):

        self.assertTemplateUsed(self.response, 'blog.html')

    @classmethod
    def tearDownClass(cls) -> None:
        pass
    
