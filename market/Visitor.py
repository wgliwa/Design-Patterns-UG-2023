from __future__ import annotations

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Visitor(ABC):

    @abstractmethod
    def visit_bank(self, element) -> None:
        pass

    @abstractmethod
    def visit_buyer(self, element) -> None:
        pass

    @abstractmethod
    def visit_seller(self, element) -> None:
        pass


class ConcreteVisitor(Visitor):
    def visit_bank(self, element) -> None:
        element.next()

    def visit_seller(self, element) -> None:
        element.next()

    def visit_buyer(self, element) -> None:
        element.next()
