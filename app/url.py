# -*- coding: utf-8 -*-

from ctrl.table import TableCtrl
from ctrl.grade import GradeCtrl


url = [
    (r'/grade', GradeCtrl),
    (r'/table', TableCtrl),
    # (r'/library', LibraryCtrl),
    # (r'/card', CardCtrl),
    # (r'/net', NetCtrl),
    # (r'/news', NewsCtrl),
]