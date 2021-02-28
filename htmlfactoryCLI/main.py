import typer
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             os.path.pardir)))

from htmlfactory.TagFactory import TagFactory
from htmlfactory.SingletonTag import SingletonTag

app = typer.Typer()

@app.command()
def tag(tag_and_class_str: str, inner_html: str = '', pretty_str: bool = False):
    """
    Return an html tag by passing TAG_AND_CLASS_STR. 
    
    --inner-html lets the user pass a string that goes
    in between the opening and closing tag.
    
    --pretty-str outputs the tags with an indent.
    """
    my_tag = ''
    if pretty_str:
        my_tag = TagFactory(tag_and_class_str, inner_html).pretty_str()
    else:
        my_tag = TagFactory(tag_and_class_str, inner_html)

    output = typer.style(str(my_tag), fg=typer.colors.GREEN)
    typer.echo(output)


@app.command()
def singleton(tag_and_class_str: str):
    """
    Create a SingletonTag with a TAG_AND_CLASS_STR,
    such as "img.image".
    """
    typer.echo(SingletonTag(tag_and_class_str))

if __name__ == "__main__":
    app()