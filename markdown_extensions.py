"""Custom Python-Markdown extensions."""
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor


class SkipInlinePattern(InlineProcessor):
    """If a match is found, keep the whole string as-is."""

    def handleMatch(self, m, _data):
        return m.group(0), m.start(0), m.end(0)


class MathExtension(Extension):
    def __init__(self, regexes: list[str], **kwargs) -> None:
        super().__init__(**kwargs)
        self.regexes = regexes
        if not isinstance(regexes, list):
            raise ValueError(
                f"Argument 'regexes' should be a list, but instead got {regexes}"
            )

    def extendMarkdown(self, md):
        md.registerExtension(self)
        for i, pattern in enumerate(self.regexes):
            # We choose a priority just above 'escape':
            # https://github.com/Python-Markdown/markdown/blob/master/markdown/inlinepatterns.py
            md.inlinePatterns.register(SkipInlinePattern(pattern), f"math-{i}", 185)
