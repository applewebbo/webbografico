from core.test import TestCase


class IndexView(TestCase):
    def test_get(self):
        response = self.get("index")

        self.response_200(response)
        self.assertTemplateUsed(response, "core/index.html")
