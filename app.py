# pylint: disable=redefined-outer-name,protected-access,missing-function-docstring
"""In this module we configure our awesome-panel.org app and serve it using the
awesome_panel.application framework.

The awesome_panel.application framework provides

- Templates: One or more Templates to layout your app(s). A template might provide `main`,
`sidebar`, `topbar` layouts where you can put your content.
- Components: Smaller constitutents used to create the Template or PageComponents
- Views: Layout+Styling of Components
- Services: Services that can be used by the Template and components. For example a progress_service
- Models: Like Application, Page, Author, Tag, Progress etc.
"""
import os
import platform

import panel as pn

# We need to configure the site before we import the pages
from application.config import site  # isort: split

# We need to import the application module to get the applications added to the site
from application import pages  # pylint: disable=unused-import

if __name__ == "__main__":
    address = os.getenv("BOKEH_ADDRESS", "0.0.0.0")
    port = int(os.getenv("BOKEH_PORT", 80))
    APP_ROUTES = {app.url: app.view for app in site.applications}
    if platform.system() == "Windows":
        pn.serve(APP_ROUTES, port=port, dev=False, address=address)
    else:
        print(address)
        pn.serve(APP_ROUTES, port=port, dev=False, address=address, num_procs=4)
