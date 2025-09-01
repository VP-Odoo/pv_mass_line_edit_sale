# pv_mass_line_edit_sale/__manifest__.py
{
    "name": "Mass Line Edit – Sale",
    "version": "18.0.1.0.1",
    "summary": "Mass editing of sale order lines",
    "author": "PV-Odoo",
    "category": "Sales",
    "license": "LGPL-3",
    "depends": ["sale"],
    "data": ["views/sale_order_line_views.xml"],
    "license": "LGPL-3",
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
    'currency': 'EUR',
    "description": """
Mass Line Edit for Sale Orders
==============================

This module allows you to quickly update multiple sale order lines at once in any quotation or sales order.

Features:
---------
* **Master Toggle**: Add a *Select All Lines* checkbox at the top of the order form to enable bulk selection.
* **Per-Line Control**: Each sale order line gets an *Apply to All* toggle (boolean switch).
* **Mass Editing**: When you edit a field on one line with *Apply to All* enabled, the same change is automatically applied to all other selected lines in the same order.
* Works on both quotations and confirmed sales orders (subject to Odoo's standard field edit restrictions).
* Prevents infinite loops with a safe propagation mechanism.

Benefits:
---------
* Save time by editing once and applying changes to multiple lines.
* Reduce human error by ensuring consistent values across multiple order lines.

""",
}
