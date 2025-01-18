from manim import *


TEXT_COLOR = ManimColor('#000000')
BG_COLOR = ManimColor('#D3D3D3')
# Other options for the background color:
#     - D3D3D3: Light gray
#     - D6EAF8: Light blue
#     - 4A5568: Blue
#     - FF7F50: Coral
LOGO_COLOR_DARK_BLUE = ManimColor('#313183')
LOGO_COLOR_LIGHT_BLUE = ManimColor('#2a93d1')


class TemplateScene(Scene):
    def _initialize_template(self):
        self.camera.background_color = BG_COLOR

        finki_logo = VGroup(
            Rectangle(height=3.5, width=.8).shift(LEFT * 2)  # I
            .set_color(color=LOGO_COLOR_LIGHT_BLUE)
            .set_opacity(1)
            .set_stroke(color=BLACK, width=2),
            Difference(Circle(radius=2, color=BLUE).set_opacity(1), Circle(radius=1.3))  # O
            .shift(RIGHT)
            .set_color(LOGO_COLOR_DARK_BLUE)
            .set_opacity(1)
            .set_stroke(color=BLACK, width=2)
        ).set_z_index(float('inf')).scale_to_fit_height(.7).align_on_border(UP + LEFT)
        self.add(finki_logo)

    def initialize_scene(self, title: list[str] | None = None, author: str | None = None, skip_intro: bool = False):
        self._initialize_template()
        if skip_intro:
            return
        fade_animations = []

        faculty_name = VGroup(
            Text('"Ss. Cyril and Methodius" University in Skopje', slant=ITALIC, font_size=22, color=TEXT_COLOR),
            Text('Faculty of Computer Science and Engineering', weight=BOLD, font_size=28, color=TEXT_COLOR)
        ).arrange(DOWN, buff=.1).align_on_border(UP, buff=.3)
        faculty_name.move_to((faculty_name.get_center()[0], self.mobjects[0].get_center()[1], 0))
        self.add(faculty_name)
        fade_animations.append(FadeOut(faculty_name, shift=UP))

        if not title:
            title = ['Example Title']
        title_text = VGroup(*[Text(sentence, font_size=36, color=TEXT_COLOR) for sentence in title]).arrange(DOWN, buff=.1)
        self.add(title_text)
        fade_animations.append(FadeOut(title_text, shift=LEFT))

        if author:
            author_text = Text(f'Creator: {author}', font_size=22, color=TEXT_COLOR).align_on_border(DOWN + LEFT)
            self.add(author_text)
            fade_animations.append(FadeOut(author_text, shift=DOWN))

        self.wait(1)
        self.play(AnimationGroup(*fade_animations, lag_ratio=.1))
        self.wait(.2)


class ExampleScene(TemplateScene):
    def construct(self):
        self.initialize_scene(
            title=['This is an example title', 'displayed on two rows'],
            author='Name Surname'
        )

        # Your code goes here
        self.play(Write(circle := Circle()))
        self.wait(.2)
        self.play(Unwrite(circle))
        self.wait(1)

        # Render the animation by writing the following in the terminal:
        #   manim starter_code.py ExampleScene -pqm
