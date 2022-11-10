import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_yrittaa_luoda_varaston_jossa_liikaa_tuotetta(self):
        self.varasto = Varasto(10, 11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_konstruktori_yrittaa_luoda_negatiivisen_tuote_varaston(self):
        self.varasto = Varasto(10, -1)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_ottaminen_liikaa_varastosta(self):
        self.varasto.ota_varastosta(1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_yrittaa_poistaa_varastosta(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_yrittaa_lisata_yli_varaston_tilavuuden(self):
        self.varasto.lisaa_varastoon(11)
        #satunnainen muutos
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_pyrkii_lisaamaan_saldoa(self):

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_oikean_merkkijonon_palautus(self):

        self.varasto.lisaa_varastoon(6)
        self.assertAlmostEqual(str(self.varasto), "saldo = 6, vielä tilaa 4")
    

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
