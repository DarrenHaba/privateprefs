# SPDX-FileCopyrightText: 2022-present Darren Haba <darrenhaba@live.com>
#
# SPDX-License-Identifier: MIT
from .cli import *

# The cli needs access to private save functions
# Note: the end users should use the cli instead of calling these private save functions
from ..privateprefs import _save, _save_dict # noqa



