"""Custom Python-Markdown extensions."""
import itertools

from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from markdown.treeprocessors import Treeprocessor


class SkipInlinePattern(InlineProcessor):
    """If a match is found, keep the whole string as-is."""

    def handleMatch(self, m, _data):
        return m.group(0), m.start(0), m.end(0)


class ReplaceInlineMathDelimiters(InlineProcessor):
    """Extract math expression and replace delimiters with `\(...\)`."""

    def handleMatch(self, m, _data):
        return f"\({m.group(1)}\)", m.start(0), m.end(0)


class MathJaxExtension(Extension):
    """
    Extension to avoid parsing text within math block as MarkDown.

    This converts inline math blocks delimiters `$...$` to `\(...\)` because
    dollar signs are pretty commonly used elsewhere.
    """

    """
    Inline math should:
    - be enclosed by `$...$`
    - first or last character in expression shouldn't be whitespace `$ ...$` or
      `$... $`: use negative lookahead and lookbehind
    - avoid matching `\$`
    - avoid matching `$$`
    - avoid matchign empty math expression

    Block math should:
    - be enclosed by `$$ ... $$`
    - be allowed to span multiple lines, lazily: `.+?` with `re.DOTALL`
    - avoid matching `\$`
    """
    INLINE_RE = r"(?<!\\|\$)\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\$)"  # $...$
    BLOCK_RE = r"(?<!\\)\$\$.+?\$\$"  # $$ ... $$

    def extendMarkdown(self, md):
        # We choose a priority just above 'escape':
        # https://github.com/Python-Markdown/markdown/blob/master/markdown/inlinepatterns.py
        md.inlinePatterns.register(
            ReplaceInlineMathDelimiters(self.INLINE_RE), f"math-inline", 185
        )
        md.inlinePatterns.register(SkipInlinePattern(self.BLOCK_RE), f"math-block", 185)


class ColorizeProcessor(Treeprocessor):
    COLOR_VARIABLES = itertools.cycle(["zero", "one", "two", "three", "four", "five"])

    def _set_link_style(self, element):
        for child in element:
            if child.tag == "a":
                var = next(self.COLOR_VARIABLES)
                child.set(
                    "style",
                    f"background-image: linear-gradient(to bottom, var(--{var}) 0%, var(--{var}) 100%)",
                )
            self._set_link_style(child)

    def _set_blockquote_style(self, element):
        for child in element:
            if child.tag == "blockquote":
                var = next(self.COLOR_VARIABLES)
                child.set("style", f"border-color: var(--{var})")
            self._set_blockquote_style(child)

    def run(self, root):
        self._set_link_style(root)
        self._set_blockquote_style(root)


class ColorizeExtension(Extension):
    """Loop through colors and assign them to <a> and <blockquote> elements."""

    def extendMarkdown(self, md):
        md.treeprocessors.register(ColorizeProcessor(md), "colorize", -15)
