# -*- coding: utf-8 -*-

from ctrl.table import TableCtrl
from ctrl.grade import GradeCtrl
from ctrl.dataflow import DataflowCtrl
from ctrl.datacharge import DatachargeCtrl


url = [
    (r'/grade', GradeCtrl),
    (r'/table', TableCtrl),
    # (r'/library', LibraryCtrl),
    (r'/data', DataflowCtrl),
    (r'/datacharge', DatachargeCtrl)
    # (r'/net', NetCtrl),
    # (r'/news', NewsCtrl),
]