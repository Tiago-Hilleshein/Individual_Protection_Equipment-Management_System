# gerenciador_de_epi/models.py - Código Final

from django.db import models

# =======================================================
# MODELO EPI (Equipamentos de Proteção Individual)
# =======================================================
class EPI(models.Model):
    nome = models.CharField(
        max_length=100, 
        verbose_name='Nome do EPI'
    )
    ca = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name='Número do CA'
    )
    validade = models.DateField(
        verbose_name='Data de Validade'
    )

    def __str__(self):
        return self.nome

# =======================================================
# MODELO COLABORADOR
# =======================================================
class Colaborador(models.Model):
    nome_completo = models.CharField(
        max_length=200, 
        verbose_name='Nome Completo'
    )
    matricula = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name='Matrícula'
    )
    setor = models.CharField(
        max_length=100, 
        verbose_name='Setor'
    )
    
    def __str__(self):
        return self.nome_completo

class Emprestimo(models.Model):
    # Relacionamento 1: O colaborador que recebeu o EPI
    colaborador = models.ForeignKey(
        Colaborador, 
        on_delete=models.CASCADE, 
        verbose_name='Colaborador'
    )
    
    # Relacionamento 2: O EPI que foi emprestado
    epi = models.ForeignKey(
        EPI, 
        on_delete=models.CASCADE, 
        verbose_name='EPI Emprestado'
    )
    
    # Data em que o EPI foi entregue
    data_emprestimo = models.DateField(
        auto_now_add=True, # Define a data automaticamente no momento da criação
        verbose_name='Data de Empréstimo'
    )

    def __str__(self):
        return f"{self.epi.nome} entregue a {self.colaborador.nome_completo}"