from gallery.bootstrap_dashboard.components.dashboard import Dashboard
from gallery.bootstrap_dashboard.components.products import Products
from gallery.bootstrap_dashboard.components.customers import customers_view
from gallery.bootstrap_dashboard.components.plotly import plotly_view
from gallery.bootstrap_dashboard.components.holoviews import holoviews_view

# class PageConfig(NamedTuple):
#     name: str
#     font_awesome_class: str
#     pane: pn.Pane


# PAGE_CONFIGS = [
#     PageConfig("Dashboard", "fas fa-home", Orders().view()),
#     PageConfig("Products", "far fa-file", Products()),
#     PageConfig("Customers", "fas fa-file", simple()),
#     PageConfig("Reports", "fas fa-file", pn.pane.Markdown("Reports")),
#     PageConfig("Integrations", "fas fa-file", pn.pane.Markdown("Integrations")),
#     PageConfig("About", "fas fa-file", markdown_from_file(ABOUT_PATH)),
# ]
