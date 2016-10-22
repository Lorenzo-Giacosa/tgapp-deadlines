# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate
from tg.i18n import ugettext as _

from deadlines import model
from deadlines.model import DBSession

class RootController(TGController):
    @expose('deadlines.templates.index')
    def index(self):
        sample = DBSession.query(model.Sample).first()
        flash(_("Hello World!"))
        return dict(sample=sample)
