from contextlib import contextmanager

import param

from awesome_panel.application.models import Progress


class ProgressService(param.Parameterized):
    """The purpose of the ProgressService widget is to enable easier progress reporting using the
    existing of Progress.

    The ProgressService provides

    - Easy to use functionality for
        - Function Annotation
        - Context Management

    An example use case is

    ```python
    progress_service = ProgressService()
    run_button = pn.widgets.Button(name="Click me")

    @progress_service.increment(50, "incrementing ...")
    def run(event):
        time.sleep(0.5)
    run_button.on_click(run)

    ```

    which will report the progress and reset every 2 clicks.
    """

    progress = param.ClassSelector(class_=Progress, constant=True)

    def __init__(self, **params):
        if "progress" not in params:
            params["progress"] = Progress()

        super().__init__(**params)

    def update(self, value: int, message: str, value_max: int = 100, active_count: int = 0):
        """Updates the value and message

        Args:
            value (int): A value between 0 and 100
            message (str): A message for the user describing what is happening
        """
        # Please note the order matters as the Widgets updates two times. One for each change
        progress = Progress(
            value=value, value_max=value_max, message=message, active_count=active_count,
        )
        with param.edit_constant(self):
            self.progress = progress

    def reset(self,):
        """Resets the progress to its default values"""
        # Please note the order matters as the Widgets updates two times. One for each change
        with param.edit_constant(self):
            self.progress = Progress()

    @contextmanager
    def report(
        self, value: int = 0, message: str = "", value_max: int = 100, active_count: int = 0,
    ):
        """Report the value and message.

        When the function or code is finished the progress is reset.

        Can be used as context manager or decorator.

        Args:
            value (int, optional): A value between 0 and 100. Default is 0.
            value_max(int): The maximum value the progress value can be
            message (str, optional): A message for the user describing what is happening. Default
            is ""

        Yields:
            None: Nothing is yielded
        """
        previous_progress = self.progress
        self.update(value=value, message=message, value_max=value_max, active_count=active_count)
        yield
        with param.edit_constant(self):
            self.progress = previous_progress

    @contextmanager
    def increment(
        self, value: int, message: str, value_max: int = 100,
    ):
        """Increment the value and report the message.

        When the function or code is finished the progress is NOT reset unless progress.value >= 100.

        Can be used as context manager or decorator.

        Args:
            value (int): A value between 0 and 100 that will be added to self.progress.value.
            value_max(int): The maximum value the progress value can be
            message (str): A message for the user describing what is happening

        Yields:
            None: Nothing is yielded
        """
        value_half = int(value / 2)
        new_value = min(self.progress.value + value_half, value_max,)
        self.update(
            value=new_value, value_max=value_max, message=message,
        )

        yield
        new_value = self.progress.value + value_half
        if new_value >= value_max:
            self.reset()
        else:
            self.update(value=new_value, message=message, value_max=value_max)

    @contextmanager
    def is_active(
        self, message: str
    ):
        """Signals that the application is active

        Can be used as context manager or decorator.

        Args:
            message (str): A message for the user describing what is happening

        Yields:
            None: Nothing is yielded
        """
        previous_message = self.progress.message
        self.update(
            value=self.progress.value,
            value_max=self.progress.value_max,
            message=message,
            active_count=self.progress.active_count+1
        )

        yield

        self.update(
            value=self.progress.value,
            value_max=self.progress.value_max,
            message=previous_message,
            active_count=max(0, self.progress.active_count-1)
        )
