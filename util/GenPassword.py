import re
import hashlib
import bcrypt
from enum import Enum

import secrets
import string


# Classe d'énumération pour le type de hashage
class EncryptionMethod(Enum):
    SHA256 = "sha256"
    BCRYPT = "bcrypt"
    MD5 = "md5"
    SHA1 = "sha1"
    NOCRYPT = "sans chiffrage"
    AUTO = "auto"


class GenerateMethod(Enum):
    AUTO = "automatic"
    MAN = "manual"


# Class de génération de mot de passe
class GenPassword:
    # Constructeur avec paramètres
    # password : mot de passe
    # length : longueur du mot de passe

    def __init__(self, password: str = "", length: int = 8, method: EncryptionMethod = EncryptionMethod.NOCRYPT):
        self.length = length
        self.password = password
        self.encrypted_password = ""
        self.method = method

    def generate(self, method: GenerateMethod = GenerateMethod.AUTO) -> str:
        # Génération d'un mot de passe par méthode aléatoire
        # dans la variable 'chars' je veux toutes les lettres de l'alphabet (miniscules et majuscules),
        # digits et caractères de ponctuation

        chars = string.ascii_letters + string.digits + string.punctuation
        # J'utilise la fonction 'secrets.choice' pour des raisons de sécurité
        # 'random.choice' n'est pas adaptée pour les opérations de sécurité et cryptographie
        if method == GenerateMethod.AUTO:
            self.password = ''.join(secrets.choice(chars) for _ in range(self.length))

        return self.password

    # validate vérifie si le mot de passe respecte bien les règles
    # Une majuscule, des lettres, des nombres, des caractères de ponctuation.
    def validate(self, password: str = "") -> bool:

        # Verification que le mot de passe correspond bien aux critères :
        # « J'utilise les expressions régulières pour vérifier la validité de mes mots de passe
        if len(password) != 0:
            self.password = password

        if len(self.password) < self.length:
            return False
        if not re.search(r'\d', self.password):
            return False
        if not re.search(r'[A-Z]', self.password):
            return False
        if not re.search(r'[a-z]', self.password):
            return False
        if not re.search(r'[@#$%^&+=!]', self.password):
            return False
        return True

    def encrypt(self, method: EncryptionMethod) -> str:
        self.method = method
        # Encrypte le mot de passe suivant une méthode de hash
        # On récupère de manière lisible avec ma méthode hexdigest
        if method == EncryptionMethod.MD5:
            self.encrypted_password = hashlib.md5(self.password.encode()).hexdigest()
        elif method == EncryptionMethod.SHA1:
            self.encrypted_password = hashlib.sha1(self.password.encode()).hexdigest()
        elif method == EncryptionMethod.SHA256:
            self.encrypted_password = hashlib.sha256(self.password.encode()).hexdigest()
        elif method == EncryptionMethod.BCRYPT:
            self.encrypted_password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt())
        elif method == EncryptionMethod.NOCRYPT:
            self.encrypted_password = self.password
        return self.encrypted_password

    # On vérifie que le mot de passe à vérifier correspond bien à celui qui est crypté
    def check(self, password_to_check: str = "", method: EncryptionMethod = EncryptionMethod.AUTO) -> bool:
        # on part du principe que self.password est un password "hash" donc crypté
        # Sortie: True si le password correspond au hash fait sur le mot de passe à vérifier,
        # sinon False
        if len(password_to_check.strip()) != 0:
            self.password = password_to_check
        # Si la méthode n'est pas redéfinie, on utilise celle de départ
        if method != EncryptionMethod.AUTO:
            self.method = method
        # password_to_check_encode = password_to_check.encode()
        if self.method == EncryptionMethod.BCRYPT:
            return bcrypt.checkpw(self.password.encode(), self.encrypted_password)
        elif self.method == EncryptionMethod.MD5:
            return hashlib.md5(self.password.encode()).hexdigest() == self.encrypted_password
        elif self.method == EncryptionMethod.SHA256:
            return hashlib.sha256(self.password.encode()).hexdigest() == self.encrypted_password
        elif self.method == EncryptionMethod.SHA1:
            return hashlib.sha1(self.password.encode()).hexdigest() == self.encrypted_password
        elif self.method == EncryptionMethod.NOCRYPT:
            return self.validate(self.password)

    # On retourne la methode de cryptage employée
    def get_method_encrypt(self) -> str:
        return str(self.method.value).upper()

    # Définir la longueur du mot de passe
    def set_length(self, length: int) -> None:
        self.length = length

    def get_length(self, ) -> int:
        return self.length

    def set_password(self, password: str) -> None:
        self.password = password

    def get_password(self, bCrypt=False) -> str:
        if bCrypt:
            return self.encrypted_password
        return self.password
