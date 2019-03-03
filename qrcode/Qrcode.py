import pyqrcode

def maker(imc,nome,peso,altura,conc):
    msg = f'''Nome : {nome}
Peso : {peso}
Altura : {altura}
Seu IMC : {imc:.1f}
Resultado do teste : {conc}'''
    q = pyqrcode.create(f'{msg}')
    q.png(f'{nome}.png',scale=6)
    print('QRcode gerado com sucesso')
    return True

if __name__=='__main__':
    qrcode()
