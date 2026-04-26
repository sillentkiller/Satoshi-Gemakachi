from decimal import Decimal

from satoshi_gemakachi import btc_to_sats, sats_to_btc


def test_btc_to_sats_exact_amount():
    assert btc_to_sats("0.01") == 1_000_000


def test_btc_to_sats_handles_float_precision_edge_case():
    # A common floating-point edge case should still round correctly.
    assert btc_to_sats("0.000000015") == 2


def test_sats_to_btc_round_trip():
    sats = btc_to_sats("1.23456789")
    assert sats == 123_456_789
    assert sats_to_btc(sats) == Decimal("1.23456789")
