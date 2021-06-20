"""The Awesome Panel Gallery based on the Fast Components"""
# pylint: disable=line-too-long
import panel as pn
from awesome_panel_extensions.frameworks.fast.templates.fast_gallery_template import (
    FastGalleryTemplate,
)

from application.config import site

APPLICATION = site.create_application(
    url="gallery",
    name="Gallery",
    author="Marc Skov Madsen",
    introduction="""A custom Panel template using the Fast
    web components""",
    description="""The Gallery provides a very visual overview to the applications and associated
    resources""",
    thumbnail_url="gallery.png",
    documentation_url="",
    code_url="fast_gallery/fast_gallery.py",
    gif_url="",
    mp4_url="",
)


@site.add(APPLICATION)
def view():
    """Return a FastGalleryTemplate"""
    pn.config.raw_css = [
        css for css in pn.config.raw_css if not css.startswith("/* CUSTOM TEMPLATE CSS */")
    ]
    return FastGalleryTemplate(
        site="Awesome Panel",
        title="Gallery",
        description="""The purpose of the Awesome Panel Gallery is to inspire and help you create awesome analytics apps in <fast-anchor href="https://panel.holoviz.org" target="_blank" appearance="hypertext">Panel</fast-anchor> using the tools you know and love.""",
        resources=site.applications,
        target="_self",
        theme="dark",
        meta_name="Awesome Panel Gallery",
        meta_description="Gallery of applications at awesome-panel.org",
        meta_keywords=(
            "Awesome, HoloViz, Panel, Gallery, Apps, Science, Data Engineering, Data Science, "
            "Machine Learning, Python"
        ),
        meta_author="Marc Skov Madsen",
    )


if __name__.startswith("bokeh"):
    view().servable()
