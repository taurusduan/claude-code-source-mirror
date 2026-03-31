from __future__ import annotations

import argparse

from .port_manifest import build_port_manifest
from .query_engine import QueryEnginePort


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Python porting workspace for the Claude Code rewrite effort')
    subparsers = parser.add_subparsers(dest='command', required=True)
    subparsers.add_parser('summary', help='render a Markdown summary of the Python porting workspace')
    subparsers.add_parser('manifest', help='print the current Python workspace manifest')
    list_parser = subparsers.add_parser('subsystems', help='list the current Python modules in the workspace')
    list_parser.add_argument('--limit', type=int, default=16)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    manifest = build_port_manifest()
    if args.command == 'summary':
        print(QueryEnginePort(manifest).render_summary())
        return 0
    if args.command == 'manifest':
        print(manifest.to_markdown())
        return 0
    if args.command == 'subsystems':
        for subsystem in manifest.top_level_modules[: args.limit]:
            print(f'{subsystem.name}	{subsystem.file_count}	{subsystem.notes}')
        return 0
    parser.error(f'unknown command: {args.command}')
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
