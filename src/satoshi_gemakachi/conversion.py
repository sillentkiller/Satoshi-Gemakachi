"""Conversion helpers for BTC/satoshi amounts.

These helpers intentionally avoid binary floating-point arithmetic to prevent
rounding bugs in financial calculations.
"""

from decimal import Decimal, ROUND_HALF_UP

SATOSHIS_PER_BTC = Decimal("100000000")


def btc_to_sats(amount_btc: str | Decimal) -> int:
    """Convert a BTC amount into integer satoshis.

    The value is rounded to the nearest satoshi using half-up rules.
    """

    btc_decimal = Decimal(str(amount_btc))
    sats_decimal = (btc_decimal * SATOSHIS_PER_BTC).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )
    return int(sats_decimal)


def sats_to_btc(amount_sats: int) -> Decimal:
    """Convert integer satoshis into a BTC amount."""

    return Decimal(amount_sats) / SATOSHIS_PER_BTC
