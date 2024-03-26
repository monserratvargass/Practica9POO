import random
import string


class EnigmaMachine:
    """ Atributos:
    rotores (rotores de la maquina)
    rflector: el reflector usado por la maquina
    
    metodos:
    rotate, rota todos los rotores 1 paso 
    substitute, sustituye un caracter"""
    def __init__(self, rotors, reflector):
        self.rotors=rotors
        self.reflector=reflector
    
    def rotate_rotors(self):
        """rota los rotores 1 paso"""
        for rotor in self.rotors:
            rotor.rotate()
            
    def substitute(self,letter):
        """realiza la sustitucion de un solo caracter a travez de los rotores y el reflector
        Args:
        - Letter es esl caracter a sustituir
        returns:
        regresa el caracter sustituido"""
        for rotor in self.rotors:
            letter=rotor.substitute_backward(letter)
        letter=self.reflector.substitute(letter)
        for rotor in reversed(self.rotors):
            letter=rotor.substitute_backward(letter)
        return letter
    
class Rotor:
    """ Representa el rotor de la maquina enigma
    atributos:
    wiring, el cableado del rotor
    position, la posicion
    notch, la posicion muesca del rotor
    
    metodos
    rotate, rota el rotor 1 paso
    substitute_forward, sustituye hacia adelante
    substitute_backward,sustituye hacia atrás"""
    
    def __init__(self,wiring,notch):
        self.wiring=wiring
        self.position=0
        self.notch=notch
        
    def rotate(self):
        self.position=(self.position -1)%26
        
    def substitute_forward(self,letter):
        """realiza la sustiotucion hacia adelante
        args
        letter, el caracter a sustituir
        
        returns
        str el caracter sustituido"""
        return self.wiring[(ord(letter)-ord('A')+self.position)%26]
    
    def substitute_backward(self,letter):
        """Realiza la sustitucion hacia atras por el rotor"""
        return chr((self.wiring.index(letter)-self.position+26)%26+ord('A'))
    
class Reflector:
    """Reflector de la maquina"""
    def __init__(self,wiring):
        self.wiring=wiring
            
    def substitute(self,letter):
        return self.wiring[ord(letter)-ord('A')]
        
def generate_random_wiring():
        alphabet=list(string.ascii_uppercase)
        #random.shuffle(alphabet)
        return ''.join(alphabet)
    
def main():
        #Configuración inicial
    rotor1 = Rotor(generate_random_wiring(),'Q')
    rotor2 = Rotor(generate_random_wiring(),'E')
    rotor3 = Rotor(generate_random_wiring(),'V')
    reflector = Reflector(generate_random_wiring())
        
        #creacion de la maquina enigma
    enigma=EnigmaMachine([rotor1,rotor2,rotor3],reflector)
        
        #mensaje de prueba
    plaintext=""
    ciphertext="CNORGWAOR"
        
        #cifrado del mensaje
    for letter in plaintext:
        if letter.isalpha():
            enigma.rotate_rotors()
            encrypted_letter=enigma.substitute(letter)
            ciphertext +=encrypted_letter
        else:
            ciphertext +=letter
                
        #Impresion del resultado
    print("Plaintext",plaintext)
    print("ciphertext",ciphertext)
        
if __name__=="__main__":
    main()