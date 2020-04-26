import panel as pn

def test_can_construct_application_template_with_exception(application_component, application_template):
    # Then
    assert application_template.application is application_component
    assert isinstance(application_template.menu, pn.layout.Reactive)
    assert isinstance(application_template.sidebar, pn.layout.Reactive)
    assert isinstance(application_template.main, pn.layout.Reactive)
    assert application_template.main.objects
    assert isinstance(application_template.theme_css, pn.pane.HTML)

def test_main_content_changes_when_page_changes(application_template, home_page_component, gallery_page_component):
    # Given
    assert application_template.application.model.page == home_page_component
    before = application_template.main.objects
    # When
    application_template.application.model.page = gallery_page_component
    after = application_template.main.objects
    # Then
    assert before != after

# def test_app_title_pane_object_changes_when_application_title_changes(application_template):
#     # Given
#     application_template.application.title != "New Title"
#     # When
#     application_template.application.title = "New Title"
#     # Then
#     application_template.

