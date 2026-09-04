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


def calcular_custo_ociosidade(percentual_carga, custo_rota):
    """Calcula a parcela do custo da rota perdida por carga insuficiente."""
    carga_minima = CONFIG_NEGOCIO["frota"]["carga_minima_percentual"]

    if percentual_carga >= carga_minima:
        return 0

    percentual_faltante = (carga_minima - percentual_carga) / carga_minima
    return custo_rota * percentual_faltante
