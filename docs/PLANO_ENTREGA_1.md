# Plano da entrega intermédia

Planeamento elaborado em 31 de outubro de 2026. Fonte principal: `DM2627_ProjectGuidelines.pdf`, atualizado em 2 de setembro de 2026. Confirmar no Moodle alterações, hora limite e marcação da discussão.

## O que é obrigatório

Entrega em **4 de novembro de 2026**, com **20 pontos** (guidelines, pp. 2–3):

- Notebook `GroupXX_EDA_Code.ipynb`: 5 pontos.
- Slides `GroupXX_EDA_Slides.pdf`: 15 pontos.
- Slides com 3–5 páginas de conteúdo, excluindo capa.
- Código executado, outputs visíveis, secções Markdown e execução sem erros num ambiente novo.
- Discussão de grupo de 10–15 minutos, provisoriamente de 9 a 13 de novembro, a confirmar no Moodle (p. 4). A modalidade não é especificada.

O objetivo é conhecer os membros da ACDC, identificar problemas que afetem as distâncias e o clustering, criar features úteis e apresentar hipóteses de segmentação sustentadas pela exploração.

O D1 não exige uma solução final de clusters. As decisões de preparação podem ainda ser revistas na fase seguinte; já nesta fase precisamos de documentar e justificar o que fizermos.

## Sequência do notebook

### 1. Contexto e perguntas de negócio

- Explicar quem é a ACDC e por que pretende segmentar membros.
- Formular perguntas sobre valor económico, intensidade de utilização e serviços usados.
- Definir a unidade de observação e discutir contas individuais e de equipa.
- Confirmar o significado e o período de referência das variáveis no dicionário.

### 2. Importação e inventário

- Ler o CSV com `sep=";"`, preservar `df_raw` e trabalhar numa cópia.
- Mostrar dimensões, tipos, identificador, exemplos e estatísticas iniciais.
- Separar conceptualmente identificador, datas, categorias, binárias e métricas numéricas.
- Converter números monetários e datas com regras explícitas para os formatos presentes.

### 3. Qualidade dos dados e decisões

- Quantificar missing values e possíveis códigos sentinela, sem assumir que zero significa ausência.
- Confirmar as linhas repetidas e documentar a eventual remoção.
- Uniformizar categorias com mapeamentos visíveis e justificáveis.
- Investigar contagens negativas, idades suspeitas, dias de plano e coerência temporal.
- Investigar `membership_end = 1970-01-01` antes de inferir estado ativo ou duração.
- Analisar a referência de `days_since_last_visit` antes de usar recência como variável comparável.
- Distinguir erros de extremos plausíveis; não aplicar IQR para excluir automaticamente todos os membros premium.
- Registar por decisão: problema, evidência, tratamento, número de linhas afetadas e impacto.

### 4. Exploração e relações

- Distribuições, missingness, histogramas e boxplots das métricas relevantes.
- Frequências e proporções por plano e tipo de conta.
- Comparações de uso/valor entre categorias, com tamanho dos grupos visível.
- Scatterplots e correlações para investigar associações e redundância.
- Separar acumulação por duração/intensidade de diferenças de comportamento.
- Usar os gráficos para sustentar conclusões específicas, com unidades e períodos claros.

### 5. Feature engineering

Criar poucas features defensáveis, verificar os seus resultados e explicar a sua utilidade. Candidatas a avaliar:

| Feature candidata | Utilidade possível | Verificação necessária |
|---|---|---|
| Utilização no último período: visitas reais / visitas permitidas | Comparar utilização com o direito de acesso | Denominador positivo; investigar valores superiores a 1 |
| Duração observada da membership | Contextualizar métricas acumuladas | Datas e sentinelas; confirmar que início/fim descrevem o mesmo intervalo |
| Receita por mês observado | Separar duração de valor económico | Parse do valor monetário, duração positiva e períodos comparáveis |
| Número de add-ons usados | Medir diversidade de serviços | Normalizar booleanos; distinguir diversidade de intensidade |
| Intensidade de serviços por unidade de tempo | Comparar uso de extras | Confirmar que as horas/contagens e a duração cobrem o mesmo período |

Recência já existe no CSV, por isso explorar essa coluna não é, por si só, criar uma feature nova. Não combinar contagens e horas numa soma sem significado de negócio.

### 6. Implicações para clustering

- Propor perspetivas de valor e comportamento a partir das variáveis realmente disponíveis.
- Identificar features relevantes e redundantes por perspetiva.
- Explicar como escala, encoding, missingness e outliers poderão afetar as distâncias.
- Formular perfis esperados e uma hipótese fundamentada de número de grupos, sujeita a validação.
- Não escolher arbitrariamente 3 ou 4 clusters antes de observar evidência.
- Identificar decisões em aberto para a fase de modelação.

## Estrutura proposta para os slides

Proposta de cinco slides de conteúdo, a preencher com resultados revistos pelo grupo:

1. Pergunta de negócio e retrato dos dados.
2. Problemas de qualidade mais importantes, tratamentos e consequências.
3. Padrões de comportamento/valor mais informativos, com evidência visual.
4. Features criadas e o que acrescentam à futura segmentação.
5. Hipóteses de segmentos, número esperado de grupos, limitações e próximos testes.

Esta organização é uma proposta, não uma estrutura imposta pelas guidelines. Privilegiar interpretações sobre descrições ou listas de tarefas.

## Calendário proposto até à entrega

| Data | Trabalho principal | Resultado verificável |
|---|---|---|
| 31 out. | Compreender requisitos, dados e problemas | Plano, inventário e lista de decisões |
| 1 nov. | Desenvolver auditoria e tratamentos justificados | Notebook de qualidade reproduzível |
| 2 nov. | Exploração, features e interpretações | Gráficos e evidências para as hipóteses |
| 3 nov. | Rever notebook e preparar slides | Executar do início, corrigir e ensaiar explicações |
| 4 nov. | Verificação e submissão | Ficheiros com nomes corretos, dentro da hora do Moodle |

Plano indicativo: a disponibilidade do grupo e os problemas encontrados determinam o esforço. Evitar comprometer o obrigatório com bónus nesta fase.

## Verificação antes de entregar

- [ ] Número de grupo e inscrição de todos no Moodle confirmados.
- [ ] Notebook executa integralmente num kernel novo e mostra outputs.
- [ ] Dependências e caminho dos dados documentados.
- [ ] Decisões de qualidade fundamentadas e impacto quantificado.
- [ ] Features novas desenvolvidas e verificadas.
- [ ] Insights sustentados em gráficos/tabelas e revistos pelo grupo.
- [ ] Hipóteses de segmentos identificadas como hipóteses.
- [ ] Slides com 3–5 páginas de conteúdo e nomes corretos.
- [ ] Apoio de IA registado de forma fiel; verificar a forma de declaração aplicável à entrega.
- [ ] Todos conseguem explicar as decisões e os resultados apresentados.

## Fases seguintes

O D2 está previsto para **3 de janeiro de 2027**, com notebook e relatório até 10 páginas de conteúdo: 60 pontos. Exige perspetivas justificadas, pelo menos duas abordagens de clustering por perspetiva, comparação e uma segmentação final integrada (guidelines, pp. 5–6).

O relatório final tem anexos obrigatórios de uso de IA, contribuições e responsabilidade. O D3 é uma discussão individual presencial em janeiro, com data a anunciar, valendo 20 pontos (p. 2).
