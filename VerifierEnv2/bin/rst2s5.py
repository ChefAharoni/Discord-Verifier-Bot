#!/Users/amitaharoni/Library/CloudStorage/Dropbox/03. Main Personal/01. Knowledge, Courses & School/06. CUNY - BMCC/04. Spring Semester 2024/F. Hackathon/Discord/Discord-Verifier-Bot/VerifierEnv2/bin/python

# $Id: rst2s5.py 9115 2022-07-28 17:06:24Z milde $
# Author: Chris Liechti <cliechti@gmx.net>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing HTML slides using
the S5 template system.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except Exception:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates S5 (X)HTML slideshow documents from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='s5', description=description)
