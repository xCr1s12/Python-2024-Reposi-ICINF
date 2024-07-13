import pandas as pd

# Ejemplo de DataFrame
data = pd.DataFrame({
    'Categoria': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Valor': [10, 20, 15, 25, 30, 35]
})

# Agrupar por la columna 'Categoria'
grupos = data.groupby('Categoria')

# Filtrar por una categoría específica, por ejemplo, 'A'
grupo_A = grupos.get_group('A')

print(grupo_A)