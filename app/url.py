# -*- coding: utf-8 -*-

from ctrl.table import TableCtrl
from ctrl.grade import GradeCtrl
from ctrl.data import *


url = [
    (r'/grade', GradeCtrl),
    (r'/table', TableCtrl),
    # (r'/library', LibraryCtrl),
    (r'/ver', VerCtrl),
    (r'/dataflow', DataflowCtrl),
    (r'/datacharge', DatachargeCtrl)
    # (r'/net', NetCtrl),
    # (r'/news', NewsCtrl),
]