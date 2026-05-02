# Problemas Identificados — Leitura Inicial do Código

Este arquivo é preenchido pelos estudantes na Aula 1 após a leitura do código legado.
Descreva em linguagem livre tudo que parecer estranho, errado ou difícil de entender.
Não é necessário usar termos técnicos neste momento.

---

## Minha leitura inicial

Exemplo de entradas:
- "A classe faz muita coisa ao mesmo tempo"
- "Tem código de e-mail misturado com o cálculo de multa"
- "O mesmo cálculo aparece duas vezes no código"
- "As listas de equipamentos estão fora da classe, soltas no arquivo"

- O sistema depende da data atual do computador para calcular atraso e multa.Isso dificulta testar o sistema, porque o resultado muda dependendo do dia em que o código é executado.
- As funções usam print diretamente para mostrar resultados. Isso mistura a lógica com a exibição e impede reaproveitar os dados em outros contextos (como uma interface gráfica ou teste automatizado).
- O método registrar retorna True ou False, mas os outros métodos não seguem um padrão de retorno. Isso deixa o comportamento inconsistente e dificulta prever como usar cada função.
- Não há validação adequada dos dados de entrada. Por exemplo, é possível passar dias negativos ou valores inválidos sem tratamento claro no sistema.
- O sistema percorre listas inteiras para buscar dados toda vez (busca linear). Isso pode funcionar com poucos dados, mas fica ineficiente se a quantidade de equipamentos ou empréstimos crescer.
 
---

## Revisão com vocabulário técnico

*(Este espaço será preenchido após a Aula 4, quando os termos técnicos corretos forem aprendidos)*
