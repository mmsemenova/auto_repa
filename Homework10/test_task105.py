# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test_printargs(request):
    my_marker = request.node.get_closest_marker("id_check")
    if my_marker is not None:
        args = my_marker.args
        print(args)
