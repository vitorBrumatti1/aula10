import arcade
import random

LARGURA = 800
ALTURA = 600
TITULO = "Desafio de POO"

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("personagem-direita.png", scale=0.1)
        self.textura_direita = arcade.load_texture("personagem-direita.png")
        self.textura_esquerda = arcade.load_texture("personagem-esquerda.png")

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        if self.left < 0: self.left = 0
        if self.right > LARGURA: self.right = LARGURA
        if self.bottom < 0: self.bottom = 0
        if self.top > ALTURA: self.top = ALTURA

class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.08)

class MoedaEspecial(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.1)
    
    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > LARGURA: self.change_x *= -1
        if self.bottom < 0 or self.top > ALTURA: self.change_y *= -1

class Inimigo(arcade.Sprite):
    def __init__(self):
        super().__init__("espinho.png", scale=0.05)
    
    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0 or self.right > LARGURA: self.change_x *= -1
        if self.bottom < 0 or self.top > ALTURA: self.change_y *= -1

class InimigoEspecial(arcade.Sprite):
    def __init__(self, player):
        super().__init__("espinho.png", scale=0.09)
        self.player = player
        self.velocidade = 1.5

    def update(self, delta_time):
        if self.center_x < self.player.center_x: self.center_x += self.velocidade
        elif self.center_x > self.player.center_x: self.center_x -= self.velocidade
        
        if self.center_y < self.player.center_y: self.center_y += self.velocidade
        elif self.center_y > self.player.center_y: self.center_y -= self.velocidade


class MenuView(arcade.View):
    def on_show_view(self): arcade.set_background_color(arcade.color.AMAZON)
    
    def on_draw(self):
        self.clear()
        arcade.draw_text("UM DOS JOGOS JÁ FEITOS: MULTI-TELAS", LARGURA/2, 400, arcade.color.YELLOW, 30, anchor_x="center")
        arcade.draw_text("[J] Jogar | [I] Instruções | [S] Sobre | [ESC] Sair", LARGURA/2, 300, arcade.color.WHITE, 16, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.J: self.window.show_view(GameView())
        elif key == arcade.key.I: self.window.show_view(InstrucoesView())
        elif key == arcade.key.S: self.window.show_view(SobreView())
        elif key == arcade.key.ESCAPE: arcade.close_window()

class InstrucoesView(arcade.View):
    def on_draw(self):
        self.clear()
        arcade.draw_text("INSTRUÇÕES", LARGURA/2, 450, arcade.color.WHITE, 30, anchor_x="center")
        arcade.draw_text("Colete todas as moedas para vencer.\nCuidado com os espinhos: eles tiram pontos!\nInimigos vermelhos perseguem você.", LARGURA/2, 350, arcade.color.LIGHT_GRAY, 14, anchor_x="center", multiline=True, width=600)
        arcade.draw_text("Use WASD ou Setas para mover. [M] Menu", LARGURA/2, 200, arcade.color.WHITE, 12, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.M or key == arcade.key.ESCAPE: self.window.show_view(MenuView())

class SobreView(arcade.View):
    def on_draw(self):
        self.clear()
        arcade.draw_text("DESENVOLVIDO POR:", LARGURA/2, 450, arcade.color.WHITE, 25, anchor_x="center")
        arcade.draw_text("Vitor Rufino Brumatti - 3 Info", LARGURA/2, 350, arcade.color.YELLOW, 18, anchor_x="center")
        arcade.draw_text("[M] Menu", LARGURA/2, 100, arcade.color.WHITE, 12, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.M or key == arcade.key.ESCAPE: self.window.show_view(MenuView())

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.pontos = 0
        self.tempo = 0
        self.alerta_dano = False
        self.alerta_timer = 0
        
        self.spr_player = arcade.SpriteList()
        self.spr_moedas = arcade.SpriteList()
        self.spr_inimigos = arcade.SpriteList()
        self.spr_inimigo_esp = arcade.SpriteList()

        self.player = Player()
        self.player.center_x = 400
        self.player.center_y = 300
        self.spr_player.append(self.player)

        for i in range(25):
            m = Moeda()
            self.spawn_seguro(m, self.spr_moedas)
            self.spr_moedas.append(m)

        me = MoedaEspecial()
        self.spawn_seguro(me, self.spr_moedas)
        me.change_x = me.change_y = 3
        self.spr_moedas.append(me)

        ini = Inimigo()
        self.spawn_seguro(ini, self.spr_inimigos)
        ini.change_x = 2
        ini.change_y = 2
        self.spr_inimigos.append(ini)

        self.perseguidor = InimigoEspecial(self.player)
        self.spawn_seguro(self.perseguidor, self.spr_inimigo_esp)
        self.spr_inimigo_esp.append(self.perseguidor)

    def spawn_seguro(self, sprite, lista_existente):
        tentativas = 0
        while tentativas < 100:
            sprite.center_x = random.randint(50, LARGURA - 50)
            sprite.center_y = random.randint(50, ALTURA - 50)
            
            col_player = arcade.check_for_collision(sprite, self.player)
            col_lista = arcade.check_for_collision_with_list(sprite, lista_existente)
            
            if not col_player and len(col_lista) == 0:
                break
            tentativas += 1

    def on_draw(self):
        self.clear()
        self.spr_moedas.draw()
        self.spr_inimigos.draw()
        self.spr_inimigo_esp.draw()
        self.spr_player.draw()

        arcade.draw_text(f"Pontos: {self.pontos}  |  Tempo: {self.tempo:.1f}s", 10, 20, arcade.color.WHITE, 14)
        
        if self.alerta_dano:
            arcade.draw_text("DANO RECEBIDO!", LARGURA/2, 500, arcade.color.RED, 20, anchor_x="center")

    def on_update(self, delta_time):
        self.tempo += delta_time
        self.spr_player.update()
        self.spr_moedas.update()
        self.spr_inimigos.update()
        self.spr_inimigo_esp.update()

        col_moedas = arcade.check_for_collision_with_list(self.player, self.spr_moedas)
        for m in col_moedas:
            self.pontos += 5 if isinstance(m, MoedaEspecial) else 1
            m.remove_from_sprite_lists()

        if arcade.check_for_collision_with_list(self.player, self.spr_inimigos):
            self.pontos -= 1
            self.ativar_alerta()

        if arcade.check_for_collision_with_list(self.player, self.spr_inimigo_esp):
            self.pontos -= 1
            self.ativar_alerta()
            self.spawn_seguro(self.perseguidor, self.spr_moedas)

        if self.alerta_dano:
            self.alerta_timer -= delta_time
            if self.alerta_timer <= 0: self.alerta_dano = False

        if len(self.spr_moedas) == 0:
            self.window.show_view(GameOverView(self.pontos, self.tempo))

    def ativar_alerta(self):
        self.alerta_dano = True
        self.alerta_timer = 0.5

    def on_key_press(self, key, modifiers):
        v = 4
        if key in [arcade.key.UP, arcade.key.W]: self.player.change_y = v
        elif key in [arcade.key.DOWN, arcade.key.S]: self.player.change_y = -v
        elif key in [arcade.key.LEFT, arcade.key.A]: self.player.change_x = -v
        elif key in [arcade.key.RIGHT, arcade.key.D]: self.player.change_x = v
        elif key == arcade.key.ESCAPE: self.window.show_view(MenuView())

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.W, arcade.key.DOWN, arcade.key.S]: self.player.change_y = 0
        if key in [arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D]: self.player.change_x = 0

class GameOverView(arcade.View):
    def __init__(self, score, tempo):
        super().__init__()
        self.score = score
        self.tempo = tempo

    def on_draw(self):
        self.clear()
        if self.score >= 30:
            arcade.draw_text("VITÓRIA PERFEITA!", LARGURA/2, 400, arcade.color.GOLD, 30, anchor_x="center")
            arcade.draw_text("Elogio: Você escapou dos inimigos com maestria!", LARGURA/2, 350, arcade.color.WHITE, 14, anchor_x="center")
        else:
            arcade.draw_text("JOGO CONCLUÍDO", LARGURA/2, 400, arcade.color.WHITE, 30, anchor_x="center")
        
        arcade.draw_text(f"Score Final: {self.score} | Tempo: {self.tempo:.1f}s", LARGURA/2, 300, arcade.color.LIGHT_GRAY, 18, anchor_x="center")
        arcade.draw_text("[M] Menu | [ESC] Sair", LARGURA/2, 200, arcade.color.LIGHT_GRAY, 12, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.M: self.window.show_view(MenuView())
        elif key == arcade.key.ESCAPE: arcade.close_window()

def main():
    janela = arcade.Window(LARGURA, ALTURA, TITULO)
    janela.show_view(MenuView())
    arcade.run()

if __name__ == "__main__":
    main()