FAQ
===

This page provides answers to frequently asked questions about CPFA.

General
-------

**Q: What is CPFA?**

A: CPFA (Climate Prediction For All) is an open-source educational tool
for running, visualizing, and evaluating climate predictions using
Pangu-Weather models.

**Q: What is the main purpose of CPFA?**

A: The main purpose is to provide a simple and transparent workflow
for climate prediction experiments, particularly in educational and
self-study settings.

Installation
------------

**Q: Which operating system is CPFA documented for?**

A: CPFA is primarily documented for Windows with Anaconda and
Python 3.9.2.

**Q: Which Python version should I use?**

A: Python 3.9.2 is recommended and used in the installation guide.

**Q: Which libraries are required?**

A: At minimum, NumPy, pandas, matplotlib, xarray, cartopy, ONNX
(1.13.1), and ONNX Runtime (1.14.0).

Usage
-----

**Q: What input format does CPFA require?**

A: The main input is ``input_surface.npy`` with shape
``(4, 721, 1440)`` and variable order
``[MSLP, U10, V10, T2M]``, stored in the ``input_data`` folder.

**Q: Where do prediction outputs go?**

A: Prediction outputs and derived products are stored in the
``output_data`` folder.

**Q: How do I generate visualizations?**

A: After running the prediction script, run ``visualization.py`` to
generate plots.

Evaluation
----------

**Q: How do I compare predictions with ERA5 data?**

A: Use the ``evaluation.py`` script. It reads prediction outputs and
ERA5 reference data, then computes basic performance metrics.

**Q: What metrics are supported?**

A: The exact metrics depend on the implementation of ``evaluation.py``.
Typical metrics include differences or simple error statistics.

Contributing
------------

**Q: How can I report a bug?**

A: Open an issue on the CPFA GitHub repository with detailed
information about the problem and your environment.

**Q: Is there a way to propose new features?**

A: Yes. Create a feature request issue on GitHub and describe the
motivation, expected behavior, and possible design.

Support
-------

**Q: How can I contact the maintainers?**

A: You can use GitHub Issues for public questions and bug reports.
For urgent or private matters, use the contact information listed
on the project communication channels or README.
