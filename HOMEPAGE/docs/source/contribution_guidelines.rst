Contribution Guidelines
=======================

Thank you for your interest in contributing to **CPFA
(Climate Prediction For All)**.

This page summarizes the contribution process. For more details,
refer to the ``CONTRIBUTING.md`` and ``CODE_OF_CONDUCT.md`` files
in the repository.

Ways to Contribute
------------------

You can contribute by:

- Reporting bugs and issues
- Suggesting enhancements or new features
- Improving documentation and examples
- Extending visualization and evaluation scripts
- Adding support for additional datasets or regions

Reporting Issues
----------------

Before opening a new issue:

1. Check the existing issues on GitHub.
2. Look for a similar bug report or feature request.

If no existing issue matches your case, open a new one and include:

- A clear title and description
- Steps to reproduce the issue
- Expected behavior versus actual behavior
- Screenshots, logs, or error messages when applicable
- Environment information:

  - Operating system
  - Python version
  - Package versions (especially ONNX and ONNX Runtime)

Development Workflow
--------------------

A typical development workflow is:

1. Fork the CPFA repository on GitHub.
2. Clone your fork locally.
3. Create a feature branch for your work.
4. Implement the changes and add tests or examples if appropriate.
5. Run the project scripts to verify that predictions, visualization,
   and evaluation still function as expected.
6. Submit a pull request (PR) with a clear description of the changes.

Code Style
----------

- Follow standard Python style conventions (PEP 8) as much as possible.
- Keep functions and scripts focused and readable.
- Add comments where the intent is not obvious.
- Avoid introducing unnecessary dependencies.

Documentation
-------------

- Update relevant documentation pages under the ``docs`` folder when
  you change the user-facing behavior.
- Ensure that examples and instructions remain consistent with the
  current code.
- When adding new features or options, mention them in the appropriate
  sections (e.g. How to Use, Technical Overview, FAQ).

Code of Conduct
---------------

CPFA follows a Code of Conduct to provide a welcoming and inclusive
environment for all contributors.

- Treat others with respect.
- Be constructive in discussions and reviews.
- Report unacceptable behavior as described in the Code of Conduct.

Please refer to ``CODE_OF_CONDUCT.md`` in the repository for the full
text.
