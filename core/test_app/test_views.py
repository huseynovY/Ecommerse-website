from django.urls import reverse_lazy
from django.test import TestCase, Client
from core.forms import ContactForm

class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.url = reverse_lazy('contact')
        client = Client()
        cls.response = client.get(cls.url)
    

    def test_url(self):
        self.assertEqual(self.url, '/en/contact/')

    
    def test_response_url(self):
        self.assertEqual(self.response.status_code, 200)


    def test_response_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_response_context(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)


    @classmethod
    def tearDownClass(cls) -> None:
        pass