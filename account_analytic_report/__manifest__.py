# Copyright 2024 (APSL - Nagarro) Bernat Obrador
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Analytic Reports",
    "version": "17.0.1.0.0",
    "summary": "OCA Analytic Reports",
    "author": "APSL-Nagarro, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-financial-reporting",
    "category": "Account",
    "depends": ["analytic", "account_financial_report"],
    "maintainers": ["BernatObrador", "miquelalzanillas"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/trial_balance_analytic_wizard_view.xml",
        "menuitems.xml",
        "reports.xml",
        "report/templates/trial_balance_analytic.xml",
        "views/report_trial_balance_analytic.xml",
        "views/account_analytic_line.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "account_analytic_report/static/src/js/*",
        ],
    },
    "application": False,
    "installable": True,
    "auto_install": False,
    "license": "AGPL-3",
}
