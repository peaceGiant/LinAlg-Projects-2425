from manim import *


class Intro(Scene):
    def construct(self):
        square = Square()

        self.add(square)
        self.wait(1)

        print(self.mobjects)
        print(self.mobjects[-1])

        self.remove(square)
        self.wait(1)


class AnimationsIntro(Scene):
    def construct(self):
        self.interactive_embed()
        triangle = Triangle(color=DARK_BLUE)
        triangle.shift(2 * LEFT + UP)
        triangle.scale(2).set_fill(BLUE).set_opacity(0.8)

        self.play(Write(triangle), run_time=2)

        self.play(
            triangle.animate
            .set_fill(PURE_BLUE)
            .set_opacity(0.2)
            .rotate(90 * DEGREES)
        )

        self.play(FadeOut(triangle), run_time=4)
