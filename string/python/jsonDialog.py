#!/usr/bin/env python
from dialog import Dialog

d = Dialog(dialog="dialog")
code, tag = d.menu("Some text that will be displayed above the menu entries",
                   choices=[("Tag 1", "Item text 1"),
                            ("Tag 2", "Item text 2"),
                            ("Tag 3", "Item text 3")])