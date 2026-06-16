# ChargeGrid Intelligence – Sprint 2



### Integrantes

Ângelo Malta Reina
Gustavo Mendonça Duarte
Matheus Carpinheiro Moreno
Renan de Castro Albuquerque
Vinícius Souza Ferraz


## Vídeo Demonstrativo
Link do vídeo:



## Kanban
Link do quadro Kanban:
https://app.notion.com/p/347265df85fc808ca61fcae515241da7?v=347265df85fc80c9ad80000cd0841ad6

## Disciplinas
Pensamento Computacional e Automação com Python
Soluções em Energias Renováveis e Sustentáveis

---

## Sobre o Projeto

O ChargeGrid é uma prova de conceito desenvolvida para o GoodWe Challenge da FIAP.

O projeto simula um sistema inteligente de gerenciamento de carregadores para veículos elétricos, permitindo o cadastro de estações de carregamento, gerenciamento de tarifas e simulação de recargas com controle de demanda energética.

A solução busca demonstrar conceitos de:

- Mobilidade elétrica
- Gerenciamento inteligente de demanda
- Tarifação energética
- Interoperabilidade entre carregadores
- Sustentabilidade
- Inteligência Artificial aplicada à distribuição de energia


## Objetivo

Desenvolver uma prova de conceito funcional capaz de simular o funcionamento de uma rede inteligente de carregadores para veículos elétricos.

O sistema permite:

- Cadastrar carregadores
- Editar carregadores
- Configurar tarifas de energia
- Simular recargas
- Aplicar gerenciamento inteligente de demanda em horários de pico
- Registrar histórico de recargas


## Arquitetura da Solução

A aplicação foi desenvolvida em Python utilizando:

- Listas
- Dicionários
- Estruturas condicionais
- Estruturas de repetição
- Funções
- Manipulação de dados em memória

### Estrutura de Dados

#### Carregadores

```python
{
    "nome": "FIAP Paulista",
    "id": "FIAP001",
    "localizacao": "Av. Paulista",
    "potencia": 22,
    "status": "Disponível",
    "conector": "Tipo 2"
}
```

#### Histórico de Recargas

```python
{
    "carregador": "FIAP Paulista",
    "energia": 20,
    "tempo": "0h 54min",
    "custo": 14.00
}
```

---

## Funcionalidades

### Cadastro de Carregadores

Permite cadastrar múltiplos carregadores contendo:

- Nome
- ID
- Localização
- Potência Máxima
- Tipo de Conector


### Edição de Carregadores

Permite alterar:

- Nome
- Localização
- Potência
- Tipo de Conector

A busca é realizada através do ID do carregador.


### Cadastro de Tarifas

Permite definir:

- Tarifa Normal
- Tarifa de Pico


### Simulação de Recarga

O usuário informa:

- Capacidade da bateria do veículo
- Nível atual de carga
- Nível desejado de carga

O sistema calcula:

- Energia consumida
- Tempo estimado de carregamento
- Custo da recarga


### Inteligência Artificial (Simulada)

Durante horários de pico o sistema realiza um gerenciamento inteligente de demanda.

Nesse cenário:

- A potência disponível do carregador é reduzida em 50%
- O objetivo é evitar sobrecarga da rede elétrica
- A ação é exibida ao usuário como decisão automática da IA ChargeGrid

Exemplo:

```text
IA ChargeGrid:
Alta demanda detectada.
Potência reduzida em 50%
para equilibrar a rede.
```


### Histórico de Recargas

Todas as recargas realizadas são armazenadas durante a execução do sistema.

São registrados:

- Carregador utilizado
- Energia consumida
- Tempo de recarga
- Valor pago


## Fluxo do Sistema

```text
Menu Principal
│
├── Iniciar Recarga
│   ├── Escolher carregador
│   ├── Informar bateria
│   ├── Escolher tarifa
│   └── Gerar resumo
│
├── Informações do Carregador
│   ├── Cadastrar
│   ├── Editar
│   ├── Listar
│   ├── Configurar tarifas
│   └── Visualizar tarifas
│
├── Histórico de Recargas
│
└── Encerrar Sistema
```


## Sustentabilidade

O projeto está alinhado aos princípios de sustentabilidade e energias renováveis através de:

- Incentivo ao uso de veículos elétricos
- Otimização da demanda energética
- Redução de picos de consumo
- Melhor distribuição da energia disponível
- Simulação de redes inteligentes de carregamento


## Conceitos Aplicados

- Smart Grid
- Mobilidade Elétrica
- Gestão de Energia
- Eficiência Energética
- Inteligência Artificial
- Tarifação Dinâmica
- Interoperabilidade
- Sustentabilidade
