"""Regras de negócio centralizadas para a coleta seletiva."""

CONFIG_NEGOCIO = {
    "materiais": {
        "Plástico": {"densidade": 0.90},
        "Vidro": {"densidade": 2.50},
        "Metal": {"densidade": 7.80},
    },
    "frota": {
        "capacidade_volume_litros": 10000,
        "limite_compliance_percentual": 90,
        "carga_minima_percentual": 30,
    },
    "rota": {
        "custo_km": 20.50,
    },
}
