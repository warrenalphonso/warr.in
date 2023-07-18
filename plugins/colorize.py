"""Loop through colors and assign them to <a> and <blockquote> elements."""
import itertools
from pathlib import Path

from bs4 import BeautifulSoup
from pelican import signals


def style_all_files(pelican_object):
    color_vars = itertools.cycle(["zero", "one", "two", "three", "four", "five"])

    output_path = Path(pelican_object.settings["OUTPUT_PATH"])
    for filepath in output_path.rglob("*.html"):
        with open(filepath, "r") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        for tag in soup.find_all(["a", "blockquote"]):
            var = next(color_vars)
            if tag.name == "a":
                tag["class"] = tag.get("class", []) + [f"link-{var}"]
            elif tag.name == "blockquote":
                tag["class"] = tag.get("class", []) + [f"blockquote-{var}"]
        with open(filepath, "w") as file:
            file.write(str(soup))


def register():
    signals.finalized.connect(style_all_files)
