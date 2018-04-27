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
#ClassName
##############################################################################
from osv import osv
from osv import fields

class pedido(osv.Model):

    _name = 'pedido'
    _description = 'Pedido de maquinarias a proveedores'
    
    def _compruebaImporte(self, cr, uid, ids):
        for alq in self.browse(cr, uid, ids):
            if alq.importe < 0:
                return False
            return True 
 
    _columns = {
            'name':fields.char('Id Modelo Maquina', size=64, required=True),
            'idpedido': fields.integer('ID pedido',required=True),
            'importe': fields.float('Importe', size=64, required=True),
            'administrativo':fields.many2one('administrativo', 'Administrativo', readOnly=True),
            'proveedor':fields.many2one('proveedor', 'Proveedor', readOnly=True),
            'state':fields.selection([('registrado','Registrado'),('Sin_stock','Sin stock'),('stock','En stock'),('salida','Salida de almacen'),('transito','En transito'),('localidad','En su localidad'),('entregado','Pedido entregado')],'Estado del pedido'),
        }
    
    _constraints = [(_compruebaImporte, 'El importe no puede ser negativo', ['importe'])]
    
    _sql_constraints = [ ('idpedido', 'unique(idpedido)', 'El ID Pedido debe ser unico'), ]
    
    _defaults = {'state':'registrado',}
        
pedido()