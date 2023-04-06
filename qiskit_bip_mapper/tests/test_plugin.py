# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Test the BIPMapping pass."""

import unittest

from qiskit import QuantumCircuit
from qiskit.circuit.library.standard_gates import SwapGate
from qiskit.compiler.transpiler import transpile
from qiskit.transpiler.coupling import CouplingMap
from qiskit.transpiler.preset_passmanagers.plugin import list_stage_plugins


class TestBIPMapping(unittest.TestCase):
    """Tests the BIPMapping plugin."""

    def test_plugin_in_list(self):
        """Test bip plugin is installed."""
        self.assertIn("bip", list_stage_plugins("routing"))

    def test_trivial_case(self):
        """No need to have any swap, the CX are distance 1 to each other.

        q0:--(+)-[H]-(+)-
              |       |
        q1:---.-------|--
                      |
        q2:-----------.--

        CouplingMap map: [1]--[0]--[2]
        """
        coupling = CouplingMap([[0, 1], [0, 2]])

        circuit = QuantumCircuit(3)
        circuit.cx(1, 0)
        circuit.h(0)
        circuit.cx(2, 0)
        actual = transpile(
            circuit, coupling_map=coupling, routing_method="bip", optimization_level=0
        )
        self.assertEqual(11, len(actual))
        for inst, _, _ in actual.data:  # there are no swaps
            self.assertFalse(isinstance(inst, SwapGate))
