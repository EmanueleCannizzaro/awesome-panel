# Issues Experienced During Development of this Project

Let me start out by saying that I think that **Panel is already very powerfull and usefull**.

But I have experienced som issues and rough edges as I've developed this site.

By discussing them here I hope to give you an impression of the current issues and rough edges of developing a multipage application in Panel. I also hope they well get attention by the community (including me) and be solved to lower the friction of create awesome analytical apps in Panel.

You can find an overview of all my +50 open and closed issues + feature requests [here](https://github.com/holoviz/panel/issues?utf8=%E2%9C%93&q=author%3AMarcSkovMadsen+).

## The Bokeh Layout Engine is not always your friend

- The Bokeh layout engine can work against you when you try to create advanced layouts. Things do not perform or render as expected.

To circumvent these issues my most important learning is to **KEEP IT SIMPLE STUPID!**

- Use the [Template](https://panel.pyviz.org/user_guide/Templates.html) system whenever you can.
- Don't do lots of nested Columns and Rows in Panel.
- Don't configure layout settings like width, height, margin etc. of Panel Columns and Rows via Css.
    - Use Column and Row attributes in Panel for that.

### Solved

- Panel/ Bokeh applications are especially slow in Chrome. See [Bokeh Issue 9515](https://github.com/bokeh/bokeh/issues/9515)

## The Bokeh server does not Support Multiprocessing in Practice

- See [Issue 897](https://github.com/holoviz/panel/issues/897)

## Community and Documentation is difficult to use

See GitHub issues

- Please add more structure, search, navigation and content to Panel Documentation. [Issue 833](https://github.com/holoviz/panel/issues/833)
- Please add the wonderfull help text to the docstrings to get context help in editor. [Issue 837](https://github.com/holoviz/panel/issues/837)

### Solved

- Create Discuss Forum to foster community discussions and knowledge sharing on Panel. [Issue 831](https://github.com/holoviz/panel/issues/831)
- Make Panel help text readable on Windows in Command Prompt and Git bash. [Issue 836](https://github.com/holoviz/panel/issues/836)
- Change search functionality at [https://panel.pyviz.org/](https://panel.pyviz.org/) to return Panel specific results. [Issue 832](https://github.com/holoviz/panel/issues/832)

## Markdown is not well supported

See

- A simple layout with a column and 2 markdown panes displays on top of each other [Issue 835](https://github.com/holoviz/panel/issues/835).
    - If there is a large image in the markdown the page is not rendered correctly. The Bokeh layout engine does not get the height and width correctly.
- Wide Images can overflow. Would be nice if `max-width: 100%` was set by default.

### Solved

- Support rendering of indented markdown. [Issue 828](https://github.com/holoviz/panel/issues/828).
- No Code syntax highlighting. [Issue 391](https://github.com/holoviz/panel/issues/391)
- Cannot get full width widthout lots of empty space at bottom. [Issue 848](https://github.com/holoviz/panel/issues/848)

## Plotly Plots are not well supported

- Plotly is not yet responsive in Panel. See [Issue 822](https://github.com/holoviz/panel/issues/822)

## Panels, Panes and Widgets are not full width, responsive by default

Panes and Widgets are not configured to be full width, responsive by default. I always have to set `sizing_policy="stretch_width"`. This is just overhead and friction.

## Rough edges for being a first mover

I believe I experience some rough edges for being one of the first to create a multipage app in Panel with markdown (with images and code). For example

- DataFrame widget raises exception if two columns have the same names. See [Issue 821](https://github.com/holoviz/panel/issues/821).
- Cannot dynamically add and remove panes [Issue 838](https://github.com/holoviz/panel/issues/838)
- Images does not support src urls and alt texts [Issue 841](https://github.com/holoviz/panel/issues/841)

and I sometimes get error messages like this

```bash
2019-12-03 09:34:57,514 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:57,517 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,055 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,058 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,061 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,065 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,070 Cannot apply patch to 1291 which is not in the document anymore
2019-12-03 09:34:58,073 Cannot apply patch to 1291 which is not in the document anymore
```

I've been told I can ignore these as they don't matter.

### Solved

- Sizing_mode="stretch_width" does not work for DataFrame panes. See [Issue 823](https://github.com/holoviz/panel/issues/823)
- Css_classes attribute does not work for the Holoviews Panel [Issue 902](https://github.com/holoviz/panel/issues/902)
- Plotly does not show when dynamically adding and removing pages without adding plotly extension. See [Issue 840](https://github.com/holoviz/panel/issues/840)

## Bootstrap CSS and Javascript does not play nicely with Bokeh HTML, CSS and Javascript

It's difficult to use a framework like Bootstrap together with Panel which builds on Bokeh. I gave up on it and switched to pure Panel with custom CSS.

- The javascript handling responsive layouts in Bootstrap and Bokeh does not play well.
    - For example the Bootstrap sidebar automatically adjusts it's width if I change the window size but the Bokeh Buttons do not respond to this change.
- It's difficult to wrap Panel Panes and Widgets into Bootstrap components like cards as "component templating" is not supported. See [Issue 810](https://github.com/holoviz/panel/issues/810)

## Custom CSS does not play nicely with Bokeh HTML, CSS and Javascript

I've experienced numerous problems when using css.

I have a feeling that the Bokeh Javascript on elements does not take everything like images and inline css into account. But it's difficult for me to catch and understand.

For example I struggled with the below scrollbar until I found out it was because i had a `margin-bottom: 1rem;` in the css for the info box. When I removed that the problem was solved.

![Info Alert Scrollbar Problem](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/src/pages/gallery/bootstrap_dashboard/assets/images/info_alert_scrollbar_problem.png?raw=true)

But I also struggle with it on this Limitations page. It's like the big image just above confuses the rendering. The workaround is to set `img {max-width: 100%}` in the css.

## Font Awesome Icons Cannot Easily be Used

Icons like fontawesome icons are not supported in Buttons.

I needed Buttons with Icons for my navigation which cannot use the Bootstrap `<a class="nav-link" href="#">`.

I cannot navigate in my single page app using urls. That is not supported

I could develop a multi page app that Panel serves via urls. But then I would loose my application state when navigating between pages.

BUT. I FOUND A WAY TO IMPLEMENT IT MY SELF.

## Hot reload is slow and slows down development-test cycle

See [issue 849](https://github.com/holoviz/panel/issues/849)

## There is no Browser URL widget

There is not functionality or Widget in Panel to use the Browser and  URLs like `example.com/page1/?year=1976` for navigation, bookmarking and sharing links. See [issue 811](https://github.com/holoviz/panel/issues/811).

I would like to be able to keep the server app state in sync with the client app state via the browser url. I.e.

- If the user/ client navigates to a url my app state should be updated using the full url including parameters
- If I change my app state the parameters of my state should be available in the browser url for bookmarking and sharing.

BUT. I FOUND A WAY TO PARTIALLY IMPLEMENT IT MY SELF via Javascript.
