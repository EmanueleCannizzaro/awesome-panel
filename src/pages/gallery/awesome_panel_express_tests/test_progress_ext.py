"""In this module we test the ProgressExt widget

The purpose of the ProgressExt widget is to enable easier progress reporting using the existing
[`pn.widgets.Progress`](https://panel.pyviz.org/reference/widgets/Progress.html#gallery-progress)
widget.

The ProgressExt widget provides

- A combination of a progress value and a progress message
- Easy to use functionality for
    - Function Annotation
    - Context Management

An example use case is

```python
progress = ProgressExt()
run_button = pn.widgets.Button(name="Click me")

@progress.increment(50, "incrementing ...")
def run(event):
    time.sleep(0.5)
run_button.on_click(run)

app = pn.Column(run_button, progress.view)
app.servable()
```

which will show the progress and reset every 2 clicks.
"""

import time

import panel as pn

from awesome_panel.express import ProgressExt
from awesome_panel.express.testing import TestApp


def test_view_value_and_message():
    """We test the view with a value and a message

    - The progress bar is active with the value 50
    - The message hello world is visible
    - The bar color is the blue *info* color
    """
    progress = ProgressExt(value=50, message="hello world")
    return TestApp(test_view_value_and_message, progress.view())


def test_view_message_only():
    """We test the view with a message only

    - The progress bar is active with no value
    - The message is stated
    - The bar color is the blue *info* color
    """
    progress = ProgressExt(value=0, message="hello world")
    return TestApp(test_view_message_only, progress.view())


def test_view_value_only():
    """We test the view with a value only

    - The progressbar is shown with a value of 50
    - No message is shown
    """
    progress = ProgressExt(value=50, message="")
    return TestApp(test_view_value_only, progress.view())


def test_view_none():
    """We test the view with no message or value

    - No progressbar is shown
    - No message is shown
    """
    progress = ProgressExt(value=0, message="")
    return TestApp(test_view_none, progress.view())


def test_bar_color():
    """We test the view with a value and a message

    - The progress bar is active with the value 50
    - The message hello world is visible
    - The bar color is the green *success* color
    """
    progress = ProgressExt(value=50, message="hello world", bar_color="success")
    return TestApp(test_bar_color, progress.view())


def test_report_as_context_manager():
    """We test that the `ProgressExt.report` function works as a context manager

    - Click the button to see the progress reported for 1 secs
    """
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    def run(event):  # pylint: disable=unused-argument
        with progress.report(50, "running"):
            time.sleep(1)

    run_button.on_click(run)
    return TestApp(test_report_as_context_manager, run_button, progress.view)


def test_report_as_decorator():
    """We test that the `ProgressExt.report` function works as a decorator

    - Click the button to see the progress reported for 1 secs
    """
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    @progress.report(33, "calculation")
    def run(event):  # pylint: disable=unused-argument
        time.sleep(1)

    run_button.on_click(run)
    return TestApp(test_report_as_decorator, run_button, progress.view)


def test_increment_as_context_manager():
    """We test that the `ProgressExt.report` function works as a context manager

    - Click the button multiple times and check that the progress is reset every 2 clicks
    """
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    def run(event):  # pylint: disable=unused-argument
        with progress.increment(50, "incrementing ..."):
            time.sleep(0.5)

    run_button.on_click(run)
    return TestApp(test_increment_as_context_manager, run_button, progress.view)


def test_increment_as_decorator():
    """We test that the `ProgressExt.report` function works as a context manager

    - Click the button multiple times and check that the progress is reset every 2 clicks
    """
    progress = ProgressExt()
    run_button = pn.widgets.Button(name="Click me")

    @progress.increment(50, "incrementing ...")
    def run(event):  # pylint: disable=unused-argument
        time.sleep(0.5)

    run_button.on_click(run)
    return TestApp(test_increment_as_decorator, run_button, progress.view)


def view() -> pn.Column:
    """Wraps all tests in a Column that can be included in the Gallery or served independently

    Returns:
        pn.Column -- A Column containing all the tests
    """
    return pn.Column(
        __doc__,
        test_view_value_and_message,
        test_view_message_only,
        test_view_value_only,
        test_view_none,
        test_bar_color,
        test_report_as_context_manager,
        test_report_as_decorator,
        test_increment_as_context_manager,
        test_increment_as_decorator,
        pn.layout.HSpacer(height=100),
        width=800,
    )


if __name__.startswith("bk"):
    view().servable()
