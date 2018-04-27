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

class devolucion(osv.Model):
    _name = 'devolucion'
    _description = 'Datos de la devolucion'
    
    _columns = {
            'name': fields.text('Descripción', size=250, required=True),
            'cliente': fields.many2one('cliente','Cliente', required=True),
            'administrativo': fields.many2one('administrativo','Administrativo', required=True),
            'maquinas': fields.many2many('maquina', 'maquina_devolucion_rel' ,'devolucion_id','maquina_id','Listado maquinas devueltas', required=True),
            'fecha_devolucion': fields.date('Fecha devolución', required=True),
                    }
devolucion()