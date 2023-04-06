# Qiskit BIPMapping Plugin

This repository contains a standalone routing stage to use the ``BIPMapping``
routing pass. The BIP mapping pass solves the
[routing](https://qiskit.org/documentation/apidoc/transpiler.html#routing-stage)
and [layout](https://qiskit.org/documentation/apidoc/transpiler.html#layout-stage)
problems as a binary integer programming (BIP) problem. The algorithm used
in this pass is described in:

G. Nannicini et al. "Optimal qubit assignment and routing via integer programming."
[arXiv:2106.06446](https://arxiv.org/abs/2106.06446)

This plugin depends on [CPLEX](https://www.ibm.com/products/ilog-cplex-optimization-studio)
to solve the BIP problem. While a no-cost version of CPLEX is available (and published on
[PyPI](https://pypi.org/project/cplex/)) this has limits set on the size of the problems
it can solve which prevents it from being used except for very small quantum circuits. If
you would like to use this transpiler pass for larger circuits a CPLEX license will be
required.


## Install and Use plugin

To use the unitary synthesis plugin first install qiskit terra with the pull
request:

```bash
pip install qiskit-bip-mapper
```
To install the plugin package. As part of the install process `pip` will install
the no-cost version of CPLEX from PyPI, if you're going to use a 

## Using BIPMapping pass

Once you have the plugin package installed you can use the plugin via the
`routing_method="bip"` argument on Qiskit's `transpile()` function. For example,
if you wanted to use the `BIPMapping` method to compile a 15 qubit quantum
volume circuit for a backend you would do something like:

```python

from qiskit import transpile
from qiskit.circuit.library import QuantumVolume
from qiskit.providers.fake_provider import FakePrague

qc = QuantumVolume(15)
qc.measure_all()
backend = FakePrague()

transpile(qc, backend, routing_method="bip")
```

# Authors and Citation

The BIPMapping pass is is the work of [many people](https://github.com/Qiskit/rustworkx/graphs/contributors)
who contribute to the project at different levels. Additionally, the plugin was
originally developed as part of the Qiskit project itself and you can see the
development history for it here:
<!-- update links to 0.24.0 release once available -->

- https://github.com/Qiskit/qiskit-terra/commits/0.23.3/qiskit/transpiler/passes/routing/bip_mapping.py
- https://github.com/Qiskit/qiskit-terra/commits/0.23.3/qiskit/transpiler/passes/routing/algorithms/bip_model.py

If you use `qiskit-bip-mapper` in your research, please cite our paper as per the included [BibTeX file](CITATION.bib) file.

