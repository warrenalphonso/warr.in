# warr.in

Most of the personal [static content](https://en.wikipedia.org/wiki/Static_web_page)
I want to put on the Internet. Built with [Pelican](https://getpelican.com/).

## Development

Install and use [`pre-commit`](https://pre-commit.com/) git hooks.

Install the requirements:

```bash
pip install -r requirements.txt
```

List and use the [PyInvoke](https://www.pyinvoke.org/index.html) commands:

```bash
inv --list
```

## Theme

I'd like to just inherit the [`simple` theme](https://github.com/getpelican/pelican/tree/master/pelican/themes/simple),
but they don't wrap everything in block so I can't customize as much as I want.
_This means that [some settings in the docs](https://docs.getpelican.com/en/latest/settings.html)
won't work because I removed the places the variables are read._

All non-blogpost files (including `index.html`) will be generated from the
`page.html` template. All blogpost files will be generated from the `article.html`
template. This means we don't need an `index.html` template.

## Design Graveyard

### Embed Jupyter Notebooks

It'd be neat to use a plugin to embed Jupyter Notebooks in blog posts. The main
problem is that making the Notebook CSS play well with our site CSS wasn't straightforward,
and [while I could use some hacks](https://github.com/danielfrg/pelican-jupyter/blob/1e52ce679a4922cc4307f8b6e7e9da8104db27f5/core.py#L118-L119)
I didn't want to depend on a static `nbconvert` version ([`nbconvert` chooses
the CSS version](https://cdn.jupyter.org/notebook/5.4.0/style/style.min.css)).
I can revisit this if there's more documentation and stability around Jupyter
Notebook CSS classes.

Alternatively, I could convert to Markdown and then style the input/output cells
myself. I didn't want do that.
