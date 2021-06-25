from odoo import fields, models, _
from odoo.exceptions import AccessError


class KzmDigest(models.Model):
    _inherit = 'digest.digest'

    kpi_helpdesk_tickets_feedback = fields.Boolean('Tickets Feedback')
    kpi_helpdesk_tickets_feedback_value = fields.Integer(compute='_compute_kpi_helpdesk_tickets_feedback_value')

    kpi_helpdesk_activities = fields.Boolean('Activities')
    kpi_helpdesk_activities_value = fields.Integer(compute='_compute_kpi_helpdesk_activities_value')

    def _compute_kpi_helpdesk_tickets_feedback_value(self):
        name = "feedback"
        if not self.env.user.has_group('helpdesk.group_helpdesk_user'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            feedback_ticket = self.env['helpdesk.ticket'].search_count([
                ('stage_id.name', '=', name),
                ('company_id', '=', company.id)
            ])
            record.kpi_helpdesk_tickets_feedback_value = feedback_ticket

    def _compute_kpi_helpdesk_activities_value(self):
        name = "feedback"
        stat = "overdue"
        if not self.env.user.has_group('helpdesk.group_helpdesk_user'):
            raise AccessError(_("Do not have access, skip this data for user's digest email"))
        for record in self:
            start, end, company = record._get_kpi_compute_parameters()
            activities = self.env['helpdesk.ticket'].search_count([
                ('activity_state', '=', stat),
                ('stage_id.name', '=', name),
                ('company_id', '=', company.id),
            ])
            record.kpi_helpdesk_activities_value = activities

    def compute_kpis_actions(self, company, user):
        res = super(KzmDigest, self).compute_kpis_actions(company, user)
        res['kpi_helpdesk_tickets_feedback'] = 'helpdesk.helpdesk_team_dashboard_action_main&menu_id=%s' % self.env.ref(
            'helpdesk.menu_helpdesk_root').id
        res['kpi_helpdesk_activities'] = 'helpdesk.helpdesk_team_dashboard_action_main&menu_id=%s' % self.env.ref(
            'helpdesk.menu_helpdesk_root').id
        return res
