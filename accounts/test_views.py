from django.test import TestCase
from django.shortcuts import render, redirect, reverse 
from django.contrib.auth.models import User
from checkout.models import * 

# Create your tests here.

class AccountsPageTests(TestCase):
    
    """
    Tests to check login page is rendering with the correct template
    """

    def test_login_page_status_code_and_path(self):
        response = self.client.get('/accounts/login/')
        self.assertEquals(response.status_code, 200)
        
    def test_login_page_url_name(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_login_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        
        
    """
    Tests to check regisister page is rendering with the correct template
    """

    def test_register_page_status_code_and_path(self):
        response = self.client.get('/accounts/register/')
        self.assertEquals(response.status_code, 200)
        
    def test_register_page_url_name(self):
        response = self.client.get(reverse('registration'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_register_uses_correct_template(self):
        response = self.client.get(reverse('registration'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
        
        
class TestProfileViews(TestCase):
    
    """
    Tests to check user profile
    """
    
    def setUp(self):
        self.user = User.objects.create_user(username='test',
                                        password='testword')
        self.client.login(username='test', password='testword')
        
        
    def test_profile_page_status_and_path(self):
        page = self.client.get('/accounts/profile/')
        self.assertEqual(page.status_code, 200)
    

    def test_profile_users_correct_template_and_url_name(self):
        page = self.client.get(reverse('profile'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")      
        
    