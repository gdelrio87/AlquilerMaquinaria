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

class averia(osv.Model):
    _name = 'averia'
    _description = 'Datos de averia'
    
    def _compruebaCoste(self, cr, uid, ids):
        for alq in self.browse(cr, uid, ids):
            if alq.coste < 0:
                return False
            return True
    
    _columns = {
            'name': fields.text('Descripción', size=250, required=True),
            'tecnico': fields.many2one('tecnico','Tecnico', required=True),
            'maquina': fields.many2one('maquina','Maquina', required=True),
            'coste': fields.float('Coste', size=64, required=True),
            'fecha': fields.date('Fecha', required=True),
                    }
    
    _constraints = [(_compruebaCoste, 'El coste no puede ser negativo', ['coste'])]
    
averia()