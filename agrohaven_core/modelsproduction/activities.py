# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Farm Activity
class FarmActivity(models.Model):
    _name = 'agrohaven.production.farmactivity'

    # activity name
    name = fields.Char('Farm Activity', index=True, required=True, translate=True)

    estimated_quantity = fields.Float('Estimated Quantity')
    # Will be a computed field
    actual_quantity = fields.Float('Actual Quantity')
    estimated_cost = fields.Float('Estimated Cost')
    # Will be a computed field
    actual_cost = fields.Float('Actual Cost')
    # Status
    status = fields.Selection([
        ('not_started', "Not Started"),
        ('in_progress', "In Progress"),
        ('completed', "Completed"),
    ], default='not_started')

    assigned_employee_id = fields.Many2one('res.users', ondelete='set null', string="Assigned To", index=True,
                                           help="Employee who is assigned to do the job")
    # still need to work on dates
    start_date = fields.Date(default=fields.Date.today)  # Default date
    end_date = fields.Date(default=fields.Date.today)  # Default date

    # Yet to figure out how this should be
    frequency = fields.Char('Frequency', translate=True)
    production_id = fields.Many2one('agrohaven.production.farmproduction', ondelete='cascade', string="Production",
                                    required=True)
    unit_of_measure_id = fields.Many2one('agrohaven.production.unitofmeasure', ondelete='cascade',
                                         string="Unit of Measure", required=True)

    description = fields.Text('Description', translate=True,
                              help="A precise description of the Activity, used only for internal information purposes.")
