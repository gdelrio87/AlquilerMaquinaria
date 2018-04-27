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

class maquina(osv.Model):

    _name = 'maquina'
    _description = 'Maquinas de alquiler'
    
    def _check_precio(self, cr, uid, ids):   
        for clase in self.browse(cr, uid, ids):
            if clase.precio_alquiler < 0: 
                return False 
        return True
    
    _columns = {
            'name':fields.char('Nombre', size=64, required=True),
            'modelo':fields.char('ID Modelo', size=64, required=True),
            'maquina':fields.char('ID Maquina', size=64, required=True),
            'foto': fields.binary('Foto', required=True),
            'descripcion':fields.text('Descripcion', size=250, required=True),
            'precio_alquiler':fields.float('Precio de alquiler', size=64, required=True),
            'alquileres':fields.many2many("alquiler","maquina_alquiler_rel","maquina_id","alquiler_id","Maquinas alquiladas",readonly=True),
            'proveedor':fields.many2one('proveedor', 'Proveedor', readOnly=True),
            'devoluciones': fields.many2many('devolucion','maquina_devolucion_rel','maquina_id','devolucion_id','Maquinas devueltas'), 
            'state':fields.selection([('almacen','Almacen'),('alquilado','Alquilado'),('averia','Averia'),('devuelto','Devuelto'),('finVidaUtil','Fin de vida util')],'Estado de la maquina'),
            
        }
    
    _defaults = {'state':'almacen',}
    
    _constraints = [(_check_precio, 'El precio no puede ser negativo', ['precio_alquiler']), ] 
    
    _sql_constraints = [ ('modelo', 'unique(modelo)', 'El ID modelo debe ser unico'), ('maquina', 'unique(maquina)', 'El ID maquina debe ser unico'), ]
    
maquina()