# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields
from cups import require

class cliente(osv.Model):

    _name = 'cliente'
    _description = 'Datos de los clientes'
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True),
            'apellidos':fields.char('Apellidos', size=64, required=True),
            'dni':fields.char('DNI', size=64, required=True),
            'email':fields.char('Email', size=64, required=True),
            'telefono':fields.char('Teléfono', size=25, required=True),
            'domicilio': fields.char('Domicilio', size=64, required=True),
            'ciudad': fields.char('Ciudad', size=64, required=True),
            'provincia': fields.many2one("res.country.state","Provincia", required=True),
            'cp': fields.integer('Cod. Postal', size=10, required=True),
            'pais': fields.many2one("res.country","Pais",required=True),
        }
    
    _sql_constraints = [ ('dni', 'unique(dni)', 'El DNI debe ser unico'), ]
    
    def onchange_provincia(self, cr, uid, ids, provincia, context=None):
        if provincia:
            pais = self.pool.get('res.country.state').browse(cr, uid, provincia, context).country_id.id
            return {'value':{'pais':pais}}
        return {}

cliente()