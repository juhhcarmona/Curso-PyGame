#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

#
#  Copylefth (c) 2009, Grudejo:
#    Aline Grazielle Silva Reis
#    Julia Carmona Almeida Chaves
#    Luziany Maria de Oliveira
#    Joyce Karoline Dare
#    Prof. Douglas Machado Tavares
#

import pygame
from ator import Ator
from cenario import Cenario
from pygame.constants import *


class Jogo:
    """ Classe Jogo """

    def __init__(self):
        """ Construtor:  __init__() -> instancia de jogo """
        pygame.init()
        self.tela = pygame.display.set_mode((800, 600), FULLSCREEN)
        self.cenario = Cenario(self.tela)
        self.cenario.area.fill((65, 171, 73))
        self.cenario.construir()


    def criar_atores(self):
        """ Cria os atores """
        self.joyce = Ator(400, 300)
        self.joyce.inserir_estado("EsqDir")
        for x in range(1, 5):
            self.joyce.inserir_pose("imagens/joyce_ED_%02i.png" % x)
        self.joyce.inserir_estado("DirEsq")
        for x in range(1, 5):
            self.joyce.inserir_pose("imagens/joyce_DE_%02i.png" % x)
        self.joyce.inserir_estado("CimaBaixo")
        for x in range(1, 5):
            self.joyce.inserir_pose("imagens/joyce_CB_%02i.png" % x)
        self.joyce.inserir_estado("BaixoCima")
        for x in range(1, 5):
            self.joyce.inserir_pose("imagens/joyce_BC_%02i.png" % x)
        self.grupo_atores = pygame.sprite.RenderPlain((self.joyce))


    def atualizar_atores(self):
        """ Atualiza os atores """
        retangulo = self.tela.get_rect()
        if (self.joyce.estado == "EsqDir"):
            #self.joyce.rect.x += 4
            self.cenario.mover(4, 0)
        elif (self.joyce.estado == "CimaBaixo"):
            #self.joyce.rect.y += 4
            self.cenario.mover(0, 4)
        elif (self.joyce.estado == "DirEsq"):
            #self.joyce.rect.x -= 4
            self.cenario.mover(-4, 0)
        elif (self.joyce.estado == "BaixoCima"):
            #self.joyce.rect.y -= 4
            self.cenario.mover(0, -4)


    def repintar_tela(self):
        """ Repinta a tela """
        self.cenario.repintar()
        self.grupo_atores.update()
        self.grupo_atores.draw(self.tela)
        pygame.display.flip()


    def tratar_evento_teclado(self, evento):
        """ Observa e trata os eventos """
        tecla = evento.key
        if ((tecla == K_ESCAPE) or (tecla == K_q)):
            raise SystemExit
        elif (evento.type == KEYDOWN):
            if (evento.key == K_UP):
                self.joyce.estado = "BaixoCima"
            elif (evento.key == K_DOWN):
                self.joyce.estado = "CimaBaixo"
            elif (evento.key == K_LEFT):
                self.joyce.estado = "DirEsq"
            elif (evento.key == K_RIGHT):
                self.joyce.estado = "EsqDir"


    def tratar_eventos(self):
        """ Observa e trata os eventos """
        for evento in pygame.event.get():
            if (evento.type == QUIT):
                raise SystemExit
            if (evento.type == KEYDOWN):
                self.tratar_evento_teclado(evento)


    def rodar(self):
        """ Roda o jogo """
        self.criar_atores()
        FPS = 8
        relogio = pygame.time.Clock()
        while (True):
            self.tratar_eventos()
            self.atualizar_atores()
            self.repintar_tela()
            relogio.tick(FPS)


if (__name__ == "__main__"):
    jogo = Jogo()
    jogo.rodar()
