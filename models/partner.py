from odoo import api, fields, models


class Partner(models.Model):
    _name = 'toko_hp.partner'
    _description = 'human description'

    
    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='Telepon')
    foto = fields.Char(string='Foto')
    
    
class Pegawai(models.Model):
    _inherit = 'toko_hp.partner'
    _name = 'toko_hp.pegawai'
    

    name = fields.Char(string='Nama')
    alamat_pegawai = fields.Char(string='Alamat Pegawai')
    no_telepon = fields.Char(string='No telepon')
    gaji = fields.Char(string='Gaji')
    bonus = fields.Char(string='Bonus')


class Pembeli(models.Model):
    _inherit = 'toko_hp.partner'
    _name = 'toko_hp.pembeli'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    no_telepon = fields.Char(string='No Telepon')