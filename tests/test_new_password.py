import string
from password.new_password import generate_password

def test_password_characters():
    """Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
    for char in password:
        assert char in valid_characters

"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""
 
def test_default_password_length():
    """Parametre verilmediğinde varsayılan uzunlukta (12) şifre üretilmeli"""
    password = generate_password()
    assert len(password) == 12

def test_invalid_length_zero():
    """Uzunluk 0 verildiğinde boş string dönmeli"""
    password = generate_password(0)
    assert password == ''

def test_invalid_length_negative():
    """Negatif uzunluk verildiğinde boş string dönmeli"""
    password = generate_password(-5)
    assert password == ''

def test_different_passwords():
    """Arka arkaya oluşturulan iki şifre farklı olmalı"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

def test_specified_password_length():
    """Belirtilen uzunlukta şifre üretilmeli"""
    lengths_to_test = [8, 16, 24, 32]
    for length in lengths_to_test:
        password = generate_password(length)
        assert len(password) == length

def test_password_length_edge_case():
    """Çok büyük bir uzunluk verildiğinde şifre doğru uzunlukta üretilmeli"""
    large_length = 1000
    password = generate_password(large_length)
    assert len(password) == large_length    

def test_password_length_edge_case():
    """Çok büyük bir uzunluk verildiğinde şifre doğru uzunlukta üretilmeli"""
    large_length = 1000
    password = generate_password(large_length)
    assert len(password) == large_length