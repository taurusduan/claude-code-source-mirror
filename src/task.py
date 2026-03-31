from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PortingTask:
    title: str
    detail: str
    completed: bool = False
