from __future__ import annotations
import os
import sys

import networkx as nx
import rich_click as click
import woke.ir as ir
import woke.ir.types as types
import rich
from rich import print
import pdbr
import ipdb
from woke.printers import Printer, printer



def custom_excepthook(exc_type, exc_value, exc_traceback):
    pdbr.post_mortem(exc_traceback, exc_value)

    # [Optional] call the original excepthook as well
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

# sys.excepthook = custom_excepthook
sys.excepthook = lambda *args: ipdb.pm()

os.environ["PYTHONBREAKPOINT"] = "ipdb.set_trace"

class CfgStoragePrinter(Printer):
    def print(self) -> None:
        pass

    def visit_source_unit(self, node: ir.SourceUnit):
        print(f"Source unit:", node.file)
        # assert False

    def visit_variable_declaration(self, node: ir.VariableDeclaration):
        from rich.syntax import Syntax

        if not node.is_state_variable:
            return
        breakpoint()
        for ref in node.references:
            if isinstance(ref, (ir.Identifier, ir.MemberAccess)):
                statement = ref.statement
                func_or_mod = statement.declaration
                cfg = func_or_mod.cfg
                cfg_block = cfg.get_cfg_block(statement)

                print(f"    State variable [bold]{node.name}[/bold] used in {func_or_mod.canonical_name}:")
                print("    ", Syntax(statement.source, "solidity"))
                print("")

    @printer.command(name="cfg-storage")
    def cli(self) -> None:
        pass
