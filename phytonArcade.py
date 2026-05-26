import arcade

class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Titulo padrão")
        arcade.set_background_color(arcade.color.AMAZON)

        self.personagem = Jogador()
        self.personagem.center_x = 400
        self.personagem.center_y = 300
    def on_draw(self):
        self.clear()
        arcade.draw_sprite(self.personagem)

    def on_update(self, delta_time):
        pass

class Jogador(arcade.Sprite):
    def __init__(self):
        super().__init__("personagem-direita.png", scale= 0.2)

        self.textura_direita = arcade.load_texture("personagem-direita.png")
        self.textura_esquerda = arcade.load_texture("personagem-esquerda.png")

    def update(self):
        pass

def main():
    tela = JanelaJogo()
    arcade.run()

if __name__ == "__main__":
    main()