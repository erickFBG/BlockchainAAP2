from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()

# Nesse metodo nos podemos minerar uma cadeia, informando os dados do proprietario, cep, cidade, registro, etc.
@app.route('/mine_block', methods=['POST'])
def mine_block():
    data = request.get_json()
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash,data,original_index=[])
     
    response = {    
        'message': 
                {
                    "owner_name": data['owner_name'],
                    "city": data['city'],
                    "record_number": data['record_number'],
                    "zip_code": data['zip_code']
                },
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
     
    return jsonify(response), 200

# Pensamos em fazer algo mais robusto aqui, criando verificacao com login e mais questoes de seguranca, porem
#  como e apenas um protipo vamos utilizar um grande artificio da mecanica brasileira inventada para arrumar, recuperar ou realizar algo (GAMBIARRA).
# Vamos "minerar" outro bloco e apenas referenciar o index original, o intuito desse endpoint seria atualizar um registro. Assim mantemos
# a integridade da rede, e criamos um atualizacao nos dados, se for preciso alguma verificacao futura, pegamos como base o timestamp, valendo o mais novo.
@app.route('/edit_registry/<index>', methods=['POST'])
def edit_registry(index):
    data = request.get_json()
    original_index = index
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash,data, original_index)
     
    response = {    
        'message': 
                {
                    "owner_name": data['owner_name'],
                    "city": data['city'],
                    "record_number": data['record_number'],
                    "zip_code": data['zip_code']
                },
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'original_index': original_index
    }
     
    return jsonify(response), 200


# Aqui podemos resgatar todos os registros pelo nome do dono,o ideal seria fazer pelo CPF, que e um dado unico para cada pessoa.
@app.route('/get_names/<name>', methods=['GET'])
def get_names(name):
    names_found = []
    chain = blockchain.chain
    for item in chain:
        data = item['data']
        if name == data['owner_name']:
            names_found.append(item)
            return jsonify(names_found)
        else: 
            return jsonify(["No names found"])

# Aqui podemos receber a cadeia intera
@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200
 
# Verificamos se a cadeia e valida
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
     
    if valid:
        response = {'message': 'A cadeia e valida.'}
    else:
        response = {'message': 'A cadeia e invalida.'}
    return jsonify(response), 200

app.run(host = "localhost", port=5000)