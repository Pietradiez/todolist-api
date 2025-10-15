from flask import jsonify

def buscar_tarefa():
    tarefas = [
            {
                'id':1,
                'nome' : 'Aprender digitação',
                'descrição' : 'Vamos aumentar a zoom para verificar a digitação ',
                'status':"'Pendendte"
            },
            {
                'id': 2,
                'nome': 'Aprender Python',
                'descrição' : 'Aprender a programar apis',
                'status' : 'Pendente'
            }
    ]
    return jsonify(tarefas)

def buscar_tarefas():
     tarefas = {
            
                'id':1,
                'nome' : 'Aprender digitação',
                'descrição' : 'Vamos aumentar a zoom para verificar a digitação ',
                'status':"'Pendendte"
            },
    