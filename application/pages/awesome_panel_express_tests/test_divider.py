"""This test is here for legacy reasons. Originally the `pn.layout.divider` was no documented
so I created my own because I did not know better.

The `pn.layout.divider` reference example is now available
(here)[https://panel.holoviz.org/reference/layouts/Divider.html#layouts-gallery-divider]
"""
import awesome_panel.express as pnx
import panel as pn
from awesome_panel.express.testing import TestApp

from application.config import site


def test_divider():
    """A manual test of the horizontal divider stretching to full width"""
    return TestApp(test_divider, pn.layout.Divider())


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    pn.config.sizing_mode = "stretch_width"
    main = [
        pn.pane.Markdown(__doc__),
        test_divider(),
    ]
    return site.get_template(title="Test Divider", main=main)


if __name__.startswith("bokeh"):
    view().servable("test_divider")
