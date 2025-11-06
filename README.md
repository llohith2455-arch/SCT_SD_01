# 🌡️ Temperature Converter

A small command-line tool to convert temperatures between Celsius, Fahrenheit, and Kelvin. See the implementation in [temp.py](temp.py).

## Overview
- Interactive prompt that asks for the source scale, target scale, and temperature value.
- Supports conversions between:
  - [`celsius_to_fahrenheit`](temp.py)
  - [`celsius_to_kelvin`](temp.py)
  - [`fahrenheit_to_celsius`](temp.py)
  - [`fahrenheit_to_kelvin`](temp.py)
  - [`kelvin_to_celsius`](temp.py)
  - [`kelvin_to_fahrenheit`](temp.py)
- Core logic in [`convert_temperature`](temp.py) and entrypoint in [`main`](temp.py).

## Scales (input options)
- 1 — Celsius
- 2 — Fahrenheit
- 3 — Kelvin

## Usage
Run the script and follow prompts:

```sh
python temp.py
```

Enter the source scale number, target scale number, and the temperature value when prompted. The script prints the converted temperature.

## Files
- [temp.py](temp.py) — conversion functions and CLI entrypoint
