## Générateur de mot de passe


### Les fonctions principales de la classe GenPassword :


<image src="https://github.com/pat13310/GenPassword/assets/122201455/3eea476e-d281-45a7-b4fc-04a50c449d03" width="200" height='600'></image>

### Exemples d'utilisation :

**Création du mot de passe (manuel)**
```python

generator: GenPassword = GenPassword(password="Motdepasse!", length=10)  
```
   
**Ou**   
```python
generator: GenPassword = GenPassword()     
generator.set_length(10)   
generator.set_password("Motdepasse!")   
```
> [!TIP]
> La longueur peut être définie en second paramètre du constructeur
***
**Création du mot de passe (automatique)**
```python
generator: GenPassword = GenPassword()

generator.generate()
```

***

**Encryptage d'un mot de passe**
```python
 
 #encryptage MD5    
 password_encrypt=generator.encrypt(EncryptionMethod.MD5)
 
 #encryptage SHA1  
 password_encrypt=generator.encrypt(EncryptionMethod.SHA1)
 
#encryptage SHA256    
 password_encrypt=generator.encrypt(EncryptionMethod.SHA256)

#encryptage BCRYPT  
password_encrypt=generator.encrypt(EncryptionMethod.BCRYPT)
```

***
**Vérification d'un mot de passe (non crypté)**
```python

is_validate=generator.validate()
***
**Vérification d'un mot de passe (crypté)**

is_validate=generator.check(generator.get_password(False))  
```

**Ou**   
```python

is_validate=generator.check()
```

***
**Obtenir le mot de passe (non crypté)**
```python

password=generator.get_password(False)
```

***
**Obtenir le mot de passe (crypté)**
```python

password=generator.get_password(True)
```

***
**Définir le mot de passe (non crypté)**
```python

password=generator.set_password("Motdepasse!")
```

***
**Définir la longueur du mot de passe (non crypté)**
```

password=generator.set_length(10)
```

***
### Formulaire du Login

<image src="https://github.com/pat13310/GenPassword/assets/122201455/6eddd2b3-65e0-46d4-8691-87cb268b1b81" width="300"></image>


### Formulaire du Générateur 

<image src="https://github.com/pat13310/GenPassword/assets/122201455/f44b5ab3-e0a6-42ad-a508-84f1bf1f4a46" width="300"></image>






