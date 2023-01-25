from __future__ import annotations
from typing import Generator
import numbers
import numpy as np


class Vector3:
    """A 3-dimensional vector container."""

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        :param x: X-coordinate.
        :param y: Y-coordinate.
        :param z: Z-coordinate.
        """
        self.x, self.y, self.z = x, y, z

    def dot(self, other: Vector3) -> float:
        """Computes the standard dot product of the two vectors."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def norm(self) -> float:
        """Returns the Euclidean norm of the vector."""
        return np.sqrt(self.dot(self))

    def components(self) -> tuple[float, float, float]:
        return self.x, self.y, self.z

    def normalize(self) -> Vector3:
        """Normalizes the vector, effectively turning it into a unit vector."""
        norm = self.norm()
        return self * (1.0 / np.where((norm == 0), 1, norm))

    def __add__(self, other: Vector3) -> Vector3:
        """Operator overloading for the class so two vectors can be added with the + operator."""
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3) -> Vector3:
        """Operator overloading for the class so two vectors can be subtracted with the - operator."""
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> Vector3:
        """Operator overloading for the class so scalar-vector multiplication can be done with the * operator."""
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: float):
        """Operator overloading such that scalar-vector multiplication is associative."""
        return self.__mul__(other)

    def __truediv__(self, other: float) -> Vector3:
        """Operator overloading for the class so scalar-vector division can be done with the / operator."""
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __str__(self) -> str:
        """Returns a string representation of the vector."""
        return f"({', '.join(str(component) for component in self)})"

    def __repr__(self) -> str:
        """Returns a string of the object creation of the vector, such that it may be readily reproduced."""
        return f"Vector3({', '.join(str(component) for component in self)})"

    def __iter__(self) -> Generator[float, None, None]:
        """Returns a generator that yields the elements of the vector in standard order."""
        for element in self.components():
            yield element

    def __eq__(self, other: Vector3) -> bool:
        """Tests element-wise equality of two vectors."""
        return all(False for elem1, elem2, in zip(self, other) if elem1 != elem2)

    def __ne__(self, other):
        """Tests element-wise inequality of two vectors."""
        return not self.__eq__(other)

    def extract(self, mask):
        """Extracts elements from the container as specified in the provided mask."""
        return Vector3(extract(mask, self.x), extract(mask, self.y), extract(mask, self.z))

    def place(self, mask):
        """Inserts element into the container as specified in the provided mask."""
        temp = Vector3(np.zeros(mask.shape), np.zeros(mask.shape), np.zeros(mask.shape))
        np.place(temp.x, mask, self.x), np.place(temp.y, mask, self.y), np.place(temp.z, mask, self.z)
        return temp


def extract(mask, x):
    if isinstance(x, numbers.Number):
        return x
    else:
        return np.extract(mask, x)
