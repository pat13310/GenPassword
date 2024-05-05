## Générateur de mot de passe


### Les fonctions principales de la classe GenPassword :


![Diagramme sans nom drawio](https://github.com/pat13310/GenPassword/assets/122201455/3eea476e-d281-45a7-b4fc-04a50c449d03)

### Exemples d'utilisation :

**Création du mot de passe (manuel)**

generator: GenPassword = GenPassword(password="Motdepasse!", length=10)  
   
**OU**   

generator: GenPassword = GenPassword()
generator.set_length(10)
generator.set_password("Motdepasse!")

> [!TIP]
> La longueur peut être définie en second paramètre du constructeur
***
**Création du mot de passe (automatique)**

generator: GenPassword = GenPassword()

generator.generate()
***

**Encryptage d'un mot de passe**
 
 #encryptage MD5    
 password_encrypt=generator.encrypt(EncryptionMethod.MD5)
 
 #encryptage SHA1  
 password_encrypt=generator.encrypt(EncryptionMethod.SHA1)
 
#encryptage SHA256    
 password_encrypt=generator.encrypt(EncryptionMethod.SHA256)

#encryptage BCRYPT  
password_encrypt=generator.encrypt(EncryptionMethod.BCRYPT)

***
**Vérification d'un mot de passe (non crypté)**

is_validate=generator.validate()
***
**Vérification d'un mot de passe (crypté)**

is_validate=generator.check()
***
**Obtenir le mot de passe (non crypté)**

generator.get_password(False)
***
**Obtenir le mot de passe (crypté)**

generator.get_password(True)
***
### Formulaire du Login

![image](https://github.com/pat13310/GenPassword/assets/122201455/6eddd2b3-65e0-46d4-8691-87cb268b1b81)


### Formulaire du Générateur 

![image](https://github.com/pat13310/GenPassword/assets/122201455/f44b5ab3-e0a6-42ad-a508-84f1bf1f4a46)






