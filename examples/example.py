import sys
import os.path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            os.path.pardir
        )
    )
)

from htmlfactory.TagFactory import TagFactory
from htmlfactory.SingletonTag import SingletonTag


def get_email_component():
    email_component = TagFactory(
        "div.form-group",
        (
            TagFactory(
                "label",
                'Email Address',
                four="exampleInputEmail1"
            ),
            TagFactory(
                "input.form-control",
                id="exampleInputEmail1",
                ariadescribedby="emailHelp",
                placeholder="Enter email"
            ),
            TagFactory(
                "small.form-text.text-muted",
                "We'll never share your email with anyone else.",
                id="emailHelp"
            ),
        )
    )

    return email_component


def get_password_component():
    password_component = TagFactory(
        "div.form-group",
        (
            TagFactory(
                "label",
                'Password',
                four="exampleInputPassword1"
            ),
            TagFactory(
                "input.form-control",
                id="exampleInputPassword1",
                placeholder="Password"
            ),
        )
    )

    return password_component


def get_checkbox_component():
    checkbox_component = TagFactory(
        "div.form-check",
        (
            TagFactory(
                "input.form-check-input",
                id="exampleCheck1"
            ),
            TagFactory(
                "label.form-check-label",
                'Check me out',
                four="exampleCheck1"
            ),
        )
    )

    return checkbox_component


def get_submit_button():
    button_component = TagFactory(
        "button.btn.btn-primary",
        'Submit',
        type="submit"
    )

    return button_component


def example_form():
    form_component = TagFactory("form")
    form_component.add_child_element(get_email_component())
    form_component.add_child_element(get_password_component())
    form_component.add_child_element(get_checkbox_component())
    form_component.add_child_element(get_submit_button())
    return form_component


def get_head_component():
    head = TagFactory("head")
    head.add_child_element(
        SingletonTag("meta", charset="utf-8"),
        SingletonTag(
            "meta",
            content="width=device-width, initial-scale=1, shrink-to-fit=no",
        ),
        SingletonTag(
            "link",
            href="https://maxcdn.bootstrapcdn.com"
            + "/bootstrap/4.0.0/css/bootstrap.min.css",
            integrity="sha384-Gn5384xqQ1aoWXA+058RXP"
            + "xPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm",
            crossorigin="anonymous"
        ),
        TagFactory("title", "Hello, world!")
    )

    return head


def get_body_component():
    body = TagFactory("body")
    body.add_child_element(
        TagFactory(
            "script",
            src="https://code.jquery.com/"
            + "jquery-3.2.1.slim.min.js",
            integrity="sha384-KJ3o2DKtIkvYIK3UENz"
            + "mM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN",
            crossorigin="anonymous"
        ),
        TagFactory(
            "script",
            src="https://cdnjs.cloudflare.com/ajax/"
            + "libs/popper.js/1.12.9/umd/popper.min.js",
            integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3m"
            + "gPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q",
            crossorigin="anonymous"
        ),
        TagFactory(
            "script",
            src="https://maxcdn.bootstrapcdn.com/"
            + "bootstrap/4.0.0/js/bootstrap.min.js",
            integrity="sha384-JZR6Spejh4U02d8jOt6v"
            + "LEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl",
            crossorigin="anonymous"
        )
    )

    return body


def example_base_html_page():
    html_page = TagFactory("html", lang="en")
    html_page.add_child_element(get_head_component())
    html_page.add_child_element(get_body_component())

    return html_page
