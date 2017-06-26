# Markdown

import dash_core_components as dcc
import dash_html_components as html
import dash

app = dash.Dash()

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash usses the [CommonMark](http://commonmark.org/) specification for Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help) if this is your first introduction to Markdown!
'''

app.layout = html.Div([
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server()
