# Material revisto e ferramentas da UC

Revisão dos ficheiros fornecidos em 31 de outubro de 2026. Os notebooks foram inspecionados como documentos, sem executar as células. As páginas abaixo são as páginas físicas dos PDFs.

Fonte pública de apoio: [repositório da professora](https://github.com/anacaleiro/Data-Mining-26-27). Os ficheiros locais fornecidos são a base desta revisão.

## Teóricas

| Material | Conteúdo útil | Aplicação ao projeto |
|---|---|---|
| S1 | Enquadramento e projeto em Python | Definir objetivo e justificar os métodos |
| S2 | Contexto de data mining e analytics | Traduzir perguntas de negócio em análise |
| S3 | Representação, tipos de variável, distâncias, escala, dimensionalidade e relevância | Explicar como as escolhas de features alteram a segmentação |
| S4 | Visualização e relações entre variáveis | Produzir gráficos legíveis e investigar redundância |
| S5 | Descritiva, missing, outliers, transformação e encoding | Auditar problemas e justificar os tratamentos |
| S6 | Scaling, seleção de features, PCA e feature engineering | Criar features e preparar escolhas de modelação |
| DM_lab1 | CRISP-DM, entregas e políticas | Organizar o trabalho e cumprir os requisitos |

Referências úteis: S3 pp. 14–17 (distâncias/escala) e 22–23 (tipos); S5 pp. 8–15 (missing/outliers); S6 pp. 3–14 (scaling, relevância e features); DM_lab1 pp. 17–18 (D1), 24 (IA) e 29 (código).

Os S1–S6 incluem fundamentos e referências a clustering, mas não desenvolvem uma aplicação completa e comparação de K-means, hierárquico ou DBSCAN. O syllabus lista matérias futuras; essa lista não demonstra que já tenham sido lecionadas.

S1 contém referências administrativas inconsistentes com as guidelines específicas 2026/2027. Usar as guidelines e atualizações no Moodle para prazos e pesos.

## Práticas

| Notebooks | Técnicas desenvolvidas | Utilidade imediata |
|---|---|---|
| lab00_setup | Verificação de ambiente e imports; exemplos de bibliotecas | Confirmar ambiente de trabalho |
| lab01/lab02_distances | Euclidiana, Manhattan, `cdist`, matrizes e visualização | Entender distâncias e os seus cuidados |
| lab03_data_exploration e solução | Importação, tipos, `describe`, filtragem, agregação, missing e duplicados | Estruturar inventário e auditoria |
| lab04_data_visualization e solução | Histogramas, boxplots, scatter, hexbin, KDE, pairplot e correlações | Explorar distribuições e relações |
| lab05_data_visualization e solução | Categorias, crosstabs, proporções, groupby e comparação por grupos | Comparar planos, equipas e serviços |
| lab06_data_preprocess e solução | Imputação, KNN, IQR, filtros, winsorização, features e redundância | Justificar decisões e medir impacto |
| lab07_data_preprocess | MinMax/Standard scaling e OneHotEncoder | Preparar transformações para clustering |

## Base de código adequada

- Python com `pandas`, `numpy`, `matplotlib` e `seaborn` para a EDA.
- `scipy.spatial.distance` para exemplos de distâncias se forem úteis.
- `sklearn.impute` e `sklearn.preprocessing` para imputação, scaling e encoding, quando justificados.
- Biblioteca standard para caminhos, datas e funções auxiliares.

Não foi encontrada uma lista fechada de bibliotecas autorizadas. A frase que proíbe NumPy/SciPy nos labs01/02 pertence ao exercício específico de calcular uma distância à mão; não estabelece uma proibição geral para o projeto.

`ProfileReport` é auxiliar/opcional. PCA aparece na teoria e é importado no lab07, mas não é desenvolvido aí. MiniSom é importado no setup. Plotly surge como recurso. Nenhum destes factos os torna obrigatórios para o D1.

## Cuidados ao reutilizar exemplos

- Nos labs, `age` representa ano de nascimento; no ACDC representa idade. Não copiar `2024 - age`.
- Os limites manuais usados no dataset das aulas não são limites para o ACDC.
- O projeto é de aprendizagem não supervisionada: não existe um target para justificar seleção supervisionada de features ou SMOTE por rotina.
- Remover todos os outliers de todas as colunas pode apagar os clientes mais interessantes.
- Um comentário para executar uma célula uma única vez deve motivar código mais reproduzível no nosso notebook.
- Categorias, períodos e unidades precisam de interpretação própria antes de calcular razões ou combinar métricas.
