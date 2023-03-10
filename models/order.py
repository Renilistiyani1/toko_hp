from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Order(models.Model):
    _name ='toko_hp.order'
    _description = 'New Description'


    orderhandphonedetail_ids = fields.One2many(
        comodel_name='toko_hp.orderhandphonedetail', 
        inverse_name='order_id', 
        string='Order Hp')

    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan',default=fields.Datetime.now())
    tanggal_pengiriman = fields.Date(string='Tanggal Pengiriman', default=fields.Date.today())
    pembeli = fields.Many2one(
        comodel_name='toko_hp.pembeli', 
        string='Pembeli')

    jumlah_beli = fields.Integer(string='Jumlah Beli')

class OrderHandphoneDetail(models.Model):
    _name = 'toko_hp.orderhandphonedetail'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='toko_hp.order', string='Order Hp')
    handphone_id = fields.Many2one(comodel_name='toko.handphone', 
                                    string='Handphone',
                                    domain=[('stok_hp','>','1')])

    name = fields.Char(string='Name')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')

    @api.depends('handphone_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.handphone_id.harga_hp
    
    qty = fields.Integer(string='Quantity')
    
    @api.constrains('qty')
    def _check_stok_hp(self):
        for record in self:
            bahan = self.env['toko.handphone'].search([('stok_hp', '<',record.qty)])
            if bahan:
                raise ValidationError("Stok Hp Tidak Cukup")
    
    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('harga_satuan','qty')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_satuan * record.qty
               
    
    @api.model
    def create(self,vals):
        record = super(OrderHandphoneDetail, self).create(vals) 
        if record.qty:
            self.env['toko.handphone'].search([('id','=',record.handphone_id.id)]).write({'stok_hp':record.handphone_id.stok_hp-record.qty})
            return record
    