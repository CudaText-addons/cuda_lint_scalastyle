#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Joshua Hagins
# Copyright (c) 2015 Joshua Hagins
#
# Adapted to CudaLint by Alexey Torgashin, 2020
#
# License: MIT
#

"""This module exports the Scalastyle plugin class."""

import os
from cuda_lint import Linter, util
import cudatext as app
import shutil

jar_file = app.ini_read('plugins.ini', 'lint_scalastyle', 'jar', '_')
if not os.path.isfile(jar_file):
    app.msg_box('Cannot find Scalastyle, see\n settings/plugins.ini\n [lint_scalastyle]\n jar=...',
        app.MB_OK+app.MB_ICONERROR)

cfg_file_init = os.path.join(os.path.dirname(__file__), 'scalastyle_config.xml')
cfg_file = os.path.join(app.app_path(app.APP_DIR_SETTINGS), 'scalastyle_config.xml')

if not os.path.isfile(cfg_file) and os.path.isfile(cfg_file_init):
    shutil.copy(cfg_file_init, cfg_file)

class Scalastyle(Linter):

    """Provides an interface to scalastyle."""

    syntax = 'Scala'
    cmd = ('java', '-jar', jar_file, '--config', cfg_file, '@')

    regex = (
        r'^(?:(?P<error>error)|(?P<warning>warning))'
        r'(?: file=(?P<file>.+?))'
        r'(?: message=(?P<message>.+?))'
        r'(?: line=(?P<line>\d+))?'
        r'(?: column=(?P<col>\d+))?$'
    )

    multiline = False
    line_col_base = (0, -1)
    tempfile_suffix = 'scala'
    error_stream = util.STREAM_BOTH
    word_re = r'^(\w+|([\'"]).+?\2)'
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def split_match(self, match):
        """
        Return the components of the match.

        We override this method so that errors with no line number can be displayed.

        """

        match, line, col, error, warning, message, near = super().split_match(match)

        if line is None and message:
            line = 0

        return match, line, col, error, warning, message, near
