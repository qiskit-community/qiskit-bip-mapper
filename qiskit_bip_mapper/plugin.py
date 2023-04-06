# This code is part of Qiskit.
#
# (C) Copyright IBM 2023
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Qiskit BIPMapping transpiler pass plugin."""

from qiskit.transpiler.preset_passmanagers.plugin import PassManagerStagePlugin
from qiskit.transpiler.passes import CheckMap, Error
from qiskit.transpiler import PassManager

from qiskit_bip_mapper.bip_mapping import BIPMapping


def _not_mapped(property_set):
    return not property_set["is_swap_mapped"]


class BIPMappingPlugin(PassManagerStagePlugin):
    """BIPMapping routing stage plugin."""

    def pass_manager(self, pass_manager_config, optimization_level):
        """Return the plugin pass manager."""
        pm = PassManager(
            [
                BIPMapping(
                    pass_manager_config.coupling_map,
                    backend_prop=pass_manager_config.backend_properties,
                ),
                CheckMap(pass_manager_config.coupling_map),
            ]
        )
        pm.append(Error(msg="BIP mapper failed to map", action="raise"), condition=_not_mapped)
        return pm
