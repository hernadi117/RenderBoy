from __future__ import annotations
from Vector3 import Vector3


class Color(Vector3):
    """Container to represent color value of a pixel, as an RGB triplet."""

    @classmethod
    def from_hex(cls, hex_color: str) -> Color:
        """Creates a Color object from a hex-value."""
        return Color(*tuple(int(hex_color[i:i + 2], 16) / 255 for i in (1, 3, 5)))
