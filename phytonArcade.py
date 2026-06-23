import arcade, random

class Jogador(arcade.Sprite):
    def __init__(self):
        super().__init__("personagem-direita.png", scale= 0.1)

        self.textura_direita = arcade.load_texture("personagem-direita.png")
        self.textura_esquerda = arcade.load_texture("personagem-esquerda.png")

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x > 0: 
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        if self.right > 800:
            self.change_x = 0
            self.right = 800
        if self.top > 600:
            self.change_y = 0
            self.top = 600
        if self.left < 0:
            self.change_x = 0
            self.left = 0
        if self.bottom < 0:
            self.change_y = 0
            self.bottom = 0

class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.1)

class MoedaEspecial(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.2)

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > 800:
            self.change_x *= -1
        if self.bottom < 0 or self.top > 600:
            self.change_y *= -1

class Inimigo(arcade.Sprite):
    def __init__(self):
        super().__init__("espinho.png", scale=0.1)

class TelaInicial(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.clear()
        arcade.draw_text("Jogo - O Coletor de Moedas", 800 / 2, 400, arcade.color.WHITE, 32, anchor_x="center")
        arcade.draw_text("Pressione [J] para jogar", 800 / 2, 300, arcade.color.LIGHT_SEA_GREEN, 18, anchor_x="center")
        arcade.draw_text("Pressione [ESC] para SAIR", 800 / 2, 240, arcade.color.LIGHT_SEA_GREEN, 18, anchor_x="center")
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.J:
            tela_jogo = JanelaJogo()
            self.window.show_view(tela_jogo)
        elif key == arcade.key.ESCAPE:
            arcade.close_window()

class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Desafio Final - Coletor Pro")
        arcade.set_background_color(arcade.color.AMAZON) # [8, 14]
        self.setup()

    def setup(self):
        self.pontuacao = 0
        self.tempo = 0.0
        self.jogo_finalizado = False
        self.velocidade_base = 3

        self.sprite_jogador = arcade.SpriteList()
        self.sprite_moedas = arcade.SpriteList()
        self.sprite_inimigos = arcade.SpriteList()

        self.jogador = Jogador()
        self.jogador.center_x = 400
        self.jogador.center_y = 300
        self.sprite_jogador.append(self.jogador)

        for i in range(random.randint(10, 20)):
            m = Moeda()
            m.center_x = random.randint(50, 750)
            m.center_y = random.randint(50, 550)
            self.sprite_moedas.append(m)

        self.especial = MoedaEspecial()
        self.especial.center_x = random.randint(50, 750)
        self.especial.center_y = random.randint(50, 550)
        self.especial.change_x = self.velocidade_base
        self.especial.change_y = self.velocidade_base
        self.sprite_moedas.append(self.especial)

        for i in range(random.randint(1, 5)):
            e = Inimigo()
            e.center_x = random.randint(50, 700)
            e.center_y = random.randint(50, 500)
            self.sprite_inimigos.append(e)

    def on_draw(self):
        self.clear()

        if not self.jogo_finalizado:
            self.sprite_moedas.draw()
            self.sprite_inimigos.draw()
            self.sprite_jogador.draw()

            arcade.draw_text(f"Pontos: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14)
            arcade.draw_text(f"Tempo: {self.tempo:.2f}s", 10, 550, arcade.color.WHITE, 12)
        else:
            arcade.draw_text("PARABÉNS! JOGO CONCLUÍDO", 150, 350, arcade.color.YELLOW, 30)
            arcade.draw_text(f"Pontuação Final: {self.pontuacao} | Tempo: {self.tempo:.2f}s", 200, 300, arcade.color.WHITE, 16)
            arcade.draw_text("Pressione R para recomeçar ou ESC para sair", 220, 260, arcade.color.LIGHT_GRAY, 12)

    def on_update(self, delta_time):
        if self.jogo_finalizado:
            return

        self.tempo += delta_time

        self.sprite_jogador.update(delta_time)
        self.sprite_moedas.update(delta_time)
        self.sprite_inimigos.update(delta_time)

        moedas_atingidas = arcade.check_for_collision_with_list(self.jogador, self.sprite_moedas)
        for moeda in moedas_atingidas:
            moeda.remove_from_sprite_lists()
            if moeda == self.especial:
                self.pontuacao += 5
            else:
                self.pontuacao += 1
        
        inimigos_atingidos = arcade.check_for_collision_with_list(self.jogador, self.sprite_inimigos)
        for inimigo in inimigos_atingidos:
            self.pontuacao -= 1
            inimigo.remove_from_sprite_lists()

        if len(self.sprite_moedas) == 0:
            self.jogo_finalizado = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.jogador.change_y = self.velocidade_base
        if key == arcade.key.DOWN or key == arcade.key.S:
            self.jogador.change_y = -self.velocidade_base
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.jogador.change_x = -self.velocidade_base
        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.jogador.change_x = self.velocidade_base
        
        elif key == arcade.key.ESCAPE:
            arcade.close_window()
        
        elif key == arcade.key.R and self.jogo_finalizado:
            self.setup()

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D]:
                self.jogador.change_x = 0
                
        if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.W, arcade.key.S]:
            self.jogador.change_y = 0

def main():
    JanelaJogo()
    arcade.run()

if __name__ == "__main__":
    main()