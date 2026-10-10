import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'bugClassifier.pkl')

# Verificando a existência do modelo antes de carregar ele
if not os.path.exists(MODEL_PATH):
    print("Erro: O modelo ainda não foi treinado. Execute o ficheiro 'train.py' primeiro.")
    exit()

# Carrega o modelo já treinado do sistema após atualização do sistema 
modelo = joblib.load(MODEL_PATH)

# Simulando a receção de um novo bug
novo_bug = [
    'Quero compartilhar a tela pelo anyviewer porém não fica disponível para a outra máquina'
]

# Realiza a predição
resultado = modelo.predict(novo_bug)

print(f'🐛 Bug analisado: "{novo_bug[0]}"')
print(f'🚨 Prioridade/Severidade atribuída: {resultado[0]}')