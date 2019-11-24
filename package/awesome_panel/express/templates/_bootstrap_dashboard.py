
import panel as pn
import pathlib

TEMPLATE_URL = pathlib.Path(__file__).parent / "templates" / "bootstrap_dashboard.html"


class BootStrapDashboardTemplate(pn.Template):
    def __init__(self, app_title: str = "App Name"):
        template = TEMPLATE_URL.read_text()

        self.sidebar = pn.Column()
        self.main = pn.Column()

        items = {
            "sidebar": self.sidebar,
            "main": self.main,
            "app_title": pn.Row(
                pn.pane.HTML(app_title),
            ),
        }
        super().__init__(template=template, items=items)

        self.add_panel("app_title", pn.Row(pn.pane.HTML("App Title")))

