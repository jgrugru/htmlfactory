import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             os.path.pardir)))

from typer.testing import CliRunner

from htmlfactoryCLI.main import app

runner = CliRunner()


def test_tag():
    result = runner.invoke(app, ["tag", "div.basic"])
    assert result.exit_code == 0
    assert """<div class='basic'></div>""" in result.stdout


def test_tag_with_inner_html():
    result = runner.invoke(app, ["tag", "div.basic", "--inner-html", "I'm inside"])
    assert result.exit_code == 0
    assert """<div class='basic'>I'm inside</div>""" in result.stdout


def test_tag_with_pretty_str():
    result = runner.invoke(app, ["tag", "div.basic", "--inner-html", "I'm inside", "--pretty-str"])
    assert result.exit_code == 0
    assert """<div class="basic">\n I'm inside\n</div>""" in result.stdout


def test_singleton_tag():
    result = runner.invoke(app, ["singleton", "img.image"])
    assert result.exit_code == 0
    assert """<img class='image'>""" in result.stdout