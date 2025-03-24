# Análise das Métricas de Qualidade dos Repositórios

## Introdução

Este estudo busca analisar a relação entre diferentes aspectos dos repositórios de software e suas métricas de qualidade. Para isso, foram levantadas algumas hipóteses informais:

- Repositórios populares devem ter melhor qualidade de código, pois recebem mais revisões e colaborações.
- Repositórios mais antigos devem apresentar maior qualidade devido às refatorações ao longo do tempo, embora possam sofrer com código legado.
- Repositórios mais ativos devem ter qualidade superior, pois estão em constante manutenção.
- Repositórios maiores podem ser mais estruturados, mas também podem sofrer com maior complexidade e acoplamento.

## Metodologia

Os repositórios foram analisados com base em métricas extraídas utilizando a ferramenta CK. As seguintes métricas foram coletadas:

- **Popularidade**: Quantidade de estrelas no GitHub.
- **Atividade**: Frequência de commits e releases.
- **Tamanho**: Linhas de código do repositório.
- **CBO (Coupling Between Objects)**: Mede o acoplamento entre classes.
- **DIT (Depth of Inheritance Tree)**: Mede a profundidade da herança.
- **LCOM (Lack of Cohesion of Methods)**: Mede a falta de coesão entre os métodos de uma classe.

A análise estatística foi feita considerando média, mediana e desvio padrão para cada métrica.

## Resultados e Discussão

### RQ01: Qual a relação entre a popularidade dos repositórios e suas características de qualidade?

- **Popularidade**: Média = 9212,99; Mediana = 5627,5; Desvio Padrão = 10953,62
- **CBO**: Média = 5,25; Mediana = 5,20; Desvio Padrão = 1,77
- **DIT**: Média = 1,45; Mediana = 1,39; Desvio Padrão = 0,34
- **LCOM**: Média = 116,79; Mediana = 23,59; Desvio Padrão = 1807,29

**Análise**: A hipótese inicial sugeria que repositórios populares teriam melhor qualidade de código. No entanto, os valores elevados de LCOM sugerem que há falta de coesão, o que pode indicar dificuldades na manutenção.

### RQ02: Qual a relação entre a maturidade dos repositórios e suas características de qualidade?

- **Atividade**: Média = 0,55; Mediana = 0; Desvio Padrão = 3,99
- **CBO**: Média = 5,25; Mediana = 5,20; Desvio Padrão = 1,77
- **DIT**: Média = 1,45; Mediana = 1,39; Desvio Padrão = 0,34
- **LCOM**: Média = 116,79; Mediana = 23,59; Desvio Padrão = 1807,29

**Análise**: Esperava-se que repositórios mais maduros apresentassem melhor qualidade. No entanto, a baixa atividade (mediana = 0) indica que muitos repositórios podem estar inativos, o que pode comprometer a manutenção do código.

### RQ03: Qual a relação entre a atividade dos repositórios e suas características de qualidade?

- **Atividade**: Média = 0,55; Mediana = 0; Desvio Padrão = 3,99
- **CBO**: Média = 5,25; Mediana = 5,20; Desvio Padrão = 1,77
- **DIT**: Média = 1,45; Mediana = 1,39; Desvio Padrão = 0,34
- **LCOM**: Média = 116,79; Mediana = 23,59; Desvio Padrão = 1807,29

**Análise**: Repositórios mais ativos deveriam ter melhor qualidade, mas os valores de acoplamento e coesão sugerem que nem sempre essa relação é direta. A baixa mediana da atividade também sugere que poucos repositórios são realmente ativos.

### RQ04: Qual a relação entre o tamanho dos repositórios e suas características de qualidade?

- **Tamanho**: Média = 74.051,47 linhas de código; Mediana = 14.043,5; Desvio Padrão = 17.931,99
- **CBO**: Média = 5,25; Mediana = 5,20; Desvio Padrão = 1,77
- **DIT**: Média = 1,45; Mediana = 1,39; Desvio Padrão = 0,34
- **LCOM**: Média = 116,79; Mediana = 23,59; Desvio Padrão = 1807,29

**Análise**: A hipótese sugeria que repositórios maiores poderiam apresentar maior complexidade e impactar a manutenção. O alto desvio padrão de LCOM indica grande variação na coesão do código, sugerindo que alguns repositórios grandes podem ser bem estruturados, enquanto outros sofrem com fragmentação. O acoplamento (CBO) e a profundidade da herança (DIT) não variam significativamente, indicando que o tamanho do código não está diretamente associado a maior complexidade estrutural.

## Conclusão

Os resultados mostraram que a relação entre popularidade, atividade, tamanho e qualidade do código não é tão direta quanto se esperava. Em alguns casos, há indícios de que a alta popularidade não implica, necessariamente, em melhor estrutura de código. O estudo sugere que a qualidade do código depende de outros fatores além dos analisados, como a governança do projeto e a revisão de código pelos contribuidores.
