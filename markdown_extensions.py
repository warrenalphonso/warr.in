"""Custom Python-Markdown extensions."""
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor


class SkipInlinePattern(InlineProcessor):
    """If a match is found, keep the whole string as-is."""

    def handleMatch(self, m, _data):
        return m.group(0), m.start(0), m.end(0)


class ReplaceInlineMathDelimiters(InlineProcessor):
    r"""Extract math expression and replace delimiters with `\(...\)`."""

    def handleMatch(self, m, _data):
        return rf"\({m.group(1)}\)", m.start(0), m.end(0)


class MathJaxExtension(Extension):
    r"""
    Avoid parsing text within math block as MarkDown.

    This also converts inline math blocks delimiters `$...$` to `\(...\)` because
    dollar signs are pretty commonly used elsewhere.
    """

    r"""
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
        # MathJax frequently uses '\' characters, so we choose a priority above 'escape':
        # https://github.com/Python-Markdown/markdown/blob/master/markdown/inlinepatterns.py
        md.inlinePatterns.register(
            ReplaceInlineMathDelimiters(self.INLINE_RE), "math-inline", 185
        )
        md.inlinePatterns.register(SkipInlinePattern(self.BLOCK_RE), "math-block", 185)
