from odoo import api, fields, models


class Handphone(models.Model):
    _name ='toko.handphone'
    _description = 'New Description'
    name = fields.Char(string='Merk HP')  
   
   
    img = fields.Binary(string='Image')
    deskripsi = fields.Char(string='Deskripsi')
    spesifikasi = fields.Char(string='Spesifikasi')
    harga_hp = fields.Integer(string='Harga HP')
    stok_hp = fields.Integer(string='Stok HP')
   
    