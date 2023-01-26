from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.fields import proxy
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Usuario(AbstractUser):
    class Roles(models.TextChoices):
        PARTICIPANTE =  "PARTICIPANTE","Participante"
        INSTRUCTOR =  "INSTRUCTOR","Instructor"
        RESPONSABLE =  "RESPONSABLE","Responsable"


    rol = models.CharField(max_length=50,choices=Roles.choices,default=Roles.PARTICIPANTE)
    imagen = models.ImageField(default="male_avatar.svg",null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class ParticipanteManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(rol=Usuario.Roles.PARTICIPANTE)

class InstructorManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(rol=Usuario.Roles.INSTRUCTOR)


class ResponsableManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(rol=Usuario.Roles.RESPONSABLE)

class Participante(Usuario):
    objects = ParticipanteManager()
    class Meta:
        proxy = True
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.rol = Usuario.Roles.PARTICIPANTE
        return super().save(*args,**kwargs)

class Instructor(Usuario):
    objects = InstructorManager()
    class Meta:
        proxy = True
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.rol = Usuario.Roles.INSTRUCTOR
        return super().save(*args,**kwargs)

class Responsable(Usuario):
    objects = ResponsableManager()
    class Meta:
        proxy = True
    
    def save(self,*args,**kwargs):
        if not self.pk:
            self.rol = Usuario.Roles.RESPONSABLE
        return super().save(*args,**kwargs)




class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    TIPO_EVENTOS = (
            ('Diplomado','Diplomado'),
            ('Curso','Curso'),
            ('Taller','Taller'),
            ('Programa Especial','Programa Especial')
        )
    TipoEventos =  models.CharField(max_length=30,null=True,choices=TIPO_EVENTOS)
    TIPO_MODALIDAD = (
            ('En Linea', 'En Linea'),
            ('Presencial','Presencial'),
            ('Mixta','Mixta')
        )
    modalidad = models.CharField(max_length=30,null=True,choices=TIPO_MODALIDAD)
    objetivos = models.TextField(null=True)
    experiencias = models.TextField(null=True)
    contenido = models.TextField(null=True)
    recursos_y_materiales = models.TextField(null=True,blank=True)
    Estrategias_de_Evaluacion = models.TextField(null=True)
    Duracion_en_horas = models.PositiveIntegerField(default=1,validators=[MinValueValidator(10), MaxValueValidator(400)])
    Fecha_de_Inicio = models.DateField()
    Fecha_de_Fin = models.DateField()
    Referencias_y_bibliografia = models.TextField(null=True,blank=True)
    Utilidad_y_Oportunidad_del_programa = models.TextField(null=True)
    Cupo_Maximo = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(200)])
    Requisistos_de_Acreditacion = models.TextField(null=True)
    Experiencia_y_pericia_de_Instructores = models.TextField(null=True)
    Dirigido_a = models.TextField(null=True)
    Requisitos_de_Participacion = models.TextField(null=True)
    Curriculum_de_los_Instructores = models.TextField(null=True)
    Capacidad_de_autofinanciamiento = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    responsable = models.ForeignKey(Responsable, null=True, on_delete= models.SET_NULL,default=Responsable)
    ESTATUS = (
            ('Aceptado','Aceptado'),
            ('Pendiente','Pendiente'),
            ('Rechazado','Rechazado')
        )
    estatus = models.CharField(max_length=20,default=ESTATUS[1], choices=ESTATUS)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.nombre
