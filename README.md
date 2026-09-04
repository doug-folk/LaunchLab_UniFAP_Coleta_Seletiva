# Coleta Seletiva Inteligente — LaunchLab UniFAP

Sistema para apoiar cooperativas de bairros periféricos na definição de
coletas seletivas. A aplicação transforma o peso de plástico, vidro e metal
em volume, compara o resultado com a capacidade do caminhão e sinaliza rotas
com baixa ocupação.

## Objetivo

Reduzir deslocamentos desnecessários, consumo de combustível e emissões
associadas a caminhões que retornam com pouca carga. Os pontos de coleta são
cadastrados em sequência e o sistema prioriza as maiores cargas dentro da
capacidade disponível da frota.

## Estrutura do projeto

```text
LaunchLab_UniFAP_Coleta_Seletiva/
├── .gitignore
├── princ.py
├── src/
│   └── config_negocio.py
├── tests/
│   ├── test_config_negocio.py
│   ├── test_custo_ociosidade.py
│   └── test_princ_config.py
└── README.md
```

## Regras de negócio

O arquivo `src/config_negocio.py` concentra o dicionário `CONFIG_NEGOCIO`, a
fonte única das regras que orientam a operação:

- Densidade de plástico, vidro e metal, usada para calcular o volume ocupado.
- Capacidade de 10.000 L do caminhão.
- Alerta de compliance a partir de 90% de ocupação.
- Carga mínima de 30% para avaliar a ociosidade da rota.
- Custo de R$ 20,50 por quilômetro percorrido.

Quando a ocupação fica abaixo de 30%, o sistema calcula o custo de
ociosidade de forma proporcional ao percentual que falta para alcançar essa
meta. Por exemplo, uma carga de 15% representa 50% desse custo; com 30% ou
mais, o custo de ociosidade é zero.

## Green IT e compliance

A configuração centralizada evita valores duplicados no código e torna as
regras de operação mais fáceis de revisar, auditar e alterar. Essa decisão de
arquitetura aplica governança de TI ao manter densidades, limites e custos em
um único ponto controlado.

O cálculo de volume permite selecionar apenas os pontos que cabem no
caminhão. Já o alerta de ociosidade evidencia o impacto econômico e ambiental
de rotas pouco carregadas, incentivando o agrupamento de coletas antes do
deslocamento. O limite de compliance de 90% alerta a operação antes da
ocupação máxima, contribuindo para uma frota mais segura e previsível.

Essas regras apoiam metas de Green IT ao reduzir viagens improdutivas,
consumo de combustível e emissão de poluentes, sem perder a rastreabilidade
das decisões da frota.

## Como executar

Com Python 3 instalado, execute o programa interativo na raiz do projeto:

```bash
python3 princ.py
```

Para executar os testes automatizados:

```bash
python3 -m unittest discover -s tests -v
```
