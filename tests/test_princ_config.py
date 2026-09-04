import unittest

import princ
from src.config_negocio import CONFIG_NEGOCIO


class PrincConfigTests(unittest.TestCase):
    def test_deve_usar_custo_da_configuracao_centralizada(self):
        custo_original = CONFIG_NEGOCIO["rota"]["custo_km"]
        CONFIG_NEGOCIO["rota"]["custo_km"] = 12.50

        try:
            self.assertEqual(princ.calcular_custo_rota(4), 50.0)
        finally:
            CONFIG_NEGOCIO["rota"]["custo_km"] = custo_original


if __name__ == "__main__":
    unittest.main()
