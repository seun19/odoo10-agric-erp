# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


# Farm Product
class FarmProduct(models.Model):
    _name = 'agrohaven.production.farmproduce'

    # produce name
    name = fields.Char('Farm Produce', index=True, required=True, translate=True)
    production_estimate_ids = fields.One2many('agrohaven.production.farmproduction', 'farmproduce_id',
                                              string="Production Estimate")
    description = fields.Text('Description', translate=True,
                              help="A precise description of the Product, used only for internal information purposes.")
    category_id = fields.Many2one('agrohaven.production.farmproducecategory',
                                  ondelete='set null', string="Produce Category", index=True)


# Farm Category
class FarmProductCategory(models.Model):
    _name = 'agrohaven.production.farmproducecategory'

    # Category Name
    name = fields.Char('Produce Category', index=True, required=True, translate=True)
    description = fields.Text(
        'Description', translate=True,
        help="A precise description of the Product, used only for internal information purposes.")


# Production Estimate
class FarmProduction(models.Model):
    _name = 'agrohaven.production.farmproduction'

    # production name
    name = fields.Char('Production Title', index=True, required=True, translate=True)
    supervisor_id = fields.Many2one('res.users', ondelete='set null', string="Supervisor", index=True)
    farmproduce_id = fields.Many2one('agrohaven.production.farmproduce', ondelete='cascade',
                                     string="Farm Produce", required=True)
    status = fields.Selection([
        ('not_started', "Not Started"),
        ('in_progress', "In Progress"),
        ('completed', "Completed"),
    ], default='not_started')

    # Location
    location = fields.Char('Location', translate=True)

    # Cost
    estimated_production_cost = fields.Float('Estimated Production Cost')
    actual_production_cost = fields.Float('Actual Production Cost')

    # Time Duration
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')

    # Activities
    activity_ids = fields.One2many('agrohaven.production.farmactivity', 'production_id', string="Activities")


# Pest and Disease Detection
class DiseaseDetection(models.Model):
    _name = 'agrohaven.production.disease'

    # disease name
    name = fields.Char('Production Title', index=True, required=True, translate=True)
    risk_detected = fields.Text('Risk Detected', translate=True, help="Type of risk")
    # Variables or Indicators
    indicators = fields.Char('Variables/Indicators')
    date_logged = fields.Date('Date Logged')

    # Supervisor must be picked automatically from the seasons supervisor
    supervisor_id = fields.Many2one('res.users', ondelete='set null', string="Supervisor", index=True)


# Unit of Measure
class UnitOfMeasure(models.Model):
    _name = 'agrohaven.production.unitofmeasure'

    name = fields.Char('Unit of Measure', index=True, required=True, translate=True)
    description = fields.Text(
        'Description', translate=True,
        help="A precise description of the unit of measure, used only for internal information purposes.")