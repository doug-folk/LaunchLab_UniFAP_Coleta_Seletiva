from contextlib import redirect_stdout
from io import StringIO
import unittest

import princ
import src.config_negocio as config_negocio


class CustoOciosidadeTests(unittest.TestCase):
    def obter_calculadora(self):
        calculadora = getattr(
            config_negocio,
            "calcular_custo_ociosidade",
            None,
        )
        self.assertTrue(callable(calculadora))
        return calculadora

    def test_deve_cobrar_o_custo_total_com_carga_vazia(self):
        calculadora = self.obter_calculadora()

        self.assertEqual(calculadora(0, 205.00), 205.00)

    def test_deve_cobrar_metade_do_custo_com_carga_de_quinze_porcento(self):
        calculadora = self.obter_calculadora()

        self.assertEqual(calculadora(15, 205.00), 102.50)

    def test_nao_deve_cobrar_ociosidade_com_carga_minima(self):
        calculadora = self.obter_calculadora()

        self.assertEqual(calculadora(30, 205.00), 0)

    def test_deve_exibir_o_custo_de_ociosidade_no_resumo_da_rota(self):
        saida = StringIO()

        with redirect_stdout(saida):
            princ.mostrar_resultado([], [], 2000, 10)

        self.assertIn("Custo de ociosidade: R$ 68.33", saida.getvalue())


if __name__ == "__main__":
    unittest.main()
