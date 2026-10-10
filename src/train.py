import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import make_pipeline

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'bugsDataset.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'bugClassifier.pkl')

os.makedirs(MODEL_DIR, exist_ok=True)

# 1. Carregar o dataset
print('Carregando os dados...')
df = pd.read_csv(DATA_PATH)

print('\n==== Visão Geral do Dataset ====')
print(f'Total de relatórios: {len(df)}')
print('\nDistribuição por Severidade:')
print(df['severidade'].value_counts())
print('-' * 40)

# 2. Engenharia de Recursos (Feature Engineering):
# Título + Descrição
df['texto_completo'] = df['titulo'] + ' - ' + df['descricao']

X = df['texto_completo']
y = df['severidade']

# 3. Divisão Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Pipeline de PLN + ML
pipeline = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2), max_df=0.7, min_df=2), ComplementNB()
)

# 5. Treinamento
print('\nTreinando o modelo...')
pipeline.fit(X_train, y_train)

# 6. Avaliação
y_pred = pipeline.predict(X_test)
print('\n==== Desempenho do Modelo ====')
print(classification_report(y_test, y_pred, zero_division=0))

# 7. Guardar o modelo treinado em disco (.pkl)
joblib.dump(pipeline, MODEL_PATH)
print(f'Modelo treinado e guardado com sucesso em: {MODEL_PATH}')