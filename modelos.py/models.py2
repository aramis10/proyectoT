de  Django . modelos de  importación  de base de datos

# Crea tus modelos aquí.
clase  Persona ( modelos . Modelo ):
    id  =  modelos . AutoField ( primary_key = True )
    nombre  =  modelos . CharField ( max_length = 60 )
    apellido  =  modelos . CharField ( max_length = 100 )
    dni = modelos . CharField ( max_length = 8 )
    fecha = modelos . Campo de fecha ( auto_ahora = Verdadero )
    club  =  modelos . CharField ( max_length = 50 )
    foto  =  modelos . campo de imagen (
        upload_to  =  'foto/%Y/%m/%d' ,
        en blanco  =  Verdadero ,
        verbose_name  = ( 'Foto de la persona' )
    )
  
    

 metaclase : _
    verbose_name  = ( 'Persona' )
    verbose_name_plural  = ( 'Persona' )
    
    

def  _str_ ( uno mismo ):
    devolverse  a uno mismo .
