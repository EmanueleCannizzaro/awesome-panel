"""Work in Progress Template based on Shoelace"""
import pathlib

import jinja2
import panel as pn

ROOT = pathlib.Path(__file__).parent
JS = (ROOT / "index.js").read_text()
CSS = (ROOT / "index.css").read_text()

TEMPLATES_FOLDER = str(ROOT / "templates")

bokehLoader = jinja2.PackageLoader("bokeh.core", "_templates")
templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATES_FOLDER)
loader = jinja2.ChoiceLoader([templateLoader])
templateEnv = jinja2.Environment(loader=loader)
TEMPLATE_FILE = "index.html"
template = templateEnv.site.get_template(TEMPLATE_FILE)
# outputText = template.render()  # this is where to put args to the template renderer

tmpl = pn.Template(template)

tmpl.add_variable("app_title", "Awesome Panel")
tmpl.add_variable("app_css", CSS)
tmpl.add_variable("app_js", JS)

tmpl.servable()
