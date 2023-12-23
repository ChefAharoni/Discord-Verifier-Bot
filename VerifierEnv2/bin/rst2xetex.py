#!/Users/amitaharoni/Library/CloudStorage/Dropbox/03. Main Personal/01. Knowledge, Courses & School/06. CUNY - BMCC/04. Spring Semester 2024/F. Hackathon/Discord/Discord-Verifier-Bot/VerifierEnv2/bin/python

# $Id: rst2xetex.py 9115 2022-07-28 17:06:24Z milde $
# Author: Guenter Milde
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing Lua/XeLaTeX code.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except Exception:
    pass

from docutils.core import publish_cmdline

description = ('Generates LaTeX documents from standalone reStructuredText '
               'sources for compilation with the Unicode-aware TeX variants '
               'XeLaTeX or LuaLaTeX. '
               'Reads from <source> (default is stdin) and writes to '
               '<destination> (default is stdout).  See '
               '<https://docutils.sourceforge.io/docs/user/latex.html> for '
               'the full reference.')

publish_cmdline(writer_name='xetex', description=description)
