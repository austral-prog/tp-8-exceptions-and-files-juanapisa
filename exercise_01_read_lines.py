import io
import os
import sys
import unittest

from exercise_03_sales_by_product import process_sales, read_sales


class TestReadSales(unittest.TestCase):

    def setUp(self):
        self.filename = "test_tp8_03_tmp.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def _write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)

    def test_ejemplo_basico(self):
        self._write("producto1:100;producto2:200;producto1:150;producto3:50;producto2:100;")
        self.assertEqual(
            {
                "producto1": [100.0, 150.0],
                "producto2": [200.0, 100.0],
                "producto3": [50.0],
            },
            read_sales(self.filename),
        )

    def test_un_solo_producto(self):
        self._write("producto1:10;producto1:20;producto1:30;")
        self.assertEqual({"producto1": [10.0, 20.0, 30.0]}, read_sales(self.filename))

    def test_valores_son_float(self):
        self._write("a:5;b:7;")
        data = read_sales(self.filename)
        self.assertIsInstance(data["a"][0], float)
        self.assertIsInstance(data["b"][0], float)

    def test_sin_punto_y_coma_final(self):
        self._write("a:1;b:2")
        self.assertEqual({"a": [1.0], "b": [2.0]}, read_sales(self.filename))

    def test_archivo_no_existe(self):
        with self.assertRaises(FileNotFoundError):
            read_sales("archivo_que_no_existe_tp8_03.txt")


class TestProcessSales(unittest.TestCase):

    def _capture(self, data):
        buf = io.StringIO()
        sys.stdout = buf
        try:
            process_sales(data)
        finally:
            sys.stdout = sys.__stdout__
        return buf.getvalue()

    def test_formato_y_orden(self):
        data = {
            "producto1": [100.0, 150.0],
            "producto2": [200.0, 100.0],
            "producto3": [50.0],
        }
        output = self._capture(data)
        lines = output.strip().split("\n")
        self.assertEqual("producto1: ventas totales $250.00, promedio $125.00", lines[0])
        self.assertEqual("producto2: ventas totales $300.00, promedio $150.00", lines[1])
        self.assertEqual("producto3: ventas totales $50.00, promedio $50.00", lines[2])

    def test_dos_decimales(self):
        # Promedios con decimales para verificar formato
        data = {"a": [1.0, 2.0, 2.0]}
        output = self._capture(data)
        self.assertIn("ventas totales $5.00", output)
        self.assertIn("promedio $1.67", output)

    def test_producto_unico(self):
        data = {"solo": [10.0]}
        output = self._capture(data).strip()
        self.assertEqual("solo: ventas totales $10.00, promedio $10.00", output)


if __name__ == "__main__":
    unittest.main()
