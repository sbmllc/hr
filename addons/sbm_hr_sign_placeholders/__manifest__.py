{
    "name": "SBM Odoo Sign Placeholders (EN/ES)",
    "version": "1.0.0",
    "category": "Human Resources",
    "summary": "Seed Odoo Sign with default EN/ES placeholder templates for SBM onboarding/offboarding packets.",
    "author": "SB Management LLC",
    "license": "OPL-1",
    "depends": ["sign", "documents", "mail", "sbm_hr_core"],
    "data": [
        "security/ir.model.access.csv",
        "data/sign_roles.xml",
        "data/sign_templates.xml"
    ],
    "installable": True,
    "application": False
}
