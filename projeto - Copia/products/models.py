from django.db import models
from django.utils.text import slugify


class Marca(models.Model):
    marca = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.marca)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.marca


class TipoGuitarra(models.Model):
    """
    Examples: Stratocaster, Superstrat, Telecaster, Les Paul, Semi-Hollow, Offset
    """
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = "Tipo de Guitarra"
        verbose_name_plural = "Tipos de Guitarra"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Guitarra(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="guitarras")
    tipo = models.ForeignKey(
        TipoGuitarra,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="guitarras"
    )
    modelo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to="guitarras/", blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True)
    em_destaque = models.BooleanField(default=False)
    disponibilidade = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.marca.marca}-{self.modelo}")
            slug = base_slug
            counter = 1
            while Guitarra.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
