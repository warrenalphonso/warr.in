# warr.in

Most of the personal [static content](https://en.wikipedia.org/wiki/Static_web_page)
I want to put on the Internet. Built with [Pelican](https://getpelican.com/).

## Development

Install and use [`pre-commit`](https://pre-commit.com/) git hooks.

Install the requirements:

```bash
pip install -r requirements.txt
```

Install the TailwindCSS CLI. I recommend installing it as a [standalone executable](https://tailwindcss.com/blog/standalone-cli):

```bash
curl -sL https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-x64 -o tailwindcss
chmod +x tailwindcss
```

> PyInvoke will expect the `tailwindcss` executable to exist in `PATH`. Personally,
> I keep executables for my user in `~/.local/bin/` and add this to `PATH`. [Mirroring
> the full Unix root structure is useful if you need to compile binaries just for
> your user](https://unix.stackexchange.com/a/36874).

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

### Styling

I'm using [TailwindCSS](https://tailwindcss.com/). We're using it as a PostCSS plugin.
PostCSS is some way of combining JS and CSS. I've got this input file called
`tailwind.css`.
`tailwind.config.js` knows where our HTML content lives; when I run a TailwindCSS
CLI command to convert the PostCSS input file to a CSS output file, Tailwind will
only add styles that our HTML _is actually using_ to the output file. This keeps
our output file very small!

## Design Showcase

### Inflation-adjusted prices

I try to display inflation-adjusted USD prices by using the [Urban Consumer Price
Index Minus Food and Energy](https://fred.stlouisfed.org/series/CPILFESL).This was
[inspired by Gwern](https://gwern.net/static/build/Inflation.hs).

Client-side lookup: The inflation calculation is done client-side instead of during
build because:

- I want the display to be up-to-date even if I don't build the site every year.
  Performing the calculation client-side means I can look up the current year and
  just display the original price and original year if my CPI data is outdated.
- It's slightly more general: building the website periodically to update inflation
  is assuming that inflation is fairly slow-moving.

Interoperability with Markdown: I've written a Python-Markdown extension to swap
`$[price:year]` with `<span class="inflation" data-value={price} data-year={year}>${price} in {year}</span>`,
which the JS snippet can then operate on. The extension contextualizes the price,
so it's useful even if JS is disabled, my snippet has a bug, or the CPI data is
oudated.

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
