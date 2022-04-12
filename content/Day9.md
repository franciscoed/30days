# st.line_chart

`st.line_chart` permite exibir um gráfico de linhas

This is syntax-sugar around `st.altair_chart`. The main difference is this command uses the data's own column and indices to figure out the chart's spec. As a result this is easier to use for many "just plot this" scenarios, while being less customizable.

If `st.line_chart` does not guess the data specification correctly, try specifying your desired chart using st.altair_chart.

## O que estamos construindo?

Uma aplicação simples para exibir um gráfico de linhas

Fluxo da aplicação:
1. Cria um DataFrame pandas com números gerados aleatoriamente pelo `NumPy`.
2. Cria e mostra um gráfico de linha usando o comando `st.line_chart()`.

## Aplicação de demonstração

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.line_chart/)

## Código
Veja aqui mais informações sobre como usar o [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart):
```python
import streamlit as st
import pandas as pd
import numpy as np

st.header('Gráfico de linhas')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

```

## Explicação linha por linha
A primeira coisa a fazer quando estiver criando uma aplicação Strealit é importar a biblioteca `streamlit` como `st`:
```python
import streamlit as st
import pandas as pd
import numpy as np
```

Na sequência, vamos adicionar um texto de cabeçalho:
```python
st.header('Gráfico de linhas')
```

Agora, nós criamos o Dataframe de 3 colunas com números aleatórios. 
```python
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
```

Finalmente, um gráfico de linhas é criado usando `st.line_chart()` com o DataFrame armazenado na variável `chart_data` como entrada:
```python
st.line_chart(chart_data)
```

## Leitura complementar
Leia mais sobre o comando abaixo, pois o [`st.line_chart`](https://docs.streamlit.io/library/api-reference/charts/st.line_chart) se baseia nele:
- [`st.altair_chart`](https://docs.streamlit.io/library/api-reference/charts/st.altair_chart)
