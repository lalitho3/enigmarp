from django.db import models
from django.contrib.auth.models import User


PROSPECTOS = [
        ('Fabricante > 100m2' , 'Fabricante > 100m2'),
        ('Fabricante < 100m2' , 'Fabricante < 100m2'),
        ('Distribuidor Mayorista', 'Distribuidor Mayorista')
    ]


METODOPAGO = [
        ('Transferencia', 'Transferecia'),
        ('Cheque posfechado', 'Cheque posfechado'),
        ('Efectivo', 'Efectivo'),
        ('Revision', 'Revision'),
        ('Deposito', 'Deposito')
    ]



DOCUMENTOS = [
    ('RFC Empresa', 'RFC Empresa'),
    ('Identificación Oficial REP Legal', 'Identificación Oficial REP Legal'),
    ('Comp. Domicilio Empresa', 'Comp. Domicilio Empresa'),
    ('Comp. Domicilio REP Legal', 'Comp. Domicilio REP Legal'),
    ('Acta Constitutiva', 'Acta Constitutiva'),
    ('Pagaré con Aval', 'Pagaré con Aval'),
    ('Identificación Oficial Aval', 'Identificación Oficial Aval'),
    ('Comp. Domicilio Aval', 'Comp. Domicilio Aval'),
    ('Estados de Cuenta Recientes(3)', 'Estados de Cuenta Recientes(3)'),
    ('Estados Financieros Anual y Mensual', 'Estados Financieros Anual y Mensual')]


class MantenimientoPMultiP(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UsuarioMultiPProspecto')
    id = models.AutoField(primary_key=True)
    Fecha = models.DateTimeField('Fecha', auto_now_add=True)
    RazonSocial = models.CharField('Razón Social', max_length=200, blank=False, null=False)
    Rfc = models.CharField('RFC',max_length=50, blank=False, null=False)
    NombreComercial = models.CharField('Nombre Comercial', max_length=200, blank=True)
    CodRuta = models.CharField('Codigo de Ruta', max_length=200, blank=True, null=True)
    CodAgente = models.CharField('Codigo de Agente', max_length=200, blank=True, null=True)
    NombreAgente = models.CharField('Nombre de Agente', max_length=200, blank=True, null=True)
    ContactoProspecto = models.CharField('Contacto de Prospecto', max_length=200, blank=True, null=True)
    DireccionFiscal = models.CharField('Dirección Fiscal', max_length=250, blank=True, null=True)
    NumExt = models.CharField('Numero Exterior', max_length=6,blank=True)
    NumInt = models.CharField('Numero Interior', max_length=6,blank=True)
    Colonia = models.CharField('Colonia', max_length=200, blank=True)
    Estado = models.CharField('Estado', max_length=100, blank=True)
    Municipio = models.CharField('Municipio', max_length=100, blank=True, null=True)
    CodigoPostal = models.IntegerField('Código Postal', blank=True, null=True)
    DireccionFabrica = models.CharField('Dirección Fabrica', max_length=250, blank=True, null=True)
    NumExtF = models.CharField('Numero Exterior Fabrica', max_length=6,blank=True)
    NumIntF = models.CharField('Numero Interior Fabrica', max_length=6,blank=True)
    ColoniaF = models.CharField('Colonia Fabrica', max_length=200, blank=True)
    EstadoF = models.CharField('Estado Fabrica', max_length=100, blank=True)
    MunicipioF = models.CharField('Municipio Fabrica', max_length=100, blank=True, null=True)
    CodigoPostalF = models.IntegerField('Código Postal Fabrica', blank=True, null=True)
    CorreoElectronico = models.EmailField('Correo Electronico', blank=False, null=False)
    Telefono = models.PositiveBigIntegerField('Numero Telefonico', blank=True,null=True )
    Telefono2 = models.PositiveBigIntegerField('Numero Telefonico 2', blank=True,null=True )
    TelefonoCelular = models.PositiveBigIntegerField('Numero Celular', blank=False, null=False)
    TipoProspecto = models.CharField(max_length=255,choices=PROSPECTOS,blank=False,null=False)
    VolumenCompra1 = models.DecimalField('Volumen de Compra', blank=True, null=True, decimal_places=2, max_digits=15)
    Producto1 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio1 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    VolumenCompra2 = models.DecimalField('Volumen de Compra',  blank=True, null=True, decimal_places=2, max_digits=15)
    Producto2 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio2 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    VolumenCompra3 = models.DecimalField('Volumen de Compra',  blank=True, null=True, decimal_places=2, max_digits=15)
    Producto3 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio3 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    VolumenCompra4 = models.DecimalField('Volumen de Compra', max_length=250, blank=True, null=True, decimal_places=2, max_digits=15)
    Producto4 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio4 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    Propietario = models.CharField('Propietario', max_length=200, blank=True, null=True)
    Gerente = models.CharField('Gerente', max_length=200, blank=True, null=True)
    PersonaCompras = models.CharField('Persona Encargada de Compras', max_length=200, blank=True, null=True)
    PersonaVentas = models.CharField('Persona Encargada de Ventas', max_length=200, blank=True, null=True)
    ProductosInteres = models.CharField('Productos o Marcas en Los Que Esta Interesado', max_length=255, blank=True, null=True)
    MarcaPrincipal = models.CharField('Marca Principal', blank=True, null=True, max_length=200)
    PorcentajeMarcaPrincipal = models.PositiveIntegerField('Porcentaje de marca principal', null=True, blank=True)
    SegundaMarca = models.CharField('Segunda Marca', blank=True, null=True, max_length=200)
    PorcentajeSegundaMarca = models.PositiveIntegerField('Porcentaje de segunda marca', null=True, blank=True)
    Otro = models.CharField('Otro', max_length=100, blank=True, null=True)
    PorcentajeOtro = models.PositiveIntegerField('Porcentaje de otra marca', null=True, blank=True)
    Otras = models.CharField('Otras', max_length=255, blank=True, null=True)
    Observaciones = models.TextField('Observaciones', blank=True, null=True)
    Seguimiento = models.TextField('Seguimiento', blank=True, null=True)

    class Meta:
        verbose_name = 'Mantenimiento de Prospecto'
        verbose_name_plural = 'Mantenimiento de Prospectos'
        ordering = ['-id']

    def __str__(self):
        return f'{self.RazonSocial}'



class MantenimientoClientes(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UsuarioMultiPCliente')
    id = models.AutoField(primary_key=True)
    Fecha = models.DateTimeField('Fecha', auto_now_add=True)
    RazonSocial = models.CharField('Razón Social', max_length=200, blank=False, null=False)
    Rfc = models.CharField('RFC',max_length=50, blank=False, null=False)
    Constancia = models.FileField(upload_to="constanciasFiscales/", null=True, blank=False)
    NombreComercial = models.CharField('Nombre Comercial', max_length=200, blank=True)
    CodRuta = models.CharField('Codigo de Ruta', max_length=200, blank=True, null=True)
    CodAgente = models.CharField('Codigo de Agente', max_length=200, blank=True, null=True)
    NombreAgente = models.CharField('Nombre de Agente', max_length=200, blank=True, null=True)
    ContactoProspecto = models.CharField('Contacto de Prospecto', max_length=200, blank=True, null=True)
    DireccionFiscal = models.CharField('Dirección Fiscal', max_length=250, blank=True, null=True)
    NumExt = models.CharField('Numero Exterior', max_length=6,blank=True)
    NumInt = models.CharField('Numero Interior', max_length=6,blank=True)
    Colonia = models.CharField('Colonia', max_length=200, blank=True)
    Estado = models.CharField('Estado', max_length=100, blank=True)
    Municipio = models.CharField('Municipio', max_length=100, blank=True, null=True)
    CodigoPostal = models.IntegerField('Código Postal', blank=True, null=True)
    DireccionFabrica = models.CharField('Dirección Fiscal', max_length=250, blank=True, null=True)
    NumExtF = models.CharField('Numero Exterior', max_length=6,blank=True)
    NumIntF = models.CharField('Numero Interior', max_length=6,blank=True)
    ColoniaF = models.CharField('Colonia', max_length=200, blank=True)
    EstadoF = models.CharField('Estado', max_length=100, blank=True)
    MunicipioF = models.CharField('Municipio', max_length=100, blank=True, null=True)
    CodigoPostalF = models.IntegerField('Código Postal', blank=True, null=True)
    CorreoElectronico = models.EmailField('Correo Electronico', blank=False, null=False)
    Telefono = models.PositiveBigIntegerField('Numero Telefonico', blank=True,null=True )
    Telefono2 = models.PositiveBigIntegerField('Numero Telefonico 2', blank=True,null=True )
    TelefonoCelular = models.PositiveBigIntegerField('Numero Celular', blank=False, null=False)
    TipoProspecto = models.CharField(max_length=255,choices=PROSPECTOS,blank=False,null=False)
    VolumenCompra1 = models.DecimalField('Volumen de Compra', blank=True, null=True, decimal_places=2, max_digits=15)
    Producto1 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio1 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    VolumenCompra2 = models.DecimalField('Volumen de Compra',  blank=True, null=True, decimal_places=2, max_digits=15)
    Producto2 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio2 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    VolumenCompra3 = models.DecimalField('Volumen de Compra',  blank=True, null=True, decimal_places=2, max_digits=15)
    Producto3 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio3 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    VolumenCompra4 = models.DecimalField('Volumen de Compra', max_length=250, blank=True, null=True, decimal_places=2, max_digits=15)
    Producto4 = models.CharField('Producto', max_length=255, blank=True, null=True)
    Precio4 = models.DecimalField('Precio', blank=True, null=True, decimal_places=2, max_digits=15)
    Propietario = models.CharField('Propietario', max_length=200, blank=True, null=True)
    Gerente = models.CharField('Gerente', max_length=200, blank=True, null=True)
    PersonaCompras = models.CharField('Persona Encargada de Compras', max_length=200, blank=True, null=True)
    PersonaVentas = models.CharField('Persona Encargada de Ventas', max_length=200, blank=True, null=True)
    ProductosInteres = models.CharField('Productos o Marcas en Los Que Esta Interesado', max_length=255, blank=True, null=True)
    Otras = models.CharField('Otras', max_length=255, blank=True, null=True)
    TipoPago = models.CharField(choices=METODOPAGO, max_length=255, blank=True, null=True)
    DiasPago = models.CharField('Días de Pago', max_length=100, blank=True)
    LugarPago = models.CharField('Lugar de Pago', max_length=200, blank=True, null=True)
    DiasRevision = models.CharField('Días de Revisión', max_length=100, blank=True)
    LugarRevision = models.CharField('Lugar de Pago', max_length=200, blank=True, null=True)
    DireccionEntrega = models.CharField('Dirección de Entrega', max_length=200, blank=True, null=True)
    MarcaPrincipal = models.CharField('Marca Principal', blank=True, null=True, max_length=200)
    PorcentajeMarcaPrincipal = models.PositiveIntegerField('Porcentaje de marca principal', null=True, blank=True)
    SegundaMarca = models.CharField('Segunda Marca', blank=True, null=True, max_length=200)
    PorcentajeSegundaMarca = models.PositiveIntegerField('Porcentaje de segunda marca', null=True, blank=True)
    Otro = models.CharField('Otro', max_length=100, blank=True, null=True)
    PorcentajeOtro = models.PositiveIntegerField('Porcentaje de otra marca', null=True, blank=True)
    Decorativo = models.IntegerField('Decorativo (%)',  blank=True, null=True)
    Automotriz = models.IntegerField('Automotriz (%)', blank=True, null=True)
    Industrial = models.IntegerField('Industrial (%)', blank=True, null=True)
    Vinilica = models.IntegerField('Vinilica (%)',  blank=True, null=True)
    Esmalte = models.IntegerField('Esmalte (%)', blank=True, null=True)
    Barnices = models.IntegerField('Barnices (%)', blank=True, null=True)
    Observaciones = models.TextField('Observaciones', blank=True, null=True)
    



    class Meta:
        verbose_name = 'Mantenimiento de Cliente'
        verbose_name_plural = 'Mantenimiento de Clientes'
        ordering = ['-id']

    def __str__(self):
        return f'Cliente Numero: {self.id}, {self.NombreComercial}'




class SolicitudCredito(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UsuarioMultiPCredito')
    id = models.AutoField(primary_key=True)
    Fecha = models.DateTimeField('Fecha', auto_now_add=True)
    RazonSocial = models.CharField('Razón Social', max_length=200, blank=False, null=False)
    Codigo = models.CharField('Codigo', max_length=150, blank=True, null=True)
    Rfc = models.CharField('RFC',max_length=30, blank=False, null=False)
    NombreComercial = models.CharField('Nombre Comercial', max_length=200, blank=False, null=False)
    CodRuta = models.CharField('Codigo de Ruta', max_length=200, blank=True, null=True)
    CodAgente = models.CharField('Codigo de Agente', max_length=200, blank=True, null=True)
    NombreAgente = models.CharField('Nombre de Agente', max_length=200, blank=True, null=True)
    DireccionFiscal = models.CharField('Dirección Fiscal', max_length=250, blank=False, null=False)
    NumExt = models.CharField('Numero Exterior', max_length=6,blank=True)
    NumInt = models.CharField('Numero Interior', max_length=6,blank=True)
    Colonia = models.CharField('Colonia', max_length=200, blank=True)
    Estado = models.CharField('Estado', max_length=100, blank=True)
    Municipio = models.CharField('Municipio', max_length=100, blank=True)
    CodigoPostal = models.IntegerField('Código Postal', blank=True, null=True)
    PuntoVenta = models.CharField('Dirección Punto de Venta', max_length=250, blank=False, null=False)
    Telefono = models.PositiveBigIntegerField('Numero Telefonico', blank=False,null=False )
    Telefono2 = models.PositiveBigIntegerField('Numero Telefonico 2', blank=True,null=True )
    Celular = models.PositiveBigIntegerField('Numero celular ', blank=True,null=True )
    Fax = models.CharField('Fax', max_length=200, blank=True)
    CorreoElectronico = models.EmailField('Correo Electronico', blank=False, null=True)
    ListaPrecios = models.CharField('Lista de Precios', max_length=250, blank=True, null=True)
    DescuentoGeneral = models.SmallIntegerField('Descuento General (%)', blank=True, null=True)
    Plazo = models.CharField('Plazo', max_length=250, blank=True)
    DescuentosLinea = models.CharField('Descuentos especiales por linea', max_length=150, blank=True, null=False)
    LineaCredito = models.CharField('Linea de Crédito', max_length=150, blank=True, null=True)
    Fletera = models.CharField('Fletera', max_length=150, blank=True, null=True)
    ContactoFletera = models.CharField('Contacto Fletera', max_length=150, blank=True, null=False)
    DireccionFletera = models.CharField('Dirección Fletera', max_length=150, blank=True, null=False)
    TelefonoFletera = models.PositiveBigIntegerField('Numero Celular Fletera', blank=True, null=True)
    DescuentoPronto = models.IntegerField('Descuento Pronto Pago (%)', blank=True, null=True)
    InteresMoratorio = models.IntegerField('Interes Moratorio Mensual (%)', blank=True, null=True)
    Gerente = models.CharField('Gerente', max_length=200, blank=True, null=True)
    PersonaCompras = models.CharField('Persona Encargada de Compras', max_length=200, blank=True, null=True)
    PersonaVentas = models.CharField('Persona Encargada de Ventas', max_length=200, blank=True, null=True)
    PersonaPagos = models.CharField('Persona Encargada de Pagos', max_length=200, blank=True, null=True)
    Propietario = models.CharField('Propietario', max_length=200, blank=True)
    Direccion = models.CharField('Dirección del Propietario', max_length=250, blank=True, null=True)
    TelefonoPropietario = models.PositiveBigIntegerField('Numero Telefonico del Propietario', blank=False,null=False )
    FaxPropietarion = models.CharField('Fax del Propietario', max_length=200, blank=True)
    ReferenciaNombre = models.CharField('Nombre de la referencia Comercial', max_length=200, blank=False)
    ReferenciaContacto = models.CharField('Contacto de la referencia Comercial', max_length=200, blank=False)
    ReferenciaTelefono = models.CharField('Telefono de la referencia Comercial', max_length=200, blank=False)
    ReferenciaNombre2 = models.CharField('Nombre de la referencia Comercial', max_length=200, blank=True)
    ReferenciaContacto2 = models.CharField('Contacto de la referencia Comercial', max_length=200, blank=True)
    ReferenciaTelefono2 = models.CharField('Telefono de la referencia Comercial', max_length=200, blank=True)
    ReferenciaNombre3 = models.CharField('Nombre de la referencia Comercial', max_length=200, blank=True)
    ReferenciaContacto3 = models.CharField('Contacto de la referencia Comercial', max_length=200, blank=True)
    ReferenciaTelefono3 = models.CharField('Telefono de la referencia Comercial', max_length=200, blank=True)
    ReferenciaBancariaBanco = models.CharField('Banco de la referencia Bancaria', max_length=200, blank=False)
    ReferenciaBancariaCuenta = models.CharField('Cuenta de la referencia Bancaria', max_length=200, blank=False)
    ReferenciaBancariaTelefono = models.CharField('Telefono de la referencia Bancaria', max_length=200, blank=False)
    ReferenciaNombrePersonal = models.CharField('Nombre de la referencia Personal', max_length=200, blank=False)
    ReferenciaDireccionPersonal = models.CharField('Dirección de la referencia Personal', max_length=200, blank=False)
    ReferenciaTelefonoPersonal = models.CharField('Telefono de la referencia Personal', max_length=200, blank=False)
    ReferenciaNombrePersona2 = models.CharField('Nombre de la referencia Personal', max_length=200, blank=True)
    ReferenciaDireccionPersona2 = models.CharField('Dirección de la referencia Personal', max_length=200, blank=True)
    ReferenciaTelefonoPersona2 = models.CharField('Telefono de la referencia Personal', max_length=200, blank=True)
    ReferenciaNombrePersona3 = models.CharField('Nombre de la referencia Personal', max_length=200, blank=True)
    ReferenciaDireccionPersona3 = models.CharField('Dirección de la referencia Personal', max_length=200, blank=True)
    ReferenciaTelefonoPersona3 = models.CharField('Telefono de la referencia Personal', max_length=200, blank=True)
    DocumentosEntregados = models.CharField(max_length=255, choices=DOCUMENTOS, blank=True)

    class Meta:
        verbose_name = 'Solicitud de Credito'
        ordering = ['-id']

    def __str__(self):
        return f'Solicitud de credito numero {self.id} de {self.RazonSocial}'
