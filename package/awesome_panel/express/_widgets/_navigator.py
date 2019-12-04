"""This module contains a navigation menu to be used to select between different pages"""
from typing import List, Union

import panel as pn
import param

import awesome_panel.express as pnx


class NavigationButton(pn.widgets.Button):
    def __init__(
        self,
        page: Union[pn.layout.Panel, pn.pane.Pane],
        page_outlet: pn.layout.ListPanel,
        *args,
        **kwargs,
    ):
        """## Navigation Button to navigate between pages

        Arguments:
            page {Union[pn.layout.Panel, pn.pane.Pane]} -- A page to navigate to when the button is
            clicked
            page_outlet {pn.layout.ListPanel} -- The ListPanel to update when the user navigates to
            a new page
        """
        if "name" not in kwargs:
            kwargs["name"] = page.name

        super().__init__(*args, **kwargs)

        def navigate_to_page(event):  # pylint: disable=unused-argument
            page_outlet.clear()
            page_outlet.append(page)

        self.on_click(navigate_to_page)


class NavigationMenu(pn.Column):
    "## Navigation Menu"

    def __init__(  # pylint: disable=too-many-arguments
        self,
        pages: List[Union[pn.layout.Panel, pn.pane.Pane]],
        page_outlet: pn.layout.ListPanel,
        *args,
        title: str = "Navigation",
        text_align: str = "center",
        sizing_mode: str = "stretch_width",
        **kwargs,
    ):
        """## Navigation Menu

        A widget composed of NavigationButtons that can be used to navigate between pages.

        Arguments:
            pages {List[Union[pn.layout.Panel, pn.pane.Pane]]} -- A list of 'pages' to navigate
                between. The first page in pages is selected by default.
            page_outlet {pn.layout.ListPanel} -- The ListPanel to update when the user navigates to
                a new page
        """
        menuitems = [NavigationButton(page=page, page_outlet=page_outlet) for page in pages]
        title = pnx.SubHeader(title, text_align=text_align)
        super().__init__(title, *menuitems, sizing_mode=sizing_mode, *args, **kwargs)

        page_outlet.clear()
        page_outlet.append(pages[0])
