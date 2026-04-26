# Satoshi Gemakachi

Small utilities for handling Bitcoin amount conversions safely.

## Why this matters

A common bug in money-related code is using binary floating-point arithmetic
for currency conversion. This project provides conversion helpers that use
`Decimal` to avoid precision issues.
