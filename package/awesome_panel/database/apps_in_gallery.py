"""In this module we define the list of apps contributed to the Gallery

Please note that all contribute apps should

- be located in https://raw.githubusercontent.com/MarcSkovMadsen/awesome-panel/master/
gallery/<app_name_folder>
- include that tags tags.CODE, tags.APP_IN_GALLERY as a minimum
"""
from awesome_panel.database import authors, tags
from awesome_panel.database.settings import GITHUB_BLOB_MASTER_URL, THUMBNAILS_ROOT
from awesome_panel.shared.models import Resource

GITHUB_GALLERY_URL = GITHUB_BLOB_MASTER_URL + "src/pages/gallery/"

# Please keep this list sorted by name
APPS_IN_GALLERY = [
    Resource(
        name="Bootstrap Dashboard",
        url=GITHUB_GALLERY_URL + "bootstrap_dashboard/main.py",
        thumbnail_path=THUMBNAILS_ROOT + "bootstrap_dashboard.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Bootstrap Alerts",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_bootstrap_alerts.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_bootstrap_alerts.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Code",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_code.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_code.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Divider",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_divider.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_divider.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test FontAwesome",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_fontawesome.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_fontawesome.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Headings",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_headings.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_headings.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Markdown",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_markdown.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_markdown.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
    Resource(
        name="Test Spinners",
        url=GITHUB_GALLERY_URL + "awesome_panel_express_tests/test_spinners.py",
        thumbnail_path=THUMBNAILS_ROOT + "test_spinners.png",
        tags=[tags.CODE, tags.APP_IN_GALLERY, tags.AWESOMEPANEL_EXPRESS],
        is_awesome=True,
        author=authors.MARC_SKOV_MADSEN,
    ),
]
