# -----------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -----------------------------------------------------------------------------

"""Tests for helper methods that may be used by various components."""

import unittest
import os
import sfctl.params as sf_params
from mock import patch, MagicMock

# TODO: Make sure this is actually run
class ToolTests(unittest.TestCase):
    """Tooling tests"""

    def parse_boolean(self):
        """Parse string into a boolean"""
        input_string = "truE"
        returned_bool = sf_params.to_bool(input_string)
        self.assertEqual(True, returned_bool)

        input_string = "faLse"
        returned_bool = sf_params.to_bool(input_string)
        self.assertEqual(False, returned_bool)

        input_string = "gibberish"
        with self.assertRaises(CLIError):
            sf_params.to_bool(input_string)
