# Auditoria inicial do CSV

Inspeção preliminar em 31 de outubro de 2026. São contagens sobre o ficheiro original, incluindo duplicados, antes de tratamentos. Esta nota orienta o trabalho; não é a EDA final nem fixa decisões de limpeza.

Fonte: `acdc_dataset.csv`, SHA-256 `879ff74a85594730e323caa6bbbe87dc654ed93cdc391c1f484a18fee1eff404`.

## Estrutura verificada

- 15.465 linhas e 31 colunas; separador `;`.
- 15 linhas integralmente repetidas e 15 ocorrências adicionais de identificadores repetidos.
- Datas em `YYYY-MM-DD` e `DD/MM/YYYY`. Considerando estes dois formatos, as três colunas de datas são interpretáveis; os formatos diferentes não são, por si, datas corrompidas.
- `lifetime_value` inclui valores com formatação monetária e separadores de milhares: 401 valores não vazios falham numa conversão simples com `float` e precisam de parsing adequado.
- Binárias surgem como `True`/`False`, enquanto `uses_print` usa `0`/`1`.

## Valores vazios

Contagem de campos vazios, sem ainda classificar categorias como `Unknown` como missing:

| Coluna | Vazios |
|---|---:|
| `age` | 558 |
| `gender` | 530 |
| `country` | 430 |
| `plan_tier` | 105 |
| `meeting_room_hours` | 1.298 |
| `guest_passes_issued` | 1.271 |
| `lifetime_value` | 1.040 |

As restantes colunas não têm campos vazios. Isso não garante ausência de erros ou de códigos sentinela.

## Questões concretas a investigar

| Evidência no original | Implicação para a análise |
|---|---|
| 3.956 finais de membership iguais a `1970-01-01` | Possível sentinela; não calcular duração diretamente nem assumir automaticamente estado ativo |
| 152 finais anteriores ao início, excluindo `1970` | Investigar coerência temporal; alguns casos podem depender da definição de primeiro início/fim |
| 94 últimas entradas anteriores ao início | Investigar erro temporal ou significado dos campos |
| 56 recências negativas | A recência precisa de validação antes de entrar nas distâncias |
| Em 9.914 linhas, recência = fim da membership − última entrada | A referência temporal pode variar; não assumir uma única data de extração sem evidência |
| Idades de 1 a 149 | Rever plausibilidade; um limite adulto não deve ser aplicado sem justificação |
| 566 contagens negativas de colegas | Distinguir erro de código sentinela antes de tratar |
| 42 valores negativos de visitas totais e 66 de renovações | Quantificar origem e justificar tratamento |
| 16 horas de reunião, 8 horas de eventos e 7 contagens de passes negativas | Investigar inconsistências e preservar registo do tratamento |
| 43 planos com zero dias/semana e 54 acima de sete | Verificar limites e semântica dos planos |
| 10 direitos de visita iguais a zero | Evitar divisão por zero na taxa de utilização |
| 8 casos com visitas reais superiores às permitidas | Investigar uso extra/erro; não cortar automaticamente a taxa em 1 |
| Variações como `HOT_DESK`, `Hot Desk`, `hotdesk` | Normalizar categorias antes de comparar perfis |
| Países e indústrias com abreviaturas, espaços e variantes | Construir mapeamentos explícitos, preservando o original |

Valores extremos e negativos em receita precisam de parsing e análise de contexto antes de decisões. Uma observação extrema não é automaticamente erro.

## Colunas e features

As 31 colunas reais correspondem ao dicionário do dataset nas guidelines. Qualquer alegação adicional deve ser verificada contra `df.columns`, não aceite apenas porque aparece em texto num PDF.

As prioridades são a coerência temporal, o parsing monetário, as categorias e a distinção entre intensidade de uso e acumulação por duração. As features candidatas e as dependências estão no [plano](PLANO_ENTREGA_1.md).

O diagnóstico foi feito sem modificar o CSV. As contagens serão reproduzidas no notebook e revistas depois dos tratamentos.
