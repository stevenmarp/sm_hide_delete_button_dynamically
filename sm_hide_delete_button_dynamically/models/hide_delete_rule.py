from odoo import api, fields, models


class SmHideDeleteRule(models.Model):
    _name = "sm.hide.delete.rule"
    _description = "Hide Delete Button Rule"
    _rec_name = "model_id"
    _order = "model_id"

    model_id = fields.Many2one("ir.model", string="Model", required=True, ondelete="cascade")
    model_name = fields.Char(related="model_id.model", store=True, readonly=True, index=True)
    group_ids = fields.Many2many("res.groups", string="Apply to Groups")
    active = fields.Boolean(default=True)
    notes = fields.Text()

    _sql_constraints = [
        ("model_unique", "unique(model_id)", "Only one delete rule is allowed per model."),
    ]

    @api.model
    def sm_is_delete_hidden(self, model_name):
        if not model_name:
            return False
        rules = self.sudo().search([("active", "=", True), ("model_name", "=", model_name)])
        if not rules:
            return False
        group_field = "groups_id" if "groups_id" in self.env.user._fields else "all_group_ids"
        user_group_ids = set(self.env.user[group_field].ids)
        for rule in rules:
            if not rule.group_ids or user_group_ids.intersection(rule.group_ids.ids):
                return True
        return False
