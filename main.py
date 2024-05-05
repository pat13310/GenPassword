from util.GenPassword import GenPassword, EncryptionMethod

if __name__ == '__main__':
    generator: GenPassword = GenPassword(password="Garcia66240!", length=12)
    # password: str = generator.generate()

    print("Vérification mode de passe", generator.validate())
    print("Sans Cryptage", generator.get_password())
    print(90 * "-")

    print("Méthodes de cryptage")
    generator.encrypt(EncryptionMethod.BCRYPT)
    print("Avec Cryptage ", generator.get_method_encrypt(), generator.get_password(True))

    generator.encrypt(EncryptionMethod.SHA1)
    print("Avec Cryptage ", generator.get_method_encrypt(), generator.get_password(True))

    generator.encrypt(EncryptionMethod.SHA256)
    print("Avec Cryptage ", generator.get_method_encrypt(), generator.get_password(True))

    generator.encrypt(EncryptionMethod.MD5)
    print("Avec Cryptage ", generator.get_method_encrypt(), generator.get_password(True))

    print(90 * "-")
    print("Méthodes de vérification du cryptage")
    generator.encrypt(EncryptionMethod.BCRYPT)
    print("Vérification du cryptage ", generator.get_method_encrypt(), generator.check(generator.get_password(False)))

    generator.encrypt(EncryptionMethod.SHA1)
    print("Vérification du cryptage ", generator.get_method_encrypt(), generator.check(generator.get_password(False)))

    generator.encrypt(EncryptionMethod.SHA256)
    print("Vérification du cryptage ", generator.get_method_encrypt(), generator.check(generator.get_password(False)))

    generator.encrypt(EncryptionMethod.MD5)
    print("Vérification du cryptage ", generator.get_method_encrypt(), generator.check(generator.get_password(False)))
    print(90 * "-")
    print("Méthode de vérification sans cryptage")
    generator.encrypt(EncryptionMethod.NOCRYPT)
    print("Vérification du cryptage ", generator.get_method_encrypt(), generator.validate())


