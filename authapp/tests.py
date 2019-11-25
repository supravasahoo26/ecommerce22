from django.test import TestCase
from authapp.models import Signin,Signup
class SigninTestCase(TestCase):
    def setUp(self):
        Signin.objects.create(username="zx",password="zx123")
    def test_signup_correct(self):
        c1=Signin.objects.get(username="zx",password="zx123")
        self.assertEqual(c1.get_user(),"zx")
       # self.assertEqual()

class SignupTestCase(TestCase):
    def setUp(self):
        Signup.objects.create(firstname="supi",lastname="sahu",username="zx",phone_no="7684097639",email="supravapriyadarshini25@gmail.com",password="zx123",rpsw="zx123")
    def test_signup_correct(self):
        c1=Signup.objects.get(firstname="supi")
        self.assertEqual(c1.get_fname(),"supi")
        #self.assertEqual()
