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

class alquiler(osv.Model):
    _name = 'alquiler'
    
    def _totalMaquinas(self, cr, uid, ids, field, arg, context=None):
        res = {}
        for alq in self.browse(cr, uid, ids, context=context):
            res[alq.id] = len(alq.maquinas)
        return res
    
    def eliminarMaquinas(self, cr, uid, ids, context=None):
        res = self.write(cr, uid, ids, {'maquinas':[(5, )]}, context)
        return res
    
    def _compruebaImporte(self, cr, uid, ids):
        for alq in self.browse(cr, uid, ids):
            if alq.importe < 0:
                return False
            return True
        
    def _sumaPreciosMaquina(self, cr, uid, ids, field, arg, context=None):
        res = {}
        for alq in self.browse(cr, uid, ids, context=context):
            total = 0.0
            for maqui in alq.maquinas:
                total += maqui.precio_alquiler
            res[alq.id] = total
        return res
        
    def _compruebaFecha(self,cr,uid,ids):
        for alq in self.browse(cr, uid, ids):
            if alq.fecha_alquiler > alq.fecha_fin:
                return False
            return True   
        
    _columns = {
            'fecha_alquiler': fields.date('Fecha alquiler',required=True),
            'importe': fields.function(_sumaPreciosMaquina, type='integer', string='Precio total', store=True),
            'fecha_fin': fields.date('Fecha final alquiler',required=True),
            'administrativo': fields.many2one("administrativo","Administrativo",required=True),
            'cliente': fields.many2one("cliente","Cliente",required=True),
            'maquinas': fields.many2many("maquina","maquina_alquiler_rel","alquiler_id","maquina_id","Listado maquinas",required=True),
            'maquinas_alquiladas':fields.function(_totalMaquinas, type='integer', string="Maquinas alquiladas", store=True),           
                    }
    
    _constraints = [(_compruebaImporte, 'El precio no puede ser negativo', ['importe']), (_compruebaFecha, 'La fecha de fin no puede ser menor que la de inicio', ['fecha_alquiler','fecha_fin'])] 
    
alquiler()