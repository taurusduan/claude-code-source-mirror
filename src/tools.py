from __future__ import annotations

from .models import PortingBacklog, PortingModule

PORTED_TOOLS = (
    PortingModule('port_manifest', 'Inspect the active Python source tree and summarize the current rewrite surface', 'src/port_manifest.py', 'implemented'),
    PortingModule('backlog_models', 'Represent subsystem and backlog metadata as Python dataclasses', 'src/models.py', 'implemented'),
    PortingModule('query_engine', 'Coordinate Python-facing rewrite summaries and reporting', 'src/query_engine.py', 'implemented'),
)


def build_tool_backlog() -> PortingBacklog:
    return PortingBacklog(title='Tool surface', modules=list(PORTED_TOOLS))
