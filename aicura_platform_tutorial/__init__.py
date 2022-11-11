"""Top-level package for myproject."""

import pkg_resources

__version__=pkg_resources.get_distribution("myproject").version

__author__ = """your name"""
__email__ = 'your email'

from . import (
    metrics,
    postprocessors
)