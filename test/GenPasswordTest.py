# importing required module
import unittest

from util.GenPassword import EncryptionMethod, GenPassword


# test cases for the functionality
class GenPasswordTest(unittest.TestCase):
    def setUp(self):
        self.gen_password = GenPassword(method=EncryptionMethod.NOCRYPT, length=10)

    def test_generate(self):
        password = self.gen_password.generate()
        self.assertEqual(len(password), 10)

    def test_validate_no_crypt(self):
        password = "Aa@123451565"
        self.assertTrue(self.gen_password.validate(password))

    def test_fail_validate_no_crypt(self):
        password = "12345678"
        self.assertFalse(self.gen_password.validate(password))

    def test_encryption_sha1(self):
        self.gen_password.encrypt(EncryptionMethod.SHA1)
        self.assertTrue(self.gen_password.check(self.gen_password.get_password(False), EncryptionMethod.SHA1))

    def test_encryption_sha256(self):
        self.gen_password.encrypt(EncryptionMethod.SHA256)
        self.assertTrue(self.gen_password.check(self.gen_password.get_password(False), EncryptionMethod.SHA256))

    def test_encryption_md5(self):
        self.gen_password.encrypt(EncryptionMethod.MD5)
        self.assertTrue(self.gen_password.check(self.gen_password.get_password(False), EncryptionMethod.MD5))

    def test_encryption_bcrypt(self):
        self.gen_password.encrypt(EncryptionMethod.BCRYPT)
        self.assertTrue(self.gen_password.check(self.gen_password.get_password(False), EncryptionMethod.BCRYPT))


# running the test
if __name__ == "__main__":
    unittest.main()
