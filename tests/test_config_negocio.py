from pathlib import Path
import unittest


class ConfigNegocioTests(unittest.TestCase):
    def test_deve_conter_regras_de_materiais_frota_e_rota(self):
        caminho_configuracao = Path("src/config_negocio.py")

        self.assertTrue(caminho_configuracao.is_file())

        from src.config_negocio import CONFIG_NEGOCIO

        self.assertEqual(
            CONFIG_NEGOCIO["materiais"]["Plástico"]["densidade"],
            0.90,
        )
        self.assertEqual(
            CONFIG_NEGOCIO["materiais"]["Vidro"]["densidade"],
            2.50,
        )
        self.assertEqual(
            CONFIG_NEGOCIO["materiais"]["Metal"]["densidade"],
            7.80,
        )
        self.assertEqual(
            CONFIG_NEGOCIO["frota"]["capacidade_volume_litros"],
            10000,
        )
        self.assertEqual(
            CONFIG_NEGOCIO["frota"]["limite_compliance_percentual"],
            90,
        )
        self.assertEqual(
            CONFIG_NEGOCIO["frota"]["carga_minima_percentual"],
            30,
        )
        self.assertEqual(CONFIG_NEGOCIO["rota"]["custo_km"], 20.50)


if __name__ == "__main__":
    unittest.main()
