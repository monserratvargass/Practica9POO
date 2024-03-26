import base64

class EnigmaMachine:
    def __init__(self, rotor_settings):
        self.rotor_settings = rotor_settings

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            encrypted_char = self.encrypt_char(char)
            encrypted_message += encrypted_char
        return base64.b64encode(encrypted_message.encode()).decode()

    def decrypt(self, encrypted_message):
        decrypted_message = base64.b64decode(encrypted_message).decode()
        original_message = ""
        for char in decrypted_message:
            decrypted_char = self.decrypt_char(char)
            original_message += decrypted_char
        return original_message

    def encrypt_char(self, char):
        # Lógica de encriptación aquí
        # Implementa la lógica de encriptación de la máquina Enigma con los rotores y configuraciones específicas
        # Puedes modificar esta función según las especificaciones de la máquina Enigma que estés simulando
        # Por ahora, simplemente devolvemos el carácter original
        return char

    def decrypt_char(self, char):
        # Lógica de desencriptación aquí
        # Implementa la lógica de desencriptación de la máquina Enigma con los rotores y configuraciones específicas
        # Puedes modificar esta función según las especificaciones de la máquina Enigma que estés simulando
        # Por ahora, simplemente devolvemos el carácter original
        return char

# Configuración inicial de los rotores (puedes ajustar según sea necesario)
rotor_settings = "ABC"

# Crear una instancia de la máquina Enigma
enigma_machine = EnigmaMachine(rotor_settings)

# Mensaje a encriptar
mensaje_original = "Chilaquil"

# Encriptar el mensaje
mensaje_encriptado = enigma_machine.encrypt(mensaje_original)
print("Mensaje original:", mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)

# Desencriptar el mensaje
mensaje_desencriptado = enigma_machine.decrypt(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)