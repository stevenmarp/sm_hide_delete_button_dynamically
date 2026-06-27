{
    "name": "Hide Delete Button Dynamically",
    "version": "18.0.1.0.0",
    "category": "Extra Tools",
    "summary": "Hide Delete action dynamically per model and user group",
    "description": """
Hide Delete Button Dynamically
==============================

Hide the Delete action from form and list view action menus based on model
configuration and user groups.
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "depends": ["base", "web"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/hide_delete_rule_views.xml",
        "views/menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "sm_hide_delete_button_dynamically/static/src/js/hide_delete_action.js",
        ],
    },
    "images": [
        "static/description/banner.gif",
        "static/description/icon.png",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "price": 12.20,
    "currency": "USD",
}
