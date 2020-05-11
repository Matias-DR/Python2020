#Alumno: Diz Rendani, Matias. Legajo: 17149/0. Turno: tarde.

import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import os

def menu():
	sg.theme('DarkAmber')
	es=[
		[sg.Text('Nombre de usuario: ', visible=False, key='t1')],
		[sg.InputText(visible=False, size=(17,1), key='user')],
		[sg.Button('Aceptar', size=(17,1), visible=False, key='b4')],
		[sg.Text('Elegí a qué juego jugar', key='t0')],
		[sg.Button('Ahorcado', size=(17,1), key='b0')],
		[sg.Button('TA-TE-TI', size=(17,1), key='b1')],
		[sg.Button('Otello', size=(17,1), key='b2')],
		[sg.Button('Salir', size=(17,1), key='b3')]
	]
	w=sg.Window('A no, tremendo.', es)
	opciones={'b0': 1, 'b1': 2, 'b2': 3}
	juego={'opcion': 0, 'usuario': ''}
	while True:
		e, v=w.read()
		if e in (None, 'b3'):
			juego['opcion']=0
			break
		if e in ('b0', 'b1', 'b2'):
			juego['opcion']=opciones[e]
			w.Element('t0').Update(visible=False)
			w.Element('b0').Update(visible=False)
			w.Element('b1').Update(visible=False)
			w.Element('b2').Update(visible=False)
			w.Element('b3').Update(visible=False)
			w.Element('t1').Update(visible=True)
			w.Element('user').Update(visible=True)
			w.Element('b4').Update(visible=True)
		if e=='b4':
			juego['usuario']=v['user']
			break
	w.close()
	return juego

def main(args):
	opciones={1: 'Ahorcado', 2: 'TA-TE-TI', 3: 'Otello'}
	while True:
		datos=menu()
		os.system('cls')
		opcion = datos['opcion']
		if opcion!=0:
			ar=open('user(_)data.JSON', 'a')
			ar.write('El usuario \'{}\' jugo: {}\n'.format(str(datos['usuario']), opciones[opcion]))
			ar.close()
		if opcion == 1:
			hangman.main()
		elif opcion == 2:
			tictactoeModificado.main()
		elif opcion == 3:
			reversegam.main()
		elif opcion == 0:
			break

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))