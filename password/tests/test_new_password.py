import string
from password.new_password import generate_password, password_length
import pytest

char_same_streak = 0

def test_password_characters():
	"""Şifre oluşturulurken yalnızca geçerli karakterlerin kullanıldığını test eder"""
	valid_characters = string.ascii_letters + string.digits + string.punctuation
	password = generate_password(password_length)  # Daha güvenli bir doğrulama için uzun bir şifre oluşturuluyor
	for char in password:
		assert char in valid_characters
	assert password_length == len(password)

def test_password_difference():
	password1 = generate_password(password_length)
	password2 = generate_password(password_length)

	for char, char2 in password1, password2:
		if char == char2:
			char_same_streak += 1
	assert char_same_streak != 5
"""
Aşağıda önerilenlerden birini kullanarak başka bir test yazın. Alternatif olarak, kendi testinizi de oluşturabilirsiniz!
Daha fazla test yazabilirseniz harika olur!

1. Şifrenin uzunluğunun belirtilen uzunlukla eşleşip eşleşmediğini test edin  
2. Arka arkaya oluşturulan iki şifrenin farklı olup olmadığını test edin 
"""
 